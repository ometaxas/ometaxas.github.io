/*global view, VIS, set_view, bib, utils, d3 */
"use strict";

view.doc = function (p) {
    var div = d3.select("div#doc_view"),
        total_tokens = p.total_tokens,
        topics = p.topics,
        trs, trs_enter;

    d3.select("#doc_view_main").classed("hidden", false);

    div.select("h2#doc_header")
        .html(p.citation);

    div.select("#doc_remark .token_count")
        .text(p.total_tokens);

    div.select("#doc_remark a.url")
        .attr("href", p.url);

    trs = div.select("table#doc_topics tbody")
        .selectAll("tr")
        .data(topics.map(function (d, j) {
            return {
                topic: d.topic,
                weight: d.weight,
                label: p.labels[j],
                words: p.words[j]
            };
        }));

    trs_enter = trs.enter().append("tr");
    trs.exit().remove();

    trs.on("click", function (t) {
        view.dfb().set_view(view.topic.hash(t.topic));
    });

    trs_enter.append("td").append("a")
        .classed("topic_name", true)
        .append("span")
            .classed("name", true);

    trs.select("a.topic_name")
        .attr("href", function (t) {
            return view.topic.link(t.topic);
        })
        .select("span.name")
            .text(function (t) { return t.label; });

    trs_enter.append("td").append("a")
        .classed("topic_words", true)
        .append("span")
            .classed("words", true);
    trs.select("a.topic_words")
        .attr("href", function (t) {
            return view.topic.link(t.topic);
        })
        .select("span.words") 
            .text(function (t) {
                return t.words.reduce(function (acc, x) {
                    return acc + " " + x.word;
                }, "");
            });

    view.weight_tds({
        sel: trs,
        enter: trs_enter,
        w: function (t) { return t.weight / total_tokens; },
        frac: function (t) {
            return VIS.percent_format(t.weight / total_tokens);
        },
        raw: function (t) { return t.weight; } 
    });
};

