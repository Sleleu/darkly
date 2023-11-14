
=======
### Challenge

While enumerating the different pages of the site, I saw an available page named redirect, used here to redirect users to the site's social media pages.
For example:

```
index.php?page=redirect&site=twitter
```
Seeing the possible redirections from social networks, I tried to use the redirect from another site:

```
http://192.168.56.107/?page=redirect&site=another_website
```

This led me to a page where I was able to find the flag:

```
GOOD JOB HERE IS THE FLAG : B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3
```

### Vulnerability
This vulnerability is used by attackers to succeed in phishing attacks thanks to a company's reputation.
If a legitimate site is vulnerable to an open redirect, the attacker can send a victim a link with the DNS of a legitimate site, but which eventually redirects to a malicious site.
For example, a clone of the vulnerable site could be used to gather sensitive data.

![Open-redirection-scheme-1](https://github.com/Sleleu/darkly/assets/93100775/e96bd81f-c9ab-41b8-a3c4-81339fb7f448)
> Source : [Guardia school](https://guardia.school/boite-a-outils/focus-sur-la-vulnerabilite-de-open-redirect.html)

### How to prevent open redirect 
- Just don't use redirect ? 🙂
- Don't allow the URL as user input for the destination
- Create a whitelist of trusted URLs
- Force all redirects to first through a page notifying users that they are going off of your site

### Ressources

- https://learn.snyk.io/lesson/open-redirect/
- https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
- https://guardia.school/boite-a-outils/focus-sur-la-vulnerabilite-de-open-redirect.html
