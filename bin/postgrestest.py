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
        
        
        query = (""" select topicid,  string_agg(concept, ','::text), string_agg(weightedcounts::text, ','::text)
                 from topicanalysis_view_covid19 group by topicid  """).format(experimentid)

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
        
        
        query = ("""select topicid, pubid, weight 
from doc_topic 
join covid19doc on doc_topic.docid = covid19doc.docid
where experimentid = '{}'
order by topicid """).format(experimentid)

        cur.execute(query)

        print("The number of topics per doc: ", cur.rowcount)
        rows = cur.fetchall()
        curtopic = rows[0][0]
 
        for row in rows:            
            if row[0] != curtopic:
                curtopic = row[0]
                p.append(p_cur)
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


if __name__=="__main__":
    import sys
    experimentid = 'Covid_40T_550IT_3000CHRs_3M_WVNoNet'
    #export_tw(experimentid)
    export_dt(experimentid)

