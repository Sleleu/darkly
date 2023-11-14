### Challenge

In the robots.txt file, we once again find a tree of links with a depth level of at least 3. It would be too time-consuming to visit all of them because, considering there are 25 files, then 25 more, and another 25 before reaching the README, we have 15625 files to examine.

With this script that recursively traverses the entire tree structure, we can discover a leaf README that may not have the same content as the 34 characters we find:

```python
#!/bin/python3

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def is_file_empty(url):
    req = requests.get(url)
    return len(req.content) == 0

def list_files_in_directory(url, current_path=''):
    req = requests.get(url)
    page = BeautifulSoup(req.text, 'html.parser')
    for link in page.find_all('a'):
        href = link['href']
        if href == '../':
            continue
        if href.endswith('/'):
            new_url = urljoin(url, href)
            new_path = urljoin(current_path, href)
            list_files_in_directory(new_url, new_path)
        else:
            file_name = href
            file_info = link.next_sibling.strip().split()
            file_size = file_info[-1]
            file_url = urljoin(current_path, file_name)
            if file_size != "34":
                print(f"File found: {file_url}")

url = 'http://192.168.56.107/.hidden/'
list_files_in_directory(url)
```
=======
### Vulnerability

The /.hidden folder is often used to hide files in the file system but does not provide real security. There is a risk of unauthorized access and security vulnerabilities.

This folder was mentionned in the robots.txt. The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index.

The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents.

### How to prevent this vulnerability

- Do not rely on robots.txt to provide any kind of protection over unauthorized access
- Not assume that all web robots will honor the file's instructions
- Use the file .htaccess instead, an example to deny the access of a .hidden folder :
    ```
    <Directory ~ “\.hidden”>
    Order allow,deny
    Deny from all
    </Directory>
    ```
  Or for a file:
  ```
  <Files ~ “^\.htaccess”>
  Order allow,deny
  Deny from all
  </Files>
  ```

### Resources

- https://portswigger.net/kb/issues/00600600_robots-txt-file
- https://htaccessbook.com/protect-htaccess-files/
- https://filemanagerpro.io/article/how-to-deny-access-to-files-folders-through-htaccess-file/
