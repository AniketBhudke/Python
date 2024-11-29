#adding the column in table
import oracledb as orc
def altertableadd():
    try:
        conn=orc.connect("ANIKET/1234@localhost/orcl")
        cur=conn.cursor()
        Aqa="alter table AA add(s_dneame varchar2(10),ss varchar2(10))";
        # aqa="alter table KVR add(compname varchar2(10))"
        cur.execute(Aqa)
        print("Table Alter Successfully--Verify")
    except orc.DatabaseError as db:
        print("Problem Ocuur in Datbase",db)

altertableadd()


#modify the table
# import oracledb as orc
# def altertableadd():
#     try:
#         conn=orc.connect("ANIKET/1234@localhost/orcl")
#         cur=conn.cursor()
#         aqc="alter table ABC modify(CNO number(20,3))"
#         # aqa="alter table KVR add(compname varchar2(10))"
#         cur.execute(aqc)
#         print("Table Alter Successfully--Verify")
#     except orc.DatabaseError as db:
#         print("Problem Ocuur in Datbase",db)

# altertableadd()
