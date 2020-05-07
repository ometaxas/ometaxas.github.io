import psycopg2
import json
import zipfile as zf

def write_tw(alpha, tw, out):
    twj = {
        "alpha": alpha,
        "tw": tw
    }
    with open(out, "w") as f:
        json.dump(twj, f)

    print("Wrote topic-words information to " + f.name)

def transform_topic_weights(weights, words, n):    
    return({
        "words": words[:n],            
        "weights": weights[:n]
        })

def export_tw(experimentid):
    """ query data from the vendors table """
    connection = None
    
    try:
        
        alpha = []

        connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "DBLP")
        cur = connection.cursor()
        
        
        query = ("""select topicid, title, weight 
        from topic 
        inner join topicdetails on topic.id = topicdetails.topicid
        where topic.experimentid = '{}' and visibilityindex>0  and itemtype=0 and topic.experimentid = topicdetails.experimentid
        order by topicid """).format(experimentid)

        cur.execute(query)

        print("The number of topics: ", cur.rowcount)
        rows = cur.fetchall()
 
        for row in rows:
            alpha.append(float(row[2]))
            print(row[2])

        print(alpha)    
 
        cur.close()

        tw = []
        cur = connection.cursor()
        
        
        query = ("""select topicid,  replace(string_agg(concept, ','::text),' ','_') as concepts, string_agg(weightedcounts::text, ','::text)
                 from topicanalysis_view_covid19 where experimentid = '{}' group by topicid  """).format(experimentid)

        cur.execute(query)

        print("The number of tokens: ", cur.rowcount)
        rows = cur.fetchall()

        n=50
 
        for row in rows:
            words = [(x) for x in row[1].split(",")]
            weights = [int(x) for x in row[2].split(",")]
            #tw.append(transform_topic_weights(weights, words, n))
            tw.append({
            "words": words[:n],            
            "weights": weights[:n]
            })            
            

        print(tw)    
 
        cur.close()

        out = "tw.json"
        write_tw(alpha, tw, out)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")



def write_dt(dtj, out):
    with zf.ZipFile(out, "w", compression=zf.ZIP_DEFLATED) as z:
        z.writestr("dt.json", json.dumps(dtj))

    print("Wrote sparse doc-topics to " + out)


def export_dt(experimentid):
    """ query data from the vendors table """
    connection = None
    
    try:
        
        p = [0]
        i = []
        x = []
        p_cur = 0

        connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "DBLP")
        cur = connection.cursor()
        
        
        query = ("""select distinct topicid, id, round(1000 * weight) as weight 
from doc_topic 
join covid19doc_view on doc_topic.docid = covid19doc_view.docid
where experimentid = '{}' 
order by topicid, id """).format(experimentid)

        cur.execute(query)

        print("The number of topics per doc: ", cur.rowcount)
        rows = cur.fetchall()
        curtopic = rows[0][0]
 
        for row in rows:            
            if row[0] != curtopic:
                curtopic = row[0]
                p.append(p_cur)
                print(curtopic)
            i.append(int(row[1]))
            x.append(float(row[2]))
            p_cur += 1
            
        p.append(p_cur)

        dt = { "i": i, "p": p, "x": x }

        #print(dt)    
 
        cur.close()       

        out = "dt.json.zip"
        write_dt(dt, out)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")

def write_tsgraph(nodes, links, out):
    tsj = {
        "links": links,
        "nodes": nodes
    }
    with open(out, "w") as f:
        json.dump(tsj, f)

    print("Wrote topic similarity graph information to " + f.name)
    
def export_topicsilimarity(experimentid):
    """ query data from the vendors table """
    connection = None
    
    try:
        
        
        links = []
        

        connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "DBLP")
        cur = connection.cursor()
        
        
        query = ("""select topicid1, topicid2, similarity
FROM topicsimilarity 
WHERE experimentid1 = '{}' and similarity >= 0.3   order by topicid1, topicid2""").format(experimentid)

        cur.execute(query)

        print("The number of similar topic pairs: ", cur.rowcount)
        rows = cur.fetchall()
        
 
        for row in rows:  
             links.append({
            "source": row[0],            
            "target": row[1],
            "value": float(row[2])
            })

            
        print(links)    
 
        cur.close()   
        
        nodes = []

        cur = connection.cursor()
                
        query = ("""select topicid, title, weight 
        from topic 
        inner join topicdetails on topic.id = topicdetails.topicid
        where topic.experimentid = '{}' and visibilityindex>0  and itemtype=0 and topic.experimentid = topicdetails.experimentid
        order by topicid """).format(experimentid)

        cur.execute(query)

        print("The number of topics: ", cur.rowcount)
        rows = cur.fetchall()
 
        #{"size": 60, "score": 0, "id": "Androsynth", "type": "circle"},
        for row in rows:
            nodes.append({
            "size": int(700*row[2]),            
            "title": row[1],
            "score":1,
            "id": row[0],
            "group": 1
            })
            
            
        print(nodes)    
 
        cur.close()


        out = "graph.json"
        write_tsgraph(nodes,links,out) 
        

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__=="__main__":
    import sys
    experimentid = 'Covid_55T_600IT_3000CHRs_3M_WVNoNet'
    #export_tw(experimentid)
    #export_dt(experimentid)
    export_topicsilimarity(experimentid)

