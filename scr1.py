# pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org requests
import json
from bs4 import BeautifulSoup
import os
import requests
direc=os.getcwd()+'/download/'
print(direc)
search=input("enter the word: ")
search=search.replace(" ","+")

link="https://www.google.co.in/search?hl=en&tbm=isch&sxsrf=ACYBGNQn883odsmNh8foGw8UyZTjiXwzfA%3A1576219216710&source=hp&biw=1366&bih=625&ei=UDLzXaK6KYCP4-EPgLKcgAY&q="+search+"&oq=flo&gs_l=img.3.0.35i39j0l9.6944.7358..9049...1.0..0.445.836.0j1j1j0j1......0....1..gws-wiz-img.nQXPGcdHCLE&safe=active"
print(link)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    }

source=requests.get(link, headers=headers,verify=False).text
soup=BeautifulSoup(source,"html.parser")
mydivs = soup.findAll("div", {"class": "rg_meta notranslate"})
mydivs= mydivs[0: min(10,len(mydivs))]

if(os.path.exists(direc+search+'/')==False):
    os.makedirs(direc+search+'/')

for x in mydivs:
    url=(json.loads(x.text)["ou"])
    path=direc+search+'/'+url.split('/')[-1]
    print(url)
    print(path)
    print('----------------------------------')
    r = requests.get(url, allow_redirects=True)
    open(path, 'wb').write(r.content)

