import re
import requests

emails = []
links = []
url = "http://www.mosigra.ru/"
links.append(url)
j = 0
while j < 10:     
    url_new = str(links[j])
    r = requests.get(url_new)
    email = re.findall(r'[a-zA-Z0-9][-_\w]+[.\w+]*\@[a-zA-Z0-9][-_a-z0-9]{0,61}[a-z0-9]\.[a-z]{1,6}', str(r.content))
    for x in email:
        if x not in emails:
            emails.append(x)
    http = re.finditer(r'(<a href=")(http\:\/\/[-+\w.\/$#%]+)(\")', str(r.content))
    for x in http:
        if x.group(2).startswith(url):
            if x in links:
                pass
            else:
                links.append(x.group(2))
    incomplete = re.finditer(r'(<a href=")(\/[-+\w:\/#@$.]*)(\")', str(r.content))
    for x in incomplete:
        url_new = url + x.group(2)
        if url_new in links:
            pass
        else:
            links.append(url_new)
    j = j+1
for x in emails:
    print(x)


