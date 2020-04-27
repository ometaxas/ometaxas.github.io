# A simple topic-model browser for SciTopic (focusing on [Covid-19 Open Research Corpus Analysis](https://www.semanticscholar.org/cord19/download) )

The visualization has been based on [agoldst.github.io/dfr-browser](http://agoldst.github.io/dfr-browser) and use [d3](http://d3js.org) to provide a way to browse some of a topic model of texts in a web browser, relying entirely on static html and javascript files. 

The analysis has been based on [SciTopic](https://github.com/atypon/MVTopicModel) multi-view topic modelling, representation learning and semantic annotation framework. 

SciTopic provides a lot of advantages on top of text only topic modeling alternatives (e.g., LDA) producing more interpetable, multi-view, topics as well as vector representations (embeddings) for all involving entities (including topics, words & concepts). Therefore, by combining multi-view topic modelling with skip-gram based topic2vec representation learning infers topics of better quality and facilitate similarity analysis & recommendation.

SciTopic also provides a semantic annotation engine for DBPedia (Wiki) based annotation which extends well-established [DBPedia Spotlight framework](https://www.dbpedia-spotlight.org/) 

We have analyzed [COVID-19 Open Research Dataset](https://pages.semanticscholar.org/coronavirus-research) with SciTopic in order to:

- Demonstrate related domain specific analysis capability of SciTopic
- Identify intepretable topics (described by WIKIPedia concepts, MeSH, words & texts)
- Identify and annotate publication with WikiPedia or MeSH related concepts
- Analyze related topic trends 
- Analyze similarity among topics, among publications or other entities
- Demonstrate topic & concept based exploration & information retrieval capabilities

Our analysis have been based on the following steps:

- Consume and pre-process publications from COVID-19 Open Research Dataset 
- Enrich them (e.g., getting MeSH terms) utilizing MEDLINE API / Dumps 
- Annotate all docs with Wikipedia terms using Scitopic semantic annotation engine  
- Analyze text, metadata, MeSH & Wikipedia concepts with Scitopic inferring:
- Intepretable multi-view topics 
- Topics per document or other entities
- Vector representations per topics or other entities 
- Analyze trends & similarities 
- Create / adapt an exploration Web GUI

