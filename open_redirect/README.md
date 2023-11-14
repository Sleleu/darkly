Vous avez identifié une vulnérabilité de type open redirect sur la page d'accueil du site. En naviguant, vous avez observé que les URL changent lorsqu'on clique sur les images, devenant '?page=redirect&src='. Cela indique qu'on peut ajouter des valeurs à la suite. En testant, vous avez remarqué que vous pouviez afficher le site lui-même en utilisant '../../..'. Vous avez ensuite ajouté 'code/html;' comme préfixe et inclus votre script <script> alert(1)</script>. Cependant, certains caractères n'étaient pas reconnus, alors vous avez ajouté 'base64,' et traduit votre commande en base64.

```
code/html;base64,
```

Vulnérabilité :
There is a risk of phishing through a malicious URL redirection. It could be used for concealing brute force attacks on other sites. It might also be used to bypass security controls or potentially alter the URL.
