import os
import requests
import re

base = 'http://sunlight.iis.sinica.edu.tw'
first = '/cgi-bin/text.cgi'
second = '/uwextract/show.php?type=tag&id='

def parseTerm(tag):
    split=tag.split('(')
    return {'term': split[0], 'tag': split[1][:-1]}

def getID(query):
    r = requests.post(base + first, data={'query': query.encode('big5')})
    regex = re.search('\d+', r.text.split('URL=')[1])
    return regex.group(0)

def getTags(id):
    r = requests.get(base + second + id)
    r.encoding = 'Big5'
    regex = re.search('<pre>((.|\n)*?)<\/pre>', r.text)
    result = regex.group(1)

    pattern = re.compile('[^\s!-]+')
    tags = pattern.findall(result)
    return map(parseTerm, tags)

def parse(query):
    id = getID(query)
    tags = getTags(id)
    return tags
