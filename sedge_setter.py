import sys
from tkinter import messagebox

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
def get_version_button_command_browser():
	msg1 = messagebox.showinfo(title="Sedge Information MessageBox", message="Sedge0.0.5:CSS and Label Update 2[2024/3/31,RELEASE:2024/4/6]")
	print("DEBUG:SedgeMessageBox.Type=[DEBUGER]"+msg1)
def get_version_button_command_kit():
	msg1 = messagebox.showinfo(title="Sedge Information MessageBox", message="SedgeEngin0.5.4:CSS & Attribute Update[For CSS and Label Update 2]")
	print("DEBUG:SedgeMessageBox.Type=[DEBUGER]"+msg1)
def deb_n():
	print("SystemMessage:__state__=SEDGE.SIMPLE;__error__=SEDGE.NONE;")
	print("SystemMessage:__StateCode__=SEDGE._0")
def ret(a):
	return a
def css_parser(text):
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

print(css_parser("h1{text-align:center;}"))