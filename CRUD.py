import MySQLdb

# Creates connection with DB
def create_connection():
     cnx = MySQLdb.connect(host = "localhost", user = "root", passwd = "Team5", db = "testDB")
     cur = cnx.cursor()
     return cur


def get_user(connection, user_name):
    cur = create_connection()
    cur.execute("SELECT * FROM user WHERE username = %s", user_name)
    user_name =  cur.fetchall()
    return user_name
