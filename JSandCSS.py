import sys
from tkinter import messagebox

def SEDGE_isnum(nm):
	mm = True
	for i in nm:
		if not i in "0123456789":
			mm = False
	return mm
def gets(dict,val):
	for i in dict.keys():
		if dict[i] == val:
			return i
def none_button_command():
	pass
def alert_button_command():
	msg1 = messagebox.showinfo(title="Sedge MessageBox", message="->Sedge Message Box Test<-")
	print("DEBUG:SedgeMessageBox.Type="+msg1)
def exit_sedge_button_command():
	sys.exit()
def basic_alert():
	msg1 = messagebox.showinfo(title="Sedge Information MessageBox", message="0")
	print("DEBUG:SedgeMessageBox.Type=[DEBUGER]"+msg1)
def deb_n():
	print("SystemMessage:__state__=SEDGE.SIMPLE;__error__=SEDGE.NONE;")
	print("SystemMessage:__StateCode__=SEDGE._0")
def ret(a):
	return a
def css_parser(text):
	try:
		alls = []
		allss = []
		allsss,allssss = {},{}
		temp = ""
		tmp = list(text)
		for i in tmp:
			temp += i
			if i == '}':
				alls.append(temp)
				temp = ""
		for i in alls:
			tmp = i.split("{")
			allsss[tmp[0]],allssss[tmp[0]] = tmp[1][:-2],tmp[1][:-2]
		for i in allsss.values():
			ns = i.split(":")
			ns = {ns[0]:ns[1]}
			allssss[gets(allssss,i)] = ns
		return allssss
	except IndexError:
		pass

def js_parser(text):
	mem,varn = "",""
	var = {"__browser__":"Sedge","__version__":"0.1.3","__update__":"Javascript Update--Very BIG!","__port__":"client","__language__":"JavaScript"}
	clr,clrs,state = [],[],"DEF"
	text = text.split("\n")
	for i in text:
		for j in i:
			mem+=j
			if mem in ["let","var","console.log"]:
				clr.append(mem[:])
				mem = ""
			elif mem[0] == "\"" and mem[-1] == "\"":
				clr.append(mem[1:-1][:])
				mem = ""
			elif SEDGE_isnum(mem[:-1]):
				clr.append(mem[:-1][:])
				mem = mem[-1]
			elif j == ";":
				clr.append(mem[:-1])
				mem = ""
			elif j == "=":
				clr = mem[:]
				mem = ""
			#print(mem)
	for i in clr:
		if i == "console.log":
			state = "output"
		elif i in ["var","let"]:
			state = "var_set"
		elif i == "=":
			state = "eqs" 
		elif i!="":
			if state == "output":
				if i[1] == "\"":
					n = i[2:-2]
				else:
					n = i[1:-1]
				print("JavaScript:"+n)
			elif state == "var_set":
				var[i] = "undefined"
				varn = i
			elif state == "eqs":
				var[varn] = i
				print(var)
			state = "DEF"