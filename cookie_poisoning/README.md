### Challenge

When looking at the cookies, we find a cookie with the following values:

```
name : I_am_admin
value : 68934a3e9455fa72420237eb05902327
```

Using decode: https://www.dcode.fr/identification-chiffrement

We see that it’s an MD5 hash. It was possible to reverse it directly with the site: https://md5.gromweb.com/, which gives us `false`.
Naturally, we can try re-encoding `true` into MD5, which results in: b326b5062b2f0e69046810717534cb09.

By placing this value in the cookie and refreshing the page, we come across the flag:

```
Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

### Vulnerability

Cookie poisoning is a general term for various attacks that aim to manipulate or forge HTTP cookies. Depending on the targeted site or application,
attackers may be able to steal confidential user information, such as login credentials or personal information, or perform undesirable operations,
such as change password or delete account.

In the case of this challenge, it's more about session spoofing. This challenge teaches us that the presence
of a cookie is not sufficient to protect a session, as one can craft their own cookie when it's not adequately protected.

### How to prevent cookie poisoning

- Use unique and secure session cookie (not just a true value or a hash of data that can be guessed)
- Use a SHA256 algorithm at least instead, and secure librairies

### Ressources

- https://www.invicti.com/blog/web-security/understanding-cookie-poisoning-attacks/
- https://www.techtarget.com/searchsecurity/definition/cookie-poisoning
