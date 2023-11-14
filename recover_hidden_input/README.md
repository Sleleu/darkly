=======
### Challenge

Already having a password recovery page without specifying an email is suspicious, of course. In the page's source code, we can see the email address for password recovery in a `hidden input`. From there, you can either simply remove the hidden input to reveal the email input and modify it, or craft a POST request (With curl, insomnia, postman, etc...) by altering the email in the form data.

And here is the flag :
```
THE FLAG IS : 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0
```

=======
### Vulnerability

The risk here is that an individual could gain access to vulnerable data by simply changing the email value to a slightly different one.
Like the survey page, it's an input validation issues. The basic principle here is as follows: one should never trust the client. From this perspective, any data that must remain immutable should not be left in a form-data on the client-side.

### How to prevent from this vulnerability

- Simply don't use hidden input for a POST request like this....

### Resources

- https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- https://owasp.org/www-project-mobile-top-10/2023-risks/m4-insufficient-input-output-validation
