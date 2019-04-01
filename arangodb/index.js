var arangojs = require('arangojs');
var randomstring = require('randomstring');
let username = 'root';
let password='';
let host = '127.0.0.1';
let port = '8529';
var counter = 1;

var vertexCollection = "websites";
var edgesCollection = "edges";
var graphName = "websitesGraph";

// Connection to ArangoDB
db = new arangojs.Database({
    url: `http://${host}:${port}`,
    databaseName: false
});
db.useBasicAuth(username, password);


var createVertexCollection = async function(collectionName){
    const collection = db.collection(collectionName);
    await collection.create();
};

var createEdgeCollection = async function(collectionName){
    const collection = db.edgeCollection(collectionName);
    await collection.create({
        type: 3,
        waitForSync: true
    });
};


var initVertices = async function (elementsNum, elementGenerator, collectionName) {
    let collection = db.collection(collectionName);
    for(let i=0; i < elementsNum; i++){
        let data = elementGenerator();
        await collection.save(data.data);
    }
};


var websitesGenerator = function () {
    let url = generateUrl();
    return {
        id: url,
        data: {
            'url': url,
            '_key': url.replace('http://',''),
            'creator': `stav${counter++}`
        }
    }
};


let generateUrl = function () {
    let value = randomstring.generate({
        length: 12,
        charset: 'abcdefghijklmnopqrstuvwxyz'
    });
    return `http://www.${value}.com`;
};

let getVerticesIds = async function(vertexCollection){
    let collection = db.collection(vertexCollection);
    return await collection.list("id");
}

let initEdges = async function(vertexCollection, edgesCollectionName){
    let ids = await getVerticesIds(vertexCollection);
    let passVertices = 0;
    let edgesCollection = db.edgeCollection(edgesCollectionName)
    for(let i=0; i< ids.length; i++){
        passVertices+=1;
        console.log(passVertices);
        for(let j=0; j< ids.length; j++){
            let edgeProb = Math.random();
            if(i != j && edgeProb < 0.2){
                let element = {
                    data: 'stav1',
                    _from: ids[i],
                    _to: ids[j]
                };
                await  edgesCollection.save(element);
            }
        }
    }
};



let createGraph = async function (graphName, edgeCollectionName, vertexCollectionName) {
    const graph = db.graph(graphName);
    const info = await graph.create({
        edgeDefinitions: [{
            collection: edgeCollectionName,
            from: [vertexCollectionName],
            to:[vertexCollectionName]
        }]
    }).catch(err=>{
        console.log(`error: ${err.message}`);
    });
};

let checkIfExists = function(object){
    return new Promise(async (resolve, reject)=>{
        try {
            if (object.isArangoCollection) {
                resolve(true);
            }
            else {
                resolve(false)
            }
        }
        catch (err){
            console.log(`error: ${err.message}`);
            resolve(false);
        }
    })
}


let initAll = async function (verticesCollection, edgesCollection, graphName) {
    var verCollection = db.collection(verticesCollection);
    var edgCollection = db.collection(edgesCollection);
    var graph = db.graph(graphName)

    if(await checkIfExists(verCollection)) {
        await verCollection.drop();
    }
    if(await checkIfExists(edgCollection)) {
        await edgCollection.drop();
    }
    if(await checkIfExists(graph)) {
        await graph.drop();
    }
};


(async () => {
    await initAll(vertexCollection, edgesCollection, graphName);
    await createVertexCollection(vertexCollection);
    await createEdgeCollection(edgesCollection);
    await initVertices(300, websitesGenerator, vertexCollection);
    await initEdges(vertexCollection, edgesCollection);
    await createGraph(graphName, edgesCollection, vertexCollection);
    console.log('graph creation succeeded!');
})();