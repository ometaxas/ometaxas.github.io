# A simple topic-model browser for SciXplore (focusing on [Covid-19 Open Research Corpus Analysis](https://www.semanticscholar.org/cord19/download) )

Our goal in this demo is to analyze [COVID-19 Open Research Dataset](https://pages.semanticscholar.org/coronavirus-research) in order to:

- Demonstrate related domain specific analysis capability of SciXplore
- Identify intepretable topics (described by WIKIPedia concepts, MeSH, words & texts)
- Identify and annotate publication with WikiPedia or MeSH related concepts
- Analyze related topic trends 
- Analyze similarity among topics, among publications or other entities
- Demonstrate topic & concept based exploration & information retrieval capabilities

The analysis has been based on [SciXplore](https://github.com/atypon/MVTopicModel) multi-view topic modelling, representation learning and semantic annotation framework. SciXplore provides a lot of advantages on top of text only topic modeling alternatives (e.g., LDA) producing more interpetable, multi-view, topics as well as vector representations (embeddings) for all involving entities (including topics, words & concepts). Therefore, by combining multi-view topic modelling with skip-gram based topic2vec representation learning infers topics of better quality and facilitate similarity analysis & recommendation. SciXplore also provides a semantic annotation engine for DBPedia (Wiki) based annotation which extends the well-established [DBPedia Spotlight framework](https://www.dbpedia-spotlight.org/) 


The visualization has been based on [agoldst.github.io/dfr-browser](http://agoldst.github.io/dfr-browser), use [d3](http://d3js.org) and it relies entirely on static html and javascript files. We have created a python scipt which analyzes the results of SciXplore and exports required data files in a format which is compatible with dfrbrowser. To better support the requirements of SciXplore & Covid-19 dataset we have implemented several changes on top of the dfrbrowser such as:
- Change the way we are calculating trends and more specifically the normalization: topic activity per year is based on the ratio of the docs of a topic in a given year / total docs for a given topic (and total docs of all topics for a given year)  
- Change html / CSS in several places to handle longer 'word' descriptions (which correspond to concepts)
- Support autocompletion & multi-selection in word & concept search 
- Show a topic relations view (through a Force-Directed Layout) 


Our analysis has been based on the following steps:

- Consume and pre-process publications from COVID-19 Open Research Dataset 
- Enrich them (e.g., getting MeSH terms) utilizing [MEDLINE/PubMed dumps](https://www.nlm.nih.gov/databases/download/pubmed_medline.html)
- Annotate all docs with Wikipedia terms using SciXplore semantic annotation engine  
- Analyze text, metadata, MeSH & Wikipedia concepts with SciXplore inferring:
    - Intepretable multi-view topics 
    - Topics per document or other entities
    - Vector representations per topics or other entities 
    - Analyze trends & similarities 
    - Create a WEB GUI for data exploration (adapting [agoldst.github.io/dfr-browser](http://agoldst.github.io/dfr-browser))
    - Give titles to the topics
    

There are several things that we can do on top (or that they aren't properly addressed through this visualization) especially in relation to search & recommendation, such as: 
- besides silimiarities among topics, identify and analyze similarities among concepts or documents
- content-based recommendation: given a publication, topic or concept recommend similar entities
- improvements on concept-based search (e.g., search using multiple topics or articles which are related to some concepts)
- merge corresponding WIKI & MeSH concepts (and provide links)
- journal or publisher specific analysis (e.g., search by journal or publisher)

For more information or feedback please contact Omiros Metaxas: ometaxas@atypon.com


