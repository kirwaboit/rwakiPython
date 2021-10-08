# Databases


- Great resources :-
- https://phoenixnap.com/kb/sql-vs-nosql 
- https://phoenixnap.com/kb/acid-vs-base 

## ACID Vs BASE
ACID stands for :-  

1. Atomic – Each transaction is either properly carried out or the process halts and the database reverts back to the state before the transaction started. This ensures that all data in the database is valid.  
2. Consistent – A processed transaction will never endanger the structural integrity of the database.  
3.  Isolated – Transactions cannot compromise the integrity of other transactions by interacting with them while they are still in progress.  
4. Durable – The data related to the completed transaction will persist even in the cases of network or power outages. If a transaction fails, it will not impact the manipulated data.  


- The ACID model provides a consistent system.
    - Financial institutions will almost exclusively use ACID databases. Money transfers depend on the atomic nature of ACID.  
    An interrupted transaction which is not immediately removed from the database can cause a lot of issues. Money could be debited from one account and, due to an error, never credited to another. 
    - Examples of ACID database management systems :Relational database management systems in general e.g MySQL, PostgreSQL, Oracle, SQLite, and Microsoft SQL Server.  
- The BASE model provides high availability.  
    - Marketing and customer service companies who deal with sentiment analysis will prefer the elasticity of BASE when conducting their social network research. Social network feeds are not well structured but contain huge amounts of data which a BASE-modeled database can easily store.
    - Examples of BASE database management systems NoSQL databases tend to conform to BASE principles e.g MongoDB, Cassandra and Redis

ACID stands for:  


# Postgress   




<div style="width:50%">![Chilling](/https://www.w3schools.com/w3images/fjords.jpg)</div>  

![a-kitten.jpg](/Databases\postgresElephantLogo.png =200x200)

![postgresElephantLogo](/Databases\images\postgresElephantLogo.png)


Linked logo: ![alt text](/wordpress-logo-32.png)
(http://wordpress.com/ "WordPress Website")



- Pro: Rich SQL. PostgreSQL is old (first release in 1995) and its motto is “The World's Most Advanced Open Source Relational Database”. ...
- Pro: Query Parallelism. ...
- Pro: Partitioning. ...
- Pro: Strong adoption. ...
- Cons : No compression. ...
- Cons: No columnar tables. ...
- Cons: No machine learning included. 

## Postgress use cases:

## Which is better MongoDB or Postgres?

Both databases are awesome. If you are looking for a distributed database for modern transactional and analytical applications that are working with rapidly changing, multi-structured data, then MongoDB is the way to go. If a SQL database fits your needs, then Postgres is a great choice.