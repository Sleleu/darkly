=======
### Challenge

I go to the `survey` page URL, then inspect the page. In the 'inspect' tab, I navigate to 'Sources' and source code. We can see this kind of balise :
```
<option value="1">1</option>
```
If we try to modify the value with a big number, and select the option modified, this function is called : `javascript:this.form.submit();`

It seems that the backend has not implemented any form of input validation because we obtained the flag simply with this action :

```
THE FLAG IS 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA
```

=======


### Vulnerability
This challenge invites us to focus on input validation issues.
The risk here is that an external person can modify the source code with any value they want, potentially causing the script to malfunction. This creates a vulnerability that can be exploited.

### How to implementing input validation

- Data from all potentially untrusted sources should be subject to input validation, including not only Internet-facing web clients but also backend feeds over extranets
- Create when it's possible an allow list validation for all input fields provided by the user.
- Properly sanitize output data to prevent XSS attacks for example.

### Resources

- https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- https://owasp.org/www-project-mobile-top-10/2023-risks/m4-insufficient-input-output-validation
