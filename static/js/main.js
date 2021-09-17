let iterationCount = 5

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
    console.log("Graph/DELETE")
    ajax("POST", "Graph/CreateGraph?vertex_count=" + iterationCount, null)
    console.log("Graph/POST")
    ajax("DELETE", "Graph/DeleteGraphDataForNeo4j", null)
    console.log("GraphNeo4j/DELETE")
    ajax("POST", "Graph/CreateGraphForNeo4j", null)
    console.log("GraphNeo4j/POST")
    ajax("GET", "Graph/GetGraphData", getGraphData)
    console.log("Graph/GET")
}

function search() {
    startID = document.getElementById("search-panel-path-start").value
    endID = document.getElementById("search-panel-path-end").value

    document.getElementById("dfs-memory").innerHTML = "loading"
    document.getElementById("bfs-memory").innerHTML = "loading"
    document.getElementById("dfs-sql").innerHTML = "loading"
    document.getElementById("bfs-sql").innerHTML = "loading"
    document.getElementById("dfs-neo4j").innerHTML = "loading"
    document.getElementById("bfs-neo4j").innerHTML = "loading"

    ajax("GET", "Search/Ram/DepthFirst?start=" + startID + "&end=" + endID, updateDFSmemory)
    ajax("GET", "Search/Ram/BreadthFirst?start=" + startID + "&end=" + endID, updateBFSmemory)
    ajax("GET", "Search/MySQL/DepthFirst?start=" + startID + "&end=" + endID, updateDFSsql)
    ajax("GET", "Search/MySQL/BreadthFirst?start=" + startID + "&end=" + endID, updateBFSsql)
    ajax("GET", "Search/Neo4j/DepthFirst?start=" + startID + "&end=" + endID, updateDFSneo4j)
    ajax("GET", "Search/Neo4j/BreadthFirst?start=" + startID + "&end=" + endID, updateBFSneo4j)
}

function updateDFSmemory(data) {
    console.log("DFSmemory")
    console.log(data)
    document.getElementById("dfs-memory").innerHTML = data.time
}

function updateBFSmemory(data) {
    console.log("BFSmemory")
    console.log(data)
    document.getElementById("bfs-memory").innerHTML = data.time
}

function updateDFSsql(data) {
    console.log("DFSsql")
    console.log(data)
    document.getElementById("dfs-sql").innerHTML = data.time
}

function updateBFSsql(data) {
    console.log("BFSsql")
    console.log(data)
    document.getElementById("bfs-sql").innerHTML = data.time
}

function updateDFSneo4j(data) {
    console.log("DFSneo4j")
    console.log(data)
    document.getElementById("dfs-neo4j").innerHTML = data.time
}

function updateBFSneo4j(data) {
    console.log("BFSneo4j")
    console.log(data)
    document.getElementById("bfs-neo4j").innerHTML = data.time
}

ajax("GET", "Graph/GetGraphData", getGraphData)

//new graph
document.getElementById("buttonNewGraph").addEventListener("click", getNewGraph);

//settings
document.getElementById("buttonSearch").addEventListener("click", function() { document.getElementById("search-panel").style.display = "flex" });
document.getElementById("buttonSearchExecute").addEventListener("click", function() {
    search();
});
document.getElementById("buttonSearchExit").addEventListener("click", function() {
    document.getElementById("search-panel").style.display = "none"
});

//settings
document.getElementById("buttonSettings").addEventListener("click", function() {
    document.getElementById("settings-panel-iteration-count").value = iterationCount
    document.getElementById("settings-panel").style.display = "flex";
});
document.getElementById("buttonSettingsOk").addEventListener("click", function() {
    document.getElementById("settings-panel").style.display = "none"
    iterationCount = document.getElementById("settings-panel-iteration-count").value
});