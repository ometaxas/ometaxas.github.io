select doi, title, authors, journal, publishername, docid, to_char(to_date(pubyear||'01'||'01', 'YYYYMMDD'), 'YYYY-MM-DD"T"HH24:MI:SS"Z"'), concepts
from (
SELECT row_number() OVER (ORDER BY document.docid) - 1 AS id,
    document.docid,
    document.doi,
    document.title,
    covid19_doc.authors,
    document.journalname AS journal,
    ''::text AS issn,
    document.publishername,
    document.pubyear,
	concepts
   FROM document
   JOIN covid19_doc ON document.docid = covid19_doc.mag_id::text
   join public.doc_concept_view ON document.docid =  doc_concept_view.docid
  WHERE COALESCE(document.pubyear, ''::text) <> ''::text AND document.pubyear <> 'NULL'::text AND COALESCE(document.abstract, ''::text) <> ''::text
  ORDER BY document.docid
	) a