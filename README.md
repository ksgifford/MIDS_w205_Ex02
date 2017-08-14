W205 Exercise 2
Kevin Gifford - Summer 2017

Twitter Application Instructions
--------------------------------------------------------------------------------
1.  Launch an EC2 instance based on the UCB MIDS W205 EX2-FULL AMI. Install the
    necessary Python libraries:
    
    pip install psycopg2==2.6.2
    
    pip install tweepy

2.  Mount a working EBS volume with Postgres installed as /data.


3.  Start the Postgres server.


4.  Change to user "w205":

    su - w205

5.  Clone the repository into /home/w205.


6.  From /home/w205 run the following:

    cd MIDS_w205_Ex02/
    
    python create_db.py

7.  Log into Postgres to confirm creation of the postgres database:

    psql --username=postgres
    
    \connect tcount \dt

8.  You should see a table named "tweetwordcount." Exit Postgres.


9.  From MIDS_w205_Ex02/, copy credentials_template.py to
    /home/w205/MIDS_w205_Ex02/extweetwordcount/src/spouts as tweet_cred.py
    IMPORTANT - Renaming the file is essential, both for proper application operation,
    and for security of your Twitter credentials (see next step).
    

10. Edit tweet_cred.py, inserting your Twitter credential information in the
    indicated locations, and save.
    

11. Navigate to /home/w205/MIDS_w205_Ex02/extweetwordcount/ and launch the application:

    sparse run
    

12. After collecting the amount of Twitter data you desire, exit the application (Ctrl-C).


13. From /home/w205/MIDS_w205_Ex02/, you can run finalresults.py and histogram.py
    to query the tcount database and learn about the Twitter data you collected.
