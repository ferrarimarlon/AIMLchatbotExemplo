# -*- coding: latin-1 -*-

import urllib2
from bs4 import BeautifulSoup


def busca_concursos():
    fof = "https://www.concursosnobrasil.com.br/concursos/es/"
    page = urllib2.urlopen(fof)
    soup = BeautifulSoup(page, "lxml", from_encoding="latin-1")
    f = soup.find_all('a', {'class': 'orgao'})
    concursos = []
    for assunto in f:
        concursos.append(assunto['title'])

    base_concurso = open('p-concursos.aiml', 'w+')
    base_concurso.write('<?xml version="1.0" encoding="iso-8859-1"?>\n'
                       '<aiml version="1.0">\n'
                       '<meta name="author" content="PyES"/>\n'
                       '<meta name="language" content="pt-br"/>\n')
    base_concurso.write('<category>\n'
                        '<pattern>CONCURSO</pattern>\n'
                       '<template>\n'
                       '<random>\n')

    for x in concursos:
        base_concurso.write('<li>' + x.encode('latin-1') + '</li>\n')
    base_concurso.write('</random>\n</template>\n</category>')
    base_concurso.write('<category>\n'
                        '<pattern>* CONCURSO</pattern>\n'
                       '<template>\n'
                        '<srai>CONCURSO</srai>\n'
                       '</template>\n'
                       '</category>\n'
                       '<category>\n'
                        '<pattern>* CONCURSO *</pattern>\n'
                       '<template>\n'
                        '<srai>CONCURSO</srai>\n'
                       '</template>\n'
                       '</category>\n'
                       '<category>\n'
                        '<pattern>CONCURSO *</pattern>\n'
                       '<template>\n'
                        '<srai>CONCURSO</srai>\n'
                       '</template>\n'
                       '</category>\n')
    base_concurso.write('</aiml>')

    base_concurso.close()
