import oracledb as orc 
def daleterecord():
    conn=orc.connect("ANIKET/1234@localhost/orcl")
    cur=conn.cursor()
    iq="delete STUDENT1 WHERE s_Roll_No = 4"
    cur.execute(iq)
    conn.commit()
    print("Deleted Successfully-verify")
daleterecord()    