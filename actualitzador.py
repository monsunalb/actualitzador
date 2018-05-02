#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Albert Montaña

import os, sys, time

def checkfile(fitxer):
	if fitxer[-3:] != ".py" and fitxer[-4:] != ".py2":
		sys.exit("el fitxer no està en python (.py)")
def anar_a(path):
	pathr= path.rpartition("/")[0]
	fitxer = path.rpartition("/")[2]
	checkfile(fitxer)
	try:
		os.chdir(pathr)
	except:
		sys.exit("path no trobada")
	return fitxer, pathr

def filechanged(fitxer, llarg):
	global a, params, columns
	if a != open(fitxer, "r").readlines():
		a = open(fitxer, "r").readlines()
		os.system("clear")
		to_pass = "python " + fitxer + " " + params
		barra = "~~~~~"
		to_pass2 = barra + llarg + barra
		print '%s%s' % (' ' * ((int(columns) / 2) - (len(to_pass2) / 2)), to_pass2)
		os.system(to_pass)

def get_dir_pys(path):
	onepy = 0
	pys = ""
	for afile in os.listdir(path):
		if afile[-3:] == ".py":
			if onepy == 0:
				pys = afile
			else:
				pys = pys + "\n" + afile
			onepy = 1
	for afile in os.listdir(path):
		if afile[-4:] == ".py2":
			if onepy == 0:
				pys = afile
			else:
				pys = pys + "\n" + afile
	if onepy == 0:
		return 0
	else:
		return pys
		

def main():
	global a, params, columns
	try:
		fitxer = sys.argv[1]
	except:
		fitxer = raw_input("Quin programa vols veure?\n>>")
	fitxerr, pathr = anar_a(fitxer)
	try:
		a = open(fitxerr, "r").readlines()
		params = raw_input("vols passar parametres?")
		if params == " " or params == "":
			params == ""
		if params == "_":
			if fitxerr[-3:] == ".py":
				params = "< %s.txt"%fitxerr[:-3]
			elif fitxerr[-4:] == ".py2":
				params = "< %s.txt"%fitxerr[:-4:]
		if params[:1] != " ":
			params = " " + params
		to_pass = "python " + fitxer + params
		os.system("clear")
		barra = "~~~~~"
		to_pass2 = barra + fitxer + barra 
		print '%s%s' % (' ' * ((int(columns) / 2) - (len(to_pass2) / 2)), to_pass2)
		os.system(to_pass)
	except:
		if get_dir_pys(pathr):			
			to_pass = "%s no trobat a %s, potser et referies a...\n" %(fitxerr, pathr) + get_dir_pys(pathr)
		else:
			to_pass = "fitxer no trobat\nno hi ha fitxers .py en aquest directori"
		sys.exit(to_pass)
	while 1:
		time.sleep(1.5)
		rows, columns = os.popen('stty size', 'r').read().split()
		filechanged(fitxerr,fitxer)
a = 0
params = ""
rows, columns = os.popen('stty size', 'r').read().split()
main()