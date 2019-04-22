module.exports.convertReadGroupResponse = function convertReadGroupResponse(streamData){
    let messages = [];
    for(let element of streamData){
        let entry = {
            id: element[0]
        }
        for(let i=0; i< element[1].length; i+=2){
            if(element[1][i] && element[1][i+1]){
                entry[element[1][i]] = element[1][i+1];
            }
        }
        messages.push(entry);
    }
    return messages;
}

module.exports.convertPendingResponse = function convertPendingResponse(pendingResponse){
    let pendingMsgs = [];
    if(pendingResponse[0] && pendingResponse[0].length > 0 && pendingResponse[0].length % 4 ===0){
        for(let i=0; i < pendingResponse[0].length;i+=4){
            let pending = {
                'id': pendingResponse[0][0],
                'consumer': pendingResponse[0][1],
                'passTime': pendingResponse[0][2],
                'deliveryTimes': pendingResponse[0][3]
            }
            pendingMsgs.push(pending);
        }
    }
    return pendingMsgs;
}
