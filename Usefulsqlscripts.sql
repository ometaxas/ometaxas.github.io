--select * from  covid19doc
--where covid19doc.pmcid='PMC5452550'
select count(*) from covid19doc

delete from doc_dbpediaresource where docid in
select docid from covid19doc

select * from public.medcit_chemicallist_chemical 
where pmid in (
select pmid from (
select  medcit.pmid, covid19doc.docid, covid19doc.pubid, 
case when coalesce(art_journal_journalissue_pubdate_year,0)=0 THEN cast(pmcids.year as int) ELSE art_journal_journalissue_pubdate_year END as year, 
art_journal_issn, art_journal_title
, string_agg(medcit_art_abstract_abstracttext.value,' '::text order by medcit_art_abstract_abstracttext_order) as abstract 
from  covid19doc
join public.pmcids on pmcids.pmcid = covid19doc.pmcid 
--and covid19doc.pmcid='PMC5452550'
left join public.medcit_art_abstract_abstracttext on medcit_art_abstract_abstracttext.pmid = cast(pmcids.pmid as int) 
and medcit_art_abstract_abstracttext.pmid_version=1
join medcit on  medcit.pmid = cast(pmcids.pmid as int)  and medcit.pmid_version=1
group by  medcit.pmid,
covid19doc.docid, covid19doc.pubid, art_journal_journalissue_pubdate_year, art_journal_issn, art_journal_title, pmcids.year
union
select  medcit.pmid, covid19doc.docid, covid19doc.pubid, 
case when coalesce(art_journal_journalissue_pubdate_year,0)=0 THEN cast(pmcids.year as int) ELSE art_journal_journalissue_pubdate_year END as year, 
art_journal_issn, art_journal_title
, string_agg(medcit_art_abstract_abstracttext.value,' '::text order by medcit_art_abstract_abstracttext_order) as abstract
from  covid19doc
join medcit on  medcit.pmid = cast(covid19doc.pmid as int) and medcit.pmid_version=1  
--and covid19doc.pmcid='PMC5452550'
left join public.pmcids on pmcids.pmid = covid19doc.pmid 
left join public.medcit_art_abstract_abstracttext on medcit_art_abstract_abstracttext.pmid = cast(covid19doc.pmid as int) 
	and medcit_art_abstract_abstracttext.pmid_version=1
group by medcit.pmid,
covid19doc.docid, covid19doc.pubid, art_journal_journalissue_pubdate_year, art_journal_issn, art_journal_title, pmcids.year
	)a
	)


select * from
public.medcit_chemicallist_chemical 
join 
where nameofsubstance like '%hloroquine%'


public.medcit_supplmeshlist_supplmeshname where value like '%hloroquine%'


select Resource from doc_dbpediaResource 
group by resource 
having count(*)>30	EXCEPT select URI from DBpediaResource


update doc_dbpediaresource  
set resource = 'http://dbpedia.org/resource/Coronavirus_HKU15'

select * from doc_dbpediaresource
where 
resource like '%Dromedary%' and 
docid in
(select docid from covid19doc)

update topicanalysis 
set item = 'http://dbpedia.org/resource/Coronavirus_HKU15'
where 
item = 'https://en.wikipedia.org/wiki/Coronavirus_HKU15' and 
experimentid like 'Covid%'
--docid in
--(select docid from covid19doc)

INSERT INTO public.doc_dbpediaresource(
	docid, resource, support, count, similarity, mention, confidence, annotator, resourcecount)
	
	select docid, 'https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2', ;
	
	select * from doc_dbpediaresource 
	where resource like Sars


select * from 
(
select topicid,  replace(string_agg(concept, ','::text),' ','_') as concepts, string_agg(weightedcounts::text, ','::text)
                 from topicanalysis_view_covid19 				 
				 group by topicid
	)a
	where concepts like '%chloroquine%'
				 
select distinct docid from doc_dbpediaresource where docid in
(select docid from covid19doc)

select  docfullinfo_view.docid, text,  fos, venue, DBPediaResources 
from docfullinfo_view 
  LEFT JOIN doc_dbpediaresource ON docfullinfo_view.docid = doc_dbpediaresource.docid  
  where doc_dbpediaresource.docid is null AND COALESCE(text, ''::text)<>'' and repository='covid19' 
  
  select * from document 
  join covid19doc on covid19doc.docid = document.docid
  where length(document.abstract) > length(covid19doc.abstract)
  
  select * 
  --from doc_fos 
  from doc_dbpediaresource
  where docid='cvd40551'
  
  s
  
  select * from docfullinfo_view 
  where repository='covid19' 
  --and docid='cvd40551'
  and lower(text) like '%covid-19%'
  
  select * from doc_dbpediaresource
  where resource = 'http://dbpedia.org/resource/SARS_coronavirus'
  
  select * from docfullinfo_view
  where docid in ('cvd11571','cvd14294','cvd5715')
  
  select distinct doc_dbpediaresource.docid from 
  doc_dbpediaresource
  join docfullinfo_view on docfullinfo_view.docid = doc_dbpediaresource.docid
  where resource = 'http://dbpedia.org/resource/SARS_coronavirus'
   and lower(text) like '%sars-cov-2%'
  
  update doc_dbpediaresource 
  set resource = 'http://dbpedia.org/resource/Severe_acute_respiratory_syndrome_coronavirus_2'
  where resource = 'http://dbpedia.org/resource/SARS_coronavirus'
  and docid in 
  ( select distinct doc_dbpediaresource.docid from 
  doc_dbpediaresource
  join docfullinfo_view on docfullinfo_view.docid = doc_dbpediaresource.docid
  where resource = 'http://dbpedia.org/resource/SARS_coronavirus'
   and lower(text) like '%sars-cov-2%')
   
  insert into doc_doc_dbpediaresource
  
  select * from doc_topic
  where experimentid = 'Covid_50T_550IT_3000CHRs_4M_WVNoNet'
  and docid = 'cvd27241'
  order by docid, topicid
  limit 100
  
  INSERT INTO public.doc_dbpediaresource(
	docid, resource, support, count, similarity, mention, confidence, annotator, resourcecount)
	
	select docid, 'https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2', ;
	
	select * from doc_dbpediaresource 
	where resource like Sars
	