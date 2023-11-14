
### Challenge

While writing anything as a value for `page=`, a JavaScript alert appears on the page indicating 'What?'. This is likely a clue that there is a path traversal vulnerability here.

As you continue to move up the directory structure, the alert changes until it stays on 'you can DO it', naturally suggesting that you've hit the root, so you probably need to specify a specific file. Trying with /etc/passwd, you eventually get an alert giving you the flag.

```bash
 http://192.168.56.107/index.php?page=../../../../../../../etc/passwd
```

And there you go, too easy:

```
Congratulations!! The flag is: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

### Vulnerability
A path traversal attack aims to access files and directories that are stored outside the web root folder. This can particularly happen due to misconfiguration of the server user's permissions. Generally, this concerns the 'www-data' user, but if a server is poorly configured (and has root privileges), it can allow access to sensitive files of the host system such as /etc/passwd or /etc/shadow

Sometimes, a **WAF (Web Application Firewall)** protect path traversal with a replace("../", "") but it's not a good pratice, you can escape this kind of
protection with `....//....//`, or with an url encoding `%2E%2E%2F` for example.


### How to prevent path traversal
- Update the web server and operating system, this vulnerability has been known for a while and it is likely tour web server's latest version is not vulnerable
- Do not rely on user input for any part of the path
- Run your web server from a separate disk from your system disk 

### Ressources
-  https://github.com/payloadbox/rfi-lfi-payload-list
-  https://www.synopsys.com/glossary/what-is-path-traversal.html
-  https://owasp.org/www-community/attacks/Path_Traversal
