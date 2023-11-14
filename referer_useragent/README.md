### Challenge

Well, there wasn't anything interesting on this page except when analyzing the source code, which gives us the following hints:

```jsx
<!--
You must come from: "https://www.nsa.gov/".
-->

...
...

Let's use this browser: "ft_bornToSec". It will help you a lot.
```

It's quickly apparent that it's talking about the referrer and the user-agent. So, I decided to try a little curl request, specifying the following:

```
curl --referer 'https://www.nsa.gov/' --user-agent 'ft_bornToSec' http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

And voilà! By analyzing the page's source code, we found this:

```
The flag is: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

### Vulnerability

It's possible to retrieve sensitive information from a user's referrer (such as password reset tokens).
And regarding the user_agent, it's possible to input some code to exploit vulnerabilities of a website if the content isn't correctly parsed


### How to prevent from this vulnerability

For the referer, you can simply use the tag strict-origin-when-cross-origin for the referrer policy, which indicates that when the user goes to another domain,
only the domain will be included in the referrer, otherwise, the complete URL if it's the same site.
For the useragent and the rest of the content that can be used by the user to exploit some bugs, a sanitization of the inputs are required.

### Resources
- https://truesparrow.com/blog/cross-domain-referer-vulnerability/
- https://medium.com/perimeterx/user-agent-based-attacks-are-a-low-key-risk-that-shouldnt-be-overlooked-1a5d487a1aa0
