function getGraphData(json) {
    var nodesFormatedList = [];
    var edgesFormatedList = [];

    for (let i = 0; i < json.vertices.length; i++) {
        nodesFormatedList.push({ id: json.vertices[i].id, label: json.vertices[i].id + ":" + json.vertices[i].name });
    }

    for (let i = 0; i < json.edges.length; i++) {
        edgesFormatedList.push({ from: json.edges[i].from_id, to: json.edges[i].to_id });
    }

    var nodes = new vis.DataSet(nodesFormatedList);

    var edges = new vis.DataSet(edgesFormatedList)


    var container = document.getElementById("mynetwork");
    var data = {
        nodes: nodes,
        edges: edges,
    };
    var options = {};
    var network = new vis.Network(container, data, options);
}

function getNewGraph() {
    ajax("DELETE", "Graph/DeleteGraphData", null)
    ajax("POST", "Graph/CreateGraph?vertex_count=5", null)

    setTimeout(function() {
        document.location.reload();
    }, 1000)
}

ajax("GET", "Graph/GetGraphData", getGraphData)

document.getElementById("buttonNewGraph").addEventListener("click", getNewGraph);