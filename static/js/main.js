function getGraphData(json) {

  var nodesFormatedList = [];
  var edgesFormatedList = [];

  for (let i = 0; i < json.vertices.length; i++) {
    nodesFormatedList.push({ id: json.vertices[i].id, label: json.vertices[i].name });
  }

  for (let i = 0; i < json.edges.length; i++) {
    edgesFormatedList.push({ from: json.edges[i].from_id, to: json.edges[i].to_id });
  }

  var nodes = new vis.DataSet(nodesFormatedList);

  var edges = new vis.DataSet(edgesFormatedList)

  // create an array with nodes
  //var nodes = new vis.DataSet([
  //  { id: 1, label: "Node 1" },
  //  { id: 2, label: "Node 2" },
  //  { id: 3, label: "Node 3" },
  //  { id: 4, label: "Node 4" },
  //  { id: 5, label: "Node 5" },
  //]);

  // create an array with edges
  //var edges = new vis.DataSet([
  //  { from: 1, to: 3 },
  //  { from: 1, to: 2 },
  //  { from: 2, to: 4 },
  //  { from: 2, to: 5 },
  //  { from: 3, to: 3 },
  //]);

  // create a network
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges,
  };
  var options = {};
  var network = new vis.Network(container, data, options);

  console.log(json)
}

ajax("GET", "Graph/GetGraphData", getGraphData)
