from lxml import etree
from tkinter import *
import requests as r
from PIL import Image,ImageTk
import platform

def attrib_in_label(be_s,sub):
	return be_s in list(sub.keys())
history = []
a_to = "file://C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\first.html"
header_s = "Chrome"
def down():
	cv.move("all", 0, -40)
def up():
	cv.move("all",0,40)
def back():
	if len(history) >= 2:
		textv.delete(0)
		textv.insert(0,history[-2])
		go()
def go():
	global header_s
	if not "file://" in textv.get():
		try:
			ins = "(Windows NT;"+platform.architecture()[0]+")"
			if header_s == "Sedge":
				headers={"User-Agent":"Mozilla/5.0 "+ins+" SedgeBE/0.0.1 (KHTML) Sedge/0.0.0.10 Safari/537.36"}
			elif header_s == "Chrome":
				headers={"User-Agent":"'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'"}
			history.append(textv.get())
			rendering(text=r.get(textv.get(),headers=headers).text)
		except r.exceptions.ConnectionError:
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html") as d:
				texts = d.read()
				rendering(text=texts,fail=True)
		except r.exceptions.MissingSchema:
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html") as d:
				texts = d.read()
				rendering(text=texts,fail=True,website=textv.get())
	else:
		try:
			with open(textv.get()[7:]) as d:
				texts = d.read()
				history.append(textv.get())
				rendering(text=texts)
		except FileNotFoundError:
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\internet.html") as d:
				texts = d.read()
				rendering(text=texts,fail=True,website=textv.get())
def when_a():
	global a_to
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) SedgeBrowserEngin/0.0.1 (KHTML, like Gecko) Sedge/0.0.0.10"}
	try:
		rendering(text=r.get(a_to,headers=headers).text)
	except r.exceptions.ConnectionError:
		with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html") as d:
			texts = d.read()
			rendering(text=texts,fail=True)
	except r.exceptions.MissingSchema:
		with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html") as d:
			texts = d.read()
			rendering(text=texts,fail=True,website=textv.get())
f = 1
p_font=("微软雅黑",13)
h1_font=("微软雅黑",25,"bold")
h2_font=("微软雅黑",22,"bold")
h3_font=("微软雅黑",19,"bold")
h4_font=("微软雅黑",16,"bold")
h5_font=("微软雅黑",12,"bold")
a_font = ("微软雅黑",13,"underline")
root = Tk()
root.title("Sedge1-Test")
root.geometry("800x540")
root.configure(bg='white')
cv =Canvas(root,width=8000,height=16000,background='white')
cv.place(x=0,y=60)
head = PanedWindow(height=60,width=800,orient=HORIZONTAL)
textv = Entry(head, width=100,font=p_font)
textv.insert(0,"file://C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\first.html")
textv.place(x=0,y=0)
sublime = Button(head,text="GO!", width=10,height=1,command=go)
sublime.place(x=717,y=0,anchor="nw")
ret = Button(head,text="Back", width=51,height=1,command=when_a)
ret.place(x=0,y=30,anchor="nw")
up = Button(head,text="Up", width=30,height=1,command=up)
up.place(x=361,y=30,anchor="nw")
down = Button(head,text="Down", width=30,height=1,command=down)
down.place(x=580,y=30,anchor="nw")
head.place(x=0,y=0,anchor="nw")
links=[]
im,imgs = None,None
if f:
	with open("first.html") as d:
		text = d.read()
else:
	text = r.get("https://suberstring.github.com/search/funnyface/super_invincible_top_comic_emoji_pck").text
	print(text)

