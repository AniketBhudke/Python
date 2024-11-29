import oracledb as orc
def droptable():
    try:
        conn=orc.connect("ANIKET/1234@localhost/orcl")
        cur=conn.cursor()
        aqc="drop table A"
        cur.execute(aqc)
        print("Table Drop Successfully--Verify")
    except orc.DatabaseError as db:
        print("Problem Ocuur in Datbase",db)

droptable()
