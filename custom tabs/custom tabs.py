"""
Custom Tabs
"""

from Tkinter import *

def Custom_tabs():
	root = Tk()
	root.title("Custom Tabs")
	root.geometry("800x500")

	#frames
	tab_container_main = Frame(root, height = 40, bg = "red")
	tab_container_main.pack_propagate(0)
	tab_container_main.pack(side = "top", fill = "x")

	padd_top = Frame(tab_container_main, height = 4, bg = "#171814")
	padd_top.pack(side = "top", fill = "x")

	global tab_container;
	tab_container = Frame(tab_container_main, height = 35, bg = "#171814")
	tab_container.pack(side = "top", fill = "x")

	padd_bottom = Frame(tab_container_main, height = 1, bg = "#171814")
	padd_bottom.pack(side = "top", fill = "x")

	#custom tab
	custom_tab = Frame(tab_container, width = 100, height = 35, bg = "#272822")
	custom_tab.pack(side = "left", padx = 3)

	#test button
	tab_test = Button(root, command = lambda: new_tab("event"))
	tab_test.pack(pady = 20)

	root.mainloop()

global new_tab;
def new_tab(tab_number):
	tab_counter = 2

	print tab_number

	custom_tab_new = Frame(tab_container, width = 100, height = 35, bg = "#272822", text = "tab %s" % tab_counter)
	custom_tab_new.pack(side = "left", padx = 3)

	tab_number += 1

Custom_tabs()