from bs4 import BeautifulSoup

f = open ("sjs.html", "r")
html_text = f.read()
f.close()


soup = BeautifulSoup(html_text, 'html.parser')
for div in soup.find_all('div', class_=['sbinfo', 'sbdetailsdate']):
    if div['class'][0] == 'sbinfo': event = div.get_text()
    else: print (event + ',"' + div.get_text().strip() + '"')
    
