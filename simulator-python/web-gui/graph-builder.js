var baseUrl = "http://localhost:5000/";
var graph;

var posXPerID = {};
var posYPerID = {};

var initGraph = function () {
    graph = {
        nodes: [],
        edges: []
    };
}

var  s = new sigma(
    {
        renderer: {
            container: document.getElementById('sigma-container'),
            type: 'canvas'
        },
        settings: {
            minArrowSize: 10
        }
    }
);
var dragListener = new sigma.plugins.dragNodes(s, s.renderers[0]);

var drawGraph = function () {
    initGraph();
    $.get(baseUrl + "get-nodes-data", function (dataStr) {
        let data = JSON.parse(dataStr);
        if(data.length > 0) {
            buildGraph(data);
            // load the graph
            s.graph.clear();
            s.graph.read(graph);
            // Bind the events:
            s.bind('doubleClickNode', clickNodeEvent);
            // draw the graph
            s.refresh();
        }
    });
}

var clickNodeEvent = function(nodeEvent){
    alert(`Node id: ${nodeEvent.data.node.id}, have ${nodeEvent.data.node.inbox.packets_queue.queue.length} wating messages`);
}

dragListener.bind('dragend', function(event) {
    var currId = parseInt(event.data.node.id);
    newPosX = event.data.node.x;
    newPosY = event.data.node.y;
    posXPerID[currId] = newPosX;
    posYPerID[currId] = newPosY;
});

var buildGraph = function (data) {
    for (let i = 0; i < data.length; i++) {
        let size = 12;
        if(data[i].inbox.packets_queue.queue.length > 0){
            size += data[i].inbox.packets_queue.queue.length * 3;
        }
        let posX = posXPerID[data[i].ID] ? posXPerID[data[i].ID] : Math.random() * 100;
        let posY = posYPerID[data[i].ID] ? posYPerID[data[i].ID] : Math.random() * 100;

        if(!posXPerID[data[i].ID]) {
            posXPerID[data[i].ID] = posX;
        }
        if(!posYPerID[data[i].ID]) {
            posYPerID[data[i].ID] = posY;
        }

        graph.nodes.push({
            id:  "" + data[i].ID,
            label: "" + data[i].ID,
            x:  posX,
            y: posY,
            size: size,
            inbox: data[i].inbox,
            color: data[i].color
        });
    }

    for (let i = 0; i < data.length; i++) {
        for(let j=0 ; j < data[i].edges.length; j++){
            graph.edges.push({
                id: `e-${i}:${j}`,
                source: data[i].edges[j].start_node_id,
                target: data[i].edges[j].end_node_id,
                color: 'Blue',
                type: 'curvedArrow'
            });
        }
    }
}