import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) < 3:
    print "Not enough arguments. Please specify an upper and lower bound.""
elif len(sys.argv) == 3:
    low = sys.argv[1].split(',')[0]
    high = sys.argv[2].split(',')[0]
    cur.execute("SELECT * FROM tweetwordcount WHERE count >= %s AND count <= %s ORDER BY count DESC", (low,high))
    wrd_list = cur.fetchall()
    for wrd in wrd_list:
        print wrd[0], ':', wrd[1]
else:
    print "Too many arguments! Please enter an upper and lower bound.""
