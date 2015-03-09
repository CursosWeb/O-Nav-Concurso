#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script 

Para ejecutarlo, desde la shell: 
 $ python 

"""

import os

logins = [
    "jginesclavero",
    "sorellan",
    "ilopezba",
#    "djprano",
    "vcarrera",
#    "lauraoeo",
    "mavilam",
    "dgsison",
    "pirumano",
    "rebemartinezgr",
    "mrobledo",
    "garaujoriestra",
#    "jmmartinc",
#    "acamara7es",
    "itzgarci",
    "RNicklasR",
    "dlumbrer",
    "jasaizc",
#    "islimane",
    "miansaay",
    "krutus",
    "kivenoliva",
    "pitu93",
    "albertoflorez",
    "jonyB0B",
    "crismartin",
    "adrianvinuelas",
    "yusfer",
#    "kthristov",
    "asu88",
    "dpaz",
#    "albertoabades",
#    "adrianalonsoba"
    ]

os.mkdir("concurso")
indice = open('concurso/index.html', 'w')
indice.write("")
indice.write("<ul>\n")

for login in logins:
    print "Bajando el repositorio de " + login
    repo_git = "http://github.com/" + login + "/X-Nav-Bootstrap-Concurso"
    os.system('git clone ' + repo_git + ' concurso/' + str(logins.index(login)) + ' > /dev/null 2>&1')
    indice.write('  <li><a href="' + str(logins.index(login)) + '/index.html">' + str(logins.index(login)) + '</a>\n')
indice.write("</ul>")
indice.close()
