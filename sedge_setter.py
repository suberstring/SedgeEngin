import sys
from tkinter import messagebox

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