def rendering(text,fail=False,website=" "):
	global im,imgs
	cv.delete("all")
	global a_to
	if fail:
		print("Error[02]:Page ",website," does not exist")
	true_tag = ["h1","p","ol","ul","li","body","footer","head","header","title","html","img"]
	print("Task[0]:Page Created.")
	html = etree.HTML(text)
	res = html.xpath("//*")
	print("Task[1]:Code Splited.")
	v = []
	pc = 0
	for i in res:
		v.append({"tag":i.tag,"text":i.text,"attrib":i.attrib,"id":str(pc)})
		pc+=1

	x = 5
	wt = ["true","more","false"]
	y = 5
	state = ""
	times = 1
	bg = "white"
	fg = "black"
	print("Task[2]:Starting Rendering.")
	cds = 0
	tx = 5
	for i in v:
		if i["tag"] == "p" or i["tag"] == "dd":
			print("Task[2-"+i["id"]+"]:Label <p> rendered")
			cv.create_text(x,y,text = i['text'],font=p_font,fill=fg,anchor=NW)
			y+=35*(str(i["text"]).count("\n")+1)
			x=5
		elif i["tag"] == "code":
			cv.create_rectangle(25,y-3,775,y+22.5*(str(i["text"]).count("\n")+1)+3,fill="#F8F8F2")
			cv.create_text(x,y,text = "     "+str(i['text']).replace("\n","\n     "),font=p_font,fill=fg,anchor=NW)
			y+=35*(str(i["text"]).count("\n")+1)
			x=5
		elif i["tag"] == "h1":
			print("Task[2-"+i["id"]+"]:Label <h1> rendered")
			cv.create_text(x,y,text = i['text'],font=h1_font,fill=fg,anchor=NW)
			y+=58
			x=5
		elif i["tag"] == "h2":
			print("Task[2-"+i["id"]+"]:Label <h2> rendered")
			cv.create_text(x,y,text = i['text'],font=h2_font,fill=fg,anchor=NW)
			y+=52
			x=5
		elif i["tag"] == "h3":
			print("Task[2-"+i["id"]+"]:Label <h3> rendered")
			cv.create_text(x,y,text = i['text'],font=h3_font,fill=fg,anchor=NW)
			y+=48
			x=5
		elif i["tag"] == "h4":
			print("Task[2-"+i["id"]+"]:Label <h4> rendered")
			cv.create_text(x,y,text = i['text'],font=h4_font,fill=fg,anchor=NW)
			y+42
			x=5
		elif i["tag"] == "h5":
			print("Task[2-"+i["id"]+"]:Label <h5> rendered")
			cv.create_text(x,y,text = i['text'],font=h5_font,fill=fg,anchor=NW)
			y+=42
			x=5
		elif i["tag"] == "title":
			print("Task[2-"+i["id"]+"]:Label <title> rendered")
			root.title(i["text"])
		elif i["tag"] == "body":
			if attrib_in_label("bgcolor",i["attrib"]):
				v.create_rectangle(0,0,10000,10000,fill=i["attrib"]["bgcolor"])
		elif i["tag"] == "ul":
			print("Task[2-"+i["id"]+"]:Label <ul> rendered")
			state = "ul"
		elif i["tag"] == "a":
			a_to = i["attrib"]["href"]
			subli = Button(cv,text=i["text"], width=10,height=1,command=when_a,bg=bg,fg="blue")
			cv.create_window(x,y,anchor="nw",window=subli)
			links.append(subli)
			x+=100
		elif i["tag"] == "li":
			print("Task[2-"+i["id"]+"]:Label <li> rendered")
			if i["text"]!=None:
				if state == "ul":
					cv.create_text(x,y,text = "    •"+str(i['text']),font=p_font,fill=fg,anchor=NW)
					y+=30
					x=5
				elif state == "ol":
					cv.create_text(x,y,text = "    "+str(times)+"."+i['text'],font=p_font,fill=fg,anchor=NW)
					y+=30
					x=5
					times+=1
		elif i["tag"] == "ol":
			print("Task[2-"+i["id"]+"]:Label <ol> rendered")
			state = "ol"
		elif i["tag"] == "error":
			print("Task[2-"+i["id"]+"]:Label <error> rendered")
			wt = [i["attrib"]["warn"],i["attrib"]["info"],i["attrib"]["error_exit"]]
		elif i["tag"] == "br":
			y+=35
			x=5
		elif i["tag"] == "img":
			try:
				imgs = Image.open(i["attrib"]["src"])
			except FileNotFoundError:
				imgs = Image.open("unknown.png")
			except OSError:
				imgs = Image.open("unknown.png")
			im = ImageTk.PhotoImage(imgs)
			cv.create_image(x,y,image=im,anchor="nw")
			y+=imgs.height
		elif i["tag"] == "table":
			state="table"
			table_loc = "header"
		elif i["tag"] == "tr":
			cds += 1
			y+=40
			tx = 5
		elif i["tag"] == "thead":
			table_loc = "header"
		elif i["tag"] == "tbody":
			table_loc = "values"
		elif i["tag"] == "td":
			if state == "table":
				if table_loc == "header":
					cv.create_rectangle(tx,y,tx+150,y+40,fill="gray")
					cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
					tx+=150
				elif table_loc == "values":
					cv.create_rectangle(tx,y,tx+150,y+40)
					cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
					tx+=150
		elif i["tag"] not in true_tag:
			if wt[0] == "true":
				if wt[1] == "more":
					print("Warning[01]:Unknown Tag(Label) ",i["tag"],".")
					if wt[2] == "true":
						sys.exit(1)

rendering(text=text)
root.mainloop()