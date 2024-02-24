from lxml import etree
from tkinter import *
import requests as r

def command():
	a = r.get(i['attrib']['href'])
	print(a.text)
p_font=("微软雅黑",13)
h1_font=("微软雅黑",30,"bold")
a_font = ("微软雅黑",13,"underline")
root = Tk()
root.title("Sedge1-Test")
root.geometry("800x500")
root.configure(bg='white')
f = True
if f:
	with open("first.html") as d:
		text = d.read()
else:
	text = r.get("https://httpbin.org/post").text

html = etree.HTML(text)
res = html.xpath("//*")
v = []
pc = 0
for i in res:
	print(i.text)
	v.append({"tag":i.tag,"text":i.text,"attrib":i.attrib,"id":pc})
	pc+=1

x = 5
y = 5
state = ""
times = 1
bg = "white"
for i in v:
	print(i["tag"])
	if i["tag"] == "p":
		l = Label(text = i['text'],font=p_font,bg=bg)
		l.place(x=x,y=y,height=35,anchor="nw")
		y+=35
	elif i["tag"] == "h1":
		l = Label(text = i['text'],font=h1_font,bg=bg)
		l.place(x=x,y=y,height=55,anchor="nw")
		y+=60
	elif i["tag"] == "title":
		root.title(i["text"])
	elif i["tag"] == "a":
		l = Button(text = i['text'],font=a_font,bg=bg,fg="blue",command=command)
		l.place(x=x,y=y,height=40,anchor="nw")
		y+=45
	elif i["tag"] == "body":
		if i["attrib"] != {}:
			root.configure(bg=i["attrib"]["bgcolor"])
			bg = i["attrib"]["bgcolor"]
	elif i["tag"] == "ul":
		state = "ul"
	elif i["tag"] == "li":
		if state == "ul":
			l = Label(text = "    •"+i['text'],font=p_font,bg=bg)
			l.place(x=x,y=y,height=35,anchor="nw")
			y+=25
		else:
			l = Label(text = "    "+str(times)+"."+i['text'],font=p_font,bg=bg)
			l.place(x=x,y=y,height=35,anchor="nw")
			y+=25
			times+=1
	elif i["tag"] == "ol":
		state = "ol"

	elif i["tag"] not in ["head","html"]:
		l = Label(text = i['text'],font=p_font,bg=bg)
		l.place(x=x,y=y,height=35,anchor="nw")
		y+=10

root.mainloop()