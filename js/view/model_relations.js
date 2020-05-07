/*global view, VIS, d3 */
"use strict";

view.model.relations = function (param) {
    var svg, bg, zoom, spec = {};

    spec.w = d3v5.select("#model_view").node().clientWidth
        || VIS.model_view.plot.w;
    spec.w = Math.max(spec.w, VIS.model_view.plot.w); // set a min. width
    spec.h = Math.floor(spec.w / VIS.model_view.plot.aspect);
    spec.m = {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0
    };


    var width = spec.w;
    var height = spec.h;

    var color = d3v5.scaleOrdinal(d3v5.schemeCategory10);

    var graph = param.graph;
    //d3v5.json("graph.json").then(function (graph) {
    if (graph) {


        var label = {
            'nodes': [],
            'links': []
        };

        graph.nodes.forEach(function (d, i) {
            label.nodes.push({ node: d });
            label.nodes.push({ node: d });
            label.links.push({
                source: i * 2,
                target: i * 2 + 1
            });
        });

        var labelLayout = d3v5.forceSimulation(label.nodes)
            .force("charge", d3v5.forceManyBody().strength(-50))
            .force("link", d3v5.forceLink(label.links).distance(0).strength(2));

        var graphLayout = d3v5.forceSimulation(graph.nodes)
            .force("charge", d3v5.forceManyBody().strength(-4000))
            .force("center", d3v5.forceCenter(width / 2, height / 2))
            .force("x", d3v5.forceX(width / 2).strength(1))
            .force("y", d3v5.forceY(height / 2).strength(1))
            .force("link", d3v5.forceLink(graph.links).id(function (d) { return d.id; }).distance(50).strength(1))
            .on("tick", ticked);

        var adjlist = [];

        graph.links.forEach(function (d) {
            adjlist[d.source.index + "-" + d.target.index] = true;
            adjlist[d.target.index + "-" + d.source.index] = true;
        });

        function neigh(a, b) {
            return a == b || adjlist[a + "-" + b];
        }

  

        var parent = d3v5.select("#model_view_scaled");

        svg = parent
            .selectAll("svg")
            .data([1])
            .join(
                enter => enter.append("svg"),
                update => update,
                exit => exit.remove()
            )
            .attr("width", spec.w + spec.m.left + spec.m.right)
            .attr("height", spec.h + spec.m.top + spec.m.bottom);;



        var container = svg.selectAll("g")
            .data([1])
            .join(
                enter => enter.append("g"),
                update => update,
                exit => exit.remove()
            );



        zoom = d3v5.zoom()
        .scaleExtent([.1, 4])
        .on("zoom", function () { container.attr("transform", d3v5.event.transform); });

        svg.call(
            zoom
        );

        // zoom reset button
        d3.select("button#reset_zoom")
            .on("click", function () {                
                svg.transition().duration(750).call(
                    zoom.transform,
                    d3v5.zoomIdentity,
                    d3v5.zoomTransform(svg.node()).invert([width / 2, height / 2])
                  );
            });

        var link = container.append("g").attr("class", "links")
            .selectAll("line")
            .data(graph.links)
            .enter()
            .append("line")
            .attr("stroke", "#aaa")
            .attr("stroke-width", "1px");

        var node = container.append("g").attr("class", "nodes")
            .selectAll("g")
            .data(graph.nodes)
            .enter()
            .append("circle")
            .attr("r", function (d) { return d.size; })
            .attr("fill", function (d) { return color(d.group); })

        node.on("mouseover", focus).on("mouseout", unfocus);

        node.on("click", function (p) {
            if (!d3v5.event.shiftKey) {
                view.dfb().set_view({
                    type: "topic",
                    param: p.id+1
                });
            }
        })

        node.call(
            d3v5.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended)
        );

        var labelNode = container.append("g").attr("class", "labelNodes")
            .selectAll("text")
            .data(label.nodes)
            .enter()
            .append("text")
            .text(function (d, i) { return i % 2 == 0 ? "" : d.node.title; })
            .style("fill", "#555")
            .style("font-family", "Arial")
            .style("font-size", 12)
            .style("pointer-events", "none"); // to prevent mouseover/drag capture

        node.on("mouseover", focus).on("mouseout", unfocus);

        function ticked() {

            node.call(updateNode);
            link.call(updateLink);

            labelLayout.alphaTarget(0.3).restart();
            labelNode.each(function (d, i) {
                if (i % 2 == 0) {
                    d.x = d.node.x;
                    d.y = d.node.y;
                } else {
                    var b = this.getBBox();

                    var diffX = d.x - d.node.x;
                    var diffY = d.y - d.node.y;

                    var dist = Math.sqrt(diffX * diffX + diffY * diffY);

                    var shiftX = b.width * (diffX - dist) / (dist * 2);
                    shiftX = Math.max(-b.width, Math.min(0, shiftX));
                    var shiftY = 16;
                    this.setAttribute("transform", "translate(" + shiftX + "," + shiftY + ")");
                }
            });
            labelNode.call(updateNode);

        }





        // zoom = d3v5.zoom()
        //     .scaleExtent([1, 4])
        //    .on("zoom", function () { container.attr("transform", d3v5.event.transform); });


        // zoom reset button
        /*
        d3.select("button#reset_zoom")
            .on("click", function () {
                view.model.relations.zoom_transition = true;
                zoom.translate([0, 0])
                    .scale(1)
                    .event(svg);
            });
            */

        //zoom(svg);

        function fixna(x) {
            if (isFinite(x)) return x;
            return 0;
        }

        function focus(d) {
            var index = d3v5.select(d3v5.event.target).datum().index;
            node.style("opacity", function (o) {
                return neigh(index, o.index) ? 1 : 0.1;
            });
            labelNode.attr("display", function (o) {
                return neigh(index, o.node.index) ? "block" : "none";
            });
            link.style("opacity", function (o) {
                return o.source.index == index || o.target.index == index ? 1 : 0.1;
            });
        }

        function unfocus() {
            labelNode.attr("display", "block");
            node.style("opacity", 1);
            link.style("opacity", 1);
        }

        function updateLink(link) {
            link.attr("x1", function (d) { return fixna(d.source.x); })
                .attr("y1", function (d) { return fixna(d.source.y); })
                .attr("x2", function (d) { return fixna(d.target.x); })
                .attr("y2", function (d) { return fixna(d.target.y); });
        }

        function updateNode(node) {
            node.attr("transform", function (d) {
                return "translate(" + fixna(d.x) + "," + fixna(d.y) + ")";
            });
        }

        function dragstarted(d) {
            d3v5.event.sourceEvent.stopPropagation();
            if (!d3v5.event.active) graphLayout.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(d) {
            d.fx = d3v5.event.x;
            d.fy = d3v5.event.y;
        }

        function dragended(d) {
            if (!d3v5.event.active) graphLayout.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

    }

    return true;

    // // // // 

}