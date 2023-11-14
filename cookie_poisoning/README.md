When looking at the cookies, we find a cookie with the following values:

```
Name: I_am_admin
Value: 68934a3e9455fa72420237eb05902327
By using the decoder: https://www.dcode.fr/identification-chiffrement
```

We see that it's an MD5 hash. It was possible to reverse it directly with the site: https://md5.gromweb.com/, which gives us "false." Naturally, we can try to convert "true" to MD5, which gives: b326b5062b2f0e69046810717534cb09.

By placing this value in the cookie and refreshing the page, we come across the flag:

"Good job! Flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3"

Documentation: https://www.invicti.com/blog/web-security/understanding-cookie-poisoning-attacks/