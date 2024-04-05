from lxml import etree
from tkinter import *
from tkinter import messagebox
import requests as r
from PIL import Image,ImageTk
import platform,cv2,sys,math,re
from sedge_setter import *

def inx(dic,v):
	return v in list(dic.keys())
def attrib_in_label(be_s,sub):
	return be_s in list(sub.keys())
history = []
a_to = "file://C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\first.html"
header_s = "Sedge"
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
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html",encoding="utf-8") as d:
				texts = d.read()
				rendering(text=texts,fail=True)
		except r.exceptions.MissingSchema:
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\error.html",encoding="utf-8") as d:
				texts = d.read()
				rendering(text=texts,fail=True,website=textv.get())
	else:
		try:
			with open(textv.get()[7:],encoding="utf-8") as d:
				texts = d.read()
				history.append(textv.get())
				if textv.get()[7:].split(".")[1] == ".sedgeml":
					rendering(text=texts,typ="wbs")
				else:
					rendering(text=texts,typ="htm")
		except FileNotFoundError:
			with open("C:\\Users\\Administrator\\Desktop\\pythons\\Sedge\\internet.html",encoding="utf-8") as d:
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
h6_font=("微软雅黑",10,"bold")
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

def rendering(text,fail=False,website=" ",typ="wbs"):
	if True:
		global im,imgs
		cv.delete("all")
		global a_to
		if fail:
			print("Error[02]:Page ",website," does not exist")
		true_tag = ["h1","p","ol","ul","li","body","footer","head","header","title","html","img",]
		print("Task[0]:Page Created.")
		html = etree.HTML(text)
		res = html.xpath("//*")
		print("Task[1]:Code Splited.")
		v = []
		css_list = {}
		pc = 0
		for i in res:
			v.append({"tag":i.tag,"text":i.text,"attrib":i.attrib,"id":str(pc)})
			pc+=1

		x = 5
		wt = ["true","more","false"]
		y = 5
		state = ""
		backc = "white"
		times = 1
		bg = "white"
		fg = "black"
		print("Task[2]:Starting Rendering.")
		cds = 0
		tx = 5
		for i in v:
			if i["tag"] == "p" or i["tag"] == "dt" or i["tag"] == "dd":
				ls = 0
				lns = ""
				for ys in i["text"]:
					if ls >= 54:
						lns += "\n"
						ls = 0
					ls+=1
					lns+=ys
				i["text"] = lns
				print("Task[2-"+i["id"]+"]:Label <p> rendered")
				if not attrib_in_label("style",i["attrib"]):
					cv.create_text(x,y,text = i['text'],font=p_font,fill=fg,anchor=NW)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					backc = "white"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+30*(str(i["text"]).count("\n")+1),fill=backc)
					if text_align == "center" or {"text-align":None}:
						cv.create_text(400,y,text = i['text'],font=p_font,fill=fg)
					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=p_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=p_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=35*(str(i["text"]).count("\n")+1)
				x=5
			elif i["tag"] == "style":
				"""Return somthing like:css_list={"h1":{"text-align":"Center"}}"""
				ty = i["text"].replace(" ","").replace("\t","").replace("\n","")
				css_list = css_parser(ty)
			elif i["tag"] == "code":
				cv.create_rectangle(25,y-3,775,y+22.5*(str(i["text"]).count("\n")+1)+3,fill="#F8F8F2")
				cv.create_text(x,y,text = "     "+str(i['text']).replace("\n","\n     "),font=p_font,fill=fg,anchor=NW)
				y+=35*(str(i["text"]).count("\n")+1)
				x=5
			elif i["tag"] == "h1":
				if not inx(css_list,"h1"):
					css_list["h1"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h1> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h1"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h1_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h1_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+58,fill=backc)
					if css_list["h1"]["text-align"] == "CENTER" or text_align == "center":
						cv.create_text(400,y,text = i['text'],font=h1_font,fill=fg)

					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=h1_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=h1_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=58
				x=5
			elif i["tag"] == "h2":
				if not inx(css_list,"h2"):
					css_list["h2"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h2> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h2"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h2_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h2_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+52,fill=backc)
					if text_align == "center" or css_list["h2"]["text-align"] == "CENTER":
						cv.create_text(400,y,text = i['text'],font=h2_font,fill=fg)
					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=h2_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=h2_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=52
				x=5
			elif i["tag"] == "h3":
				if not inx(css_list,"h3"):
					css_list["h3"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h3> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h3"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h3_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h3_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+48,fill=backc)
					if text_align == "center" or css_list["h3"]["text-align"] == "CENTER":
						cv.create_text(400,y,text = i['text'],font=h3_font,fill=fg)
					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=h3_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=h3_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=48
				x=5
			elif i["tag"] == "h4":
				if not inx(css_list,"h4"):
					css_list["h4"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h4> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h4"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h4_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h43_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+42,fill=backc)
					if text_align == "center" or css_list["h4"]["text-align"] == "CENTER":
						cv.create_text(400,y,text = i['text'],font=h4_font,fill=fg)
					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=h4_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=h4_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+42
				x=5
			elif i["tag"] == "h5":
				if not inx(css_list,"h5"):
					css_list["h5"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h5> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h5"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h5_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h5_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+42,fill=backc)
					if text_align == "center" or css_list["h5"]["text-align"] == "CENTER":
						cv.create_text(400,y,text = i['text'],font=h5_font,fill=fg)
					elif text_align == "right":
						cv.create_text(800,y,text = i['text'],font=h5_font,fill=fg,anchor=NE)
					elif text_align == "left":
						cv.create_text(x,y,text = i['text'],font=h5_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=42
				x=5
			elif i["tag"] == "h6":
				if not inx(css_list,"h6"):
					css_list["h6"] = {"text-align":None}
				print("Task[2-"+i["id"]+"]:Label <h6> rendered")
				if not attrib_in_label("style",i["attrib"]):
					if not css_list["h6"]["text-align"] == "CENTER":
						cv.create_text(x,y,text = i['text'],font=h6_font,fill=fg,anchor=NW)
					else:
						cv.create_text(400,y,text = i['text'],font=h6_font,fill=fg)
				else:
					styles = i["attrib"]["style"].split(";")
					text_align="left"
					for j in styles:
						if "text-align" in j:
							text_align = j.split(":")[1]
						elif "background-color" in j:
							backc = j.split(":")[1]
					if backc != "white":
						cv.create_rectangle(x,y,1000,y+32,fill=backc)
					if text_align == "center" or css_list["h6"]["text-align"] == "CENTER":
						cv.create_text(400,y,text = i['text'],font=h6_font,fill=fg)
					elif text_align == "right" or css_list["h6"] == "RIGHT":
						cv.create_text(800,y,text = i['text'],font=h6_font,fill=fg,anchor=NE)
					elif text_align == "left" or css_list["h6"] == "LEFT":
						cv.create_text(x,y,text = i['text'],font=h6_font,fill=fg,anchor=NW)
					else:
						print("Unknown value of \"text-align\" in \"style\"")
				y+=32
				x=5
			elif i["tag"] == "title":
				print("Task[2-"+i["id"]+"]:Label <title> rendered")
				root.title(i["text"])
			elif i["tag"] == "body":
				if attrib_in_label("bgcolor",i["attrib"]):
					v.create_rectangle(0,0,10000,10000,fill=i["attrib"]["bgcolor"])
			elif i["tag"] == "ul" or i["tag"] == "menu":
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
						vsd = ""
						for hgf in range(0,4-len(str(times))):
							vsd += " "
						cv.create_text(x,y,text = vsd+str(times)+"."+i['text'],font=p_font,fill=fg,anchor=NW)
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
				print("Task[2-"+i["id"]+"]:Label <thead> rendered")
			elif i["tag"] == "tbody":
				table_loc = "values"
				print("Task[2-"+i["id"]+"]:Label <tbody> rendered")
			elif i["tag"] == "td":
				print("Task[2-"+i["id"]+"]:Label <td> rendered")
				if state == "table":
					if table_loc == "header":
						if not attrib_in_label("style",i["attrib"]):
							cv.create_rectangle(tx,y,tx+150,y+40,fill="white")
							cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
						else:
							styles = i["attrib"]["style"].split(";")
							text_align="left"
							backc="white"
							for j in styles:
								if "text-align" in j:
									text_align = j.split(":")[1]
								elif "background-color" in j:
									backc = j.split(":")[1]
							cv.create_rectangle(tx,y,tx+150,y+40,fill=backc)
							if text_align == "center":
								cv.create_text(tx+75,y+5,text=i["text"])
							elif text_align == "right":
								cv.create_text(tx+145,y+5,text=i["text"],anchor="ne")
							elif text_align == "left":
								cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
							else:
								print("Unknown value of \"text-align\" in \"style\"")
						tx+=150
					elif table_loc == "values":
						if not attrib_in_label("style",i["attrib"]):
							cv.create_rectangle(tx,y,tx+150,y+40,fill="white")
							cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
						else:
							styles = i["attrib"]["style"].split(";")
							text_align="left"
							backc="white"
							for j in styles:
								if "text-align" in j:
									text_align = j.split(":")[1]
								elif "background-color" in j:
									backc = j.split(":")[1]
							cv.create_rectangle(tx,y,tx+150,y+40,fill=backc)
							if text_align == "center":
								cv.create_text(tx+75,y+5,text=i["text"])
							elif text_align == "right":
								cv.create_text(tx+145,y+5,text=i["text"],anchor="ne")
							elif text_align == "left":
								cv.create_text(tx+5,y+5,text=i["text"],anchor="nw")
							else:
								print("Unknown value of \"text-align\" in \"style\"")
						tx+=150
			elif i["tag"] == "button":
				print("Task[2-"+i["id"]+"]:Label <button> rendered")
				disa = NORMAL
				com = none_button_command
				if attrib_in_label("disabled",i["attrib"]):
					disa = DISABLED
				if attrib_in_label("command",i["attrib"]):
					if i["attrib"]["command"] == "alert()":
						com = alert_button_command
					if i["attrib"]["command"] == "SedgeKit.ApplicationControl.exit()":
						com = exit_sedge_button_command
					if i["attrib"]["command"] == "SedgeKit.ApplicationInfo.BrowserVersion()":
						com = get_version_button_command_browser
					if i["attrib"]["command"] == "SedgeKit.ApplicationInfo.EnginVersion()":
						com = get_version_button_command_kit
					if i["attrib"]["command"] == "SedgeKit.ApplicationControl.ReturnNow()":
						com = deb_n
				but = Button(cv,text=i["text"], width=math.floor(1.2*len(i["text"]))+1,height=1,command=com,bg=bg,state=disa)
				cv.create_window(x,y,anchor="nw",window=but)
				y+=40

			elif i["tag"] in ["html"]:
				pass
			else:
				if wt[0] == "true":
					if wt[1] == "more":
						print("Warning[01]:Unknown Tag(Label) ",i["tag"],".")
						if wt[2] == "true":
							sys.exit(1)

	else:
		text = text.split("**")
		print(text)


rendering(text=text)
root.mainloop()
