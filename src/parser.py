import os
import requests
import re

base = 'http://sunlight.iis.sinica.edu.tw'
first = '/cgi-bin/text.cgi'
second = '/uwextract/show.php?type=tag&id='

def getID(query):
    r = requests.post(base + first, data={'query': query})
    regex = re.search('\d+', r.text.split('URL=')[1])

    return regex.group(0)

def getTag(id):
    r = requests.get(base + second + id)
    r.encoding = 'utf-8'
    return r.text
    # regex = re.search('<pre>((.|\n)*?)<\/pre>', r.text)
    # encoded = regex.group(1)
    # result = encoded.decode('big5')
    # return encoded
    # original_encoding = r.encoding
    # encoded = stripped.encode(r.encoding)
    # r.encoding = 'Big5-UAO'
    # r.encoding = 'Big5'
    # return result
    # pattern = re.compile('[^\s!-]+')
    # return pattern.findall(r.text)

def parse(query):
    id = getID(query)
    return getTag(id)
