# A simple topic-model browser for SciTopic (focusing on [Covid-19 Open Research Corpus Analysis](https://www.semanticscholar.org/cord19/download) )

Our goal in this demo is to analyze [COVID-19 Open Research Dataset](https://pages.semanticscholar.org/coronavirus-research) in order to:

- Demonstrate related domain specific analysis capability of SciTopic
- Identify intepretable topics (described by WIKIPedia concepts, MeSH, words & texts)
- Identify and annotate publication with WikiPedia or MeSH related concepts
- Analyze related topic trends 
- Analyze similarity among topics, among publications or other entities
- Demonstrate topic & concept based exploration & information retrieval capabilities

The analysis has been based on [SciTopic](https://github.com/atypon/MVTopicModel) multi-view topic modelling, representation learning and semantic annotation framework. SciTopic provides a lot of advantages on top of text only topic modeling alternatives (e.g., LDA) producing more interpetable, multi-view, topics as well as vector representations (embeddings) for all involving entities (including topics, words & concepts). Therefore, by combining multi-view topic modelling with skip-gram based topic2vec representation learning infers topics of better quality and facilitate similarity analysis & recommendation. SciTopic also provides a semantic annotation engine for DBPedia (Wiki) based annotation which extends well-established [DBPedia Spotlight framework](https://www.dbpedia-spotlight.org/) 


The visualization has been based on [agoldst.github.io/dfr-browser](http://agoldst.github.io/dfr-browser), use [d3](http://d3js.org) and it relies entirely on static html and javascript files. We have created a python scipt which analyzes the results of SciTopic and exports required data files in a format which is compatible with dfrbrowser. To better support the requirements of Scitopic & Covid-19 dataset we have implemented several changes on top of the dfrbrowser such as:
- Change the way we are calculating trends and more specifically the normalization: topic activity per year is based on the ratio of the docs of a topic in a given year / total docs for a given topic (and total docs of all topics for a given year)  
- Change html / CSS in several places to handle longer 'word' descriptions (which correspond to concepts)


Our analysis has been based on the following steps:

- Consume and pre-process publications from COVID-19 Open Research Dataset 
- Enrich them (e.g., getting MeSH terms) utilizing [MEDLINE/PubMed dumps](https://www.nlm.nih.gov/databases/download/pubmed_medline.html)
- Annotate all docs with Wikipedia terms using Scitopic semantic annotation engine  
- Analyze text, metadata, MeSH & Wikipedia concepts with Scitopic inferring:
    - Intepretable multi-view topics 
    - Topics per document or other entities
    - Vector representations per topics or other entities 
    - Analyze trends & similarities 
    - Create / adapt an exploration Web GUI

There are several things that we can do on top (or that they aren't properly addressed through this visualization) especially in relation to search & recommendation, such as: 
- identify and analyze similarities among topics, concepts or documents
- given a publication, topic or concept recommend similar entities
- provide concept-based search (e.g., identifying topics or articles which are related to some concepts)
- merge corresponding WIKI & MeSH concepts (and provide links)
- journal or publisher specific analysis (e.g., search by journal or publisher)


