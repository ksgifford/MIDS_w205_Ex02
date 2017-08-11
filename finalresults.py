import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) < 2:
    cur.execute("SELECT * FROM tweetwordcount ORDER BY word")
    records = cur.fetchall()
    for rec in records:
        print rec[0], " ", rec[1], '\n'
elif len(sys.argv) == 2:
    word = sys.argv[1]
    cur.execute("SELECT count FROM tweetwordcount WHERE word=%s", (word,))
    wrd_count = cur.fetchall()
    try:
        print 'Total number of occurences of "', word, '": ', wrd_count[0][0]
    except IndexError:
        print "I'm sorry, that word wasn't found."
else:
    print 'Too many arguments! Please enter a single word.'
