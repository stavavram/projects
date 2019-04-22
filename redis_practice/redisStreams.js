var Redis = require("redis");
var StreamConvertors = require('./convertors/redisStreamConvertors');

var connect = ()=>{
    return Redis.createClient({
        'host': 'localhost',
        'port': 6379
    });
};

var getPendingMsgs = async (client)=>{
    return new Promise((resolve, reject)=>{
        client.xpending('mystream' , 'mygroup', '-', '+', '10',(err, res)=>{
            if(err){
                console.log(err);
                return reject(err);
            }
            let convertedRes = StreamConvertors.convertPendingResponse(res);
            resolve(convertedRes);
        });
    })
}

var deliverFromStreams = async (client, streamName, groupName, consumerName, history = false)=>{
    return new Promise((resolve, resject)=>{
        client.xreadgroup('GROUP', groupName, consumerName, 'STREAMS', streamName, history? '0-0':'>', (err, stream)=>{
            if(err){
                console.log(err);
                return reject(err);
            }
            let convertedStream = StreamConvertors.convertReadGroupResponse(stream[0][1]);
            return resolve(convertedStream)
        });
    });
}

var readMsgFromStream = function(client, msgId){
    return new Promise((resolve, reject)=>{
        client.xrange('mystream', msgId, msgId, (err, res)=>{
            if(err){
                console.log(err);
                return reject(err);
            }
            let convertedRes = StreamConvertors.convertReadGroupResponse(res);
            resolve(convertedRes);
        });
    });
}

var setAckToMsg = function(client, streamName, groupName, msgId){
    return new Promise((resolve, reject)=>{
        client.xack(streamName , groupName, msgId, (err, res)=>{
            if(err){
                console.log(err);
                return reject(err);
            }
            if(res === 0){
                return reject();
            }
            return resolve();
        });
    });
}

var handleMsgs = async function(client, msgId){
    let msgContent = await readMsgFromStream(client, msgId);
    console.log(msgContent);
    await setAckToMsg(client, 'mystream', 'mygroup', msgId)
};

(async () => {
    let client = await connect();

    //let pendingMsgs = await getPendingMsgs(client);
    let pendingMsgs = await deliverFromStreams(client, 'mystream', 'mygroup', 'bob2', true);
    for(let pendingMsg of pendingMsgs){
        await handleMsgs(client, pendingMsg.id);
    }
    console.log('ready for new msgs');

})();

/*
client.xadd('mystream', '*', 'messages', 'apple21', 'test', '4');
let res = await deliverFromStreams(client, 'mystream', 'mygroup', 'bob2', true);
//await client.xgroup('CREATE', 'mystream', 'mygroup', '$');
*/

/*
 /*client.xreadgroup('GROUP', 'mygroup', 'bob2', 'STREAMS', 'mystream', '>', (err, stream)=>{
        if(err){
            console.log(err);
            return;
        }
        if(stream){
            let streamRes = new Stream(stream[0][0], stream[0][1]);
            console.log(streamRes.messages);
            for(let msg of streamRes.messages){
                client.xack('mystream' , 'mygroup', msg.id, (err, res)=>{
                    if(err){
                        console.log(err);
                    }else{
                        console.log(res);
                    }
                })
            }
        }
    });
*/