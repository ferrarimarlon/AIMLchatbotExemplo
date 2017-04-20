# -*- coding: latin-1 -*-

import urllib2
from bs4 import BeautifulSoup


def busca_fofocas():
    fof = "http://entretenimento.r7.com/famosos-e-tv/noticias"
    page = urllib2.urlopen(fof)
    soup = BeautifulSoup(page, "lxml", from_encoding="latin-1")
    f = soup.find_all('a', {'class': 'nwl-link'})
    fofocas = []
    for assunto in f:
        fofocas.append(assunto['title'])

    base_fofocas = open('fofocas.aiml', 'w+')
    base_fofocas.write('<?xml version="1.0" encoding="latin-1"?>\n'
                       '<aiml version="1.0">\n'
                       '<meta name="author" content="PyES"/>\n'
                       '<meta name="language" content="pt-br"/>\n')
    base_fofocas.write('<category>\n'
                       '<pattern>FOFOCA</pattern>\n'
                       '<template>\n'
                       '<random>\n')

    for x in fofocas:
        base_fofocas.write('<li>' + x.encode('utf-8') + '</li>\n')
    base_fofocas.write('</random>\n</template>\n</category>')
    base_fofocas.write('<category>\n'
                       '<pattern>* FOFOCA</pattern>\n'
                       '<template>\n'
                       '<srai>FOFOCA</srai>\n'
                       '</template>\n'
                       '</category>\n'
                       '<category>\n'
                       '<pattern>* FOFOCA *</pattern>\n'
                       '<template>\n'
                       '<srai>FOFOCA</srai>\n'
                       '</template>\n'
                       '</category>\n'
                       '<category>\n'
                       '<pattern>FOFOCA *</pattern>\n'
                       '<template>\n'
                       '<srai>FOFOCA</srai>\n'
                       '</template>\n'
                       '</category>\n')
    base_fofocas.write('</aiml>')

    base_fofocas.close()
