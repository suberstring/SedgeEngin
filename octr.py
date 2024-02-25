from lxml import etree
from tkinter import *
import requests as r

def go():
	if not "file://" in textv.get():
		rendering(text=r.get(textv.get()).text)
	else:
		with open(textv.get()[7:]) as d:
			texts = d.read()
			rendering(text=texts)
p_font=("微软雅黑",13)
h1_font=("微软雅黑",30,"bold")
a_font = ("微软雅黑",13,"underline")
root = Tk()
root.title("Sedge1-Test")
root.geometry("800x540")
root.configure(bg='white')
head = PanedWindow(height=30,width=800,orient=HORIZONTAL)
textv = Entry(head, width=100,font=p_font)
textv.place(x=0,y=0)
sublime = Button(head,text="GO!", width=10,height=1,command=go)
sublime.place(x=720,y=0,anchor="nw")
head.place(x=0,y=0,anchor="nw")
f = 1
if f:
	with open("first.html") as d:
		text = d.read()
else:
	text = r.get("https://httpbin.org/get").text
	print(text)

def rendering(text):
	cv =Canvas(root,width=800,height=1600,background='white')
	cv.place(x=0,y=30)
	html = etree.HTML(text)
	res = html.xpath("//*")
	v = []
	pc = 0
	for i in res:
		print(i.text)
		v.append({"tag":i.tag,"text":i.text,"attrib":i.attrib,"id":pc})
		pc+=1

	x = 0
	y = 45
	state = ""
	times = 1
	bg = "white"
	fg = "black"
	for i in v:
		print(i["tag"])
		if i["tag"] == "p":
			cv.create_text(x,y,text = i['text'],font=p_font,fill=fg,anchor=NW)
			y+=35
		elif i["tag"] == "h1":
			cv.create_text(x,y,text = i['text'],font=h1_font,fill=fg,anchor=NW)
			y+=60
		elif i["tag"] == "title":
			root.title(i["text"])
		elif i["tag"] == "a":
			pass
		elif i["tag"] == "body": 
			if i["attrib"] != {}:
				root.configure(bg=i["attrib"]["bgcolor"])
				bg = i["attrib"]["bgcolor"]
		elif i["tag"] == "ul":
			state = "ul"
		elif i["tag"] == "li":
			if state == "ul":
				cv.create_text(x,y,text = "    •"+i['text'],font=p_font,fill=fg,anchor=NW)
				y+=30
			else:
				cv.create_text(x,y,text = "    "+str(times)+"."+i['text'],font=p_font,fill=fg,anchor=NW)
				y+=30
				times+=1
		elif i["tag"] == "ol":
			state = "ol"

rendering(text=text)
root.mainloop()