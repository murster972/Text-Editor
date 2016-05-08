 #!/usr/bin/env python 
from Tkinter import *
from tkFileDialog import *
import ttk, tkFont
from tkColorChooser import askcolor

def main_window():
	#creates the main window(the text-editor)
	global root;
	root = Tk()
	root.title("untitled ~ M-Text")
	padd_x = (root.winfo_screenwidth() - 700) / 2
	padd_y = (root.winfo_screenheight() - 700) / 2
	root.geometry("700x500+%s+%s" % (padd_x, padd_y))
	root.config(bg = "#FFFFFF")
	root.minsize(width = 500, height = 200)
	#root.iconbitmap("@icon.xbm")
	root.protocol("WM_DELETE_WINDOW", close_options)

	#gets screen sizes
	width = root.winfo_screenwidth()
	height = root.winfo_screenheight()

	#creates menubar
	global menubar;
	menubar = Menu(root, relief = FLAT, bg = "#E8E8E8", fg = "#7c7c7c", activeborderwidth = 0, activebackground = "#F8F8F8", activeforeground = "#7c7c7c", bd = 0, font = ("arial", 12))
	filemenu = Menu(menubar, tearoff = 0, takefocus = 0, bg = "#F0F0F0", fg = "#7c7c7c", relief = FLAT, activeborderwidth = 0, activebackground = "#F8F8F8", activeforeground = "#7c7c7c", font = ("verdana", 11))
	filemenu.add_command(label = " New                ", command = lambda: file_operations("NA", "new file", "NA", "no"))
	filemenu.add_command(label = " Open", command = lambda: file_operations("NA", "open file", "NA", "no"))
	filemenu.add_command(label = " Save", command = lambda: file_operations("NA", "save file", "save", "no"))
	filemenu.add_command(label = " Save as...", command = lambda: file_operations("NA", "save file", "save as", "no"))
	filemenu.add_separator()
	filemenu.add_command(label = " Print")
	filemenu.add_separator()
	filemenu.add_command(label = " Exit", command = root.quit)
	menubar.add_cascade(label = "       File       ", menu = filemenu)

	editmenu = Menu(menubar, tearoff = 0, takefocus = 0, bg = "#F0F0F0", fg = "#7c7c7c", relief = FLAT, activeborderwidth = 0, activebackground = "#F8F8F8", activeforeground = "#7c7c7c", font = ("verdana", 11))
	editmenu.add_command(label = " Copy                ", command = lambda: text_area.event_generate("<<Copy>>"))
	editmenu.add_command(label = " Cut", command = lambda: text_area.event_generate("<<Cut>>"))
	editmenu.add_command(label = " Paste", command = lambda: text_area.event_generate("<<Paste>>"))
	editmenu.add_command(label = " Select All", command = lambda: text_area.tag_add(SEL, "1.0", END))
	editmenu.add_command(label = " Undo", command = lambda: text_area.edit_undo())
	#editmenu.add_separator()
	#editmenu.add_command(label = " Preferences") #command = preferences)
	menubar.add_cascade(label = "       Edit       ", menu = editmenu)

	#right click menu
	rightclick_menu = Menu(None, tearoff = 0, takefocus = 0, bg = "#F0F0F0", relief = FLAT, activeborderwidth = 0, activebackground = "#F8F8F8", activeforeground = "#989898", font = ("verdana", 11))
	rightclick_menu.add_command(label = "     Copy  ", command = lambda: text_area.event_generate("<<Copy>>"))
	rightclick_menu.add_command(label = "     Cut  ", command = lambda: text_area.event_generate("<<Cut>>"))
	rightclick_menu.add_command(label = "     Paste  ", command = lambda: text_area.event_generate("<<Paste>>"))
	rightclick_menu.add_command(label = "     Select All  ", command = lambda: text_area.tag_add(SEL, "1.0", END))
	rightclick_menu.add_command(label = "     Close Menu...  ")
	rightclick_menu.add_command(label = "     Exit  ", command = root.quit and root.destroy)

	def rightclick_menu_activate(event):
		try:
			rightclick_menu.post(event.x_root, event.y_root)

		finally:
			rightclick_menu.grab_release()

	def rightclick_menu_release(event):
		rightclick_menu.unpost()

	ttk.Style().configure("TScrollbar", relief = "flat", background = "white")
	ttk.Style().configure("TNotebook", background = "white", bd = 0, height = 15)
	ttk.Style().configure("TNotebook.Tab", background = "#272822", width = 15, padding = 5, foreground = "red")

	#padding
	padding_top = Frame(root, height = 1, bg = "#D0D0D0")
	padding_top.pack(side = "top", fill = "x", anchor = "n")

	#info for text area
	global InfoFrame, Line_info;
	InfoFrame = Frame(root, bg = "#c6c6c6", height = 24, padx = 5, pady = 3)
	InfoFrame.pack_propagate(0)
	InfoFrame.pack(side = BOTTOM, fill = "x")

	Line_info = Label(InfoFrame, text = "Line ", bg = "#c6c6c6", fg = "black", font = ("verdana", 10))
	Line_info.pack(anchor = "nw")

	global scrollbar;
	scrollbar = ttk.Scrollbar(orient = 'vertical')
	scrollbar.pack(side = "right", fill = "y")

	global scrollbar2;
	scrollbar2 = ttk.Scrollbar(orient = 'horizontal')
	scrollbar2.pack(side = "bottom", fill = "x", anchor = SW)

	"""#line numbers
	global Line_numbers, line_number;
	line_numbers_main = Canvas(root, width = 30, bg = "#0b082e", yscrollcommand = scrollbar.set, confine = False, relief = RAISED, highlightcolor = "#0b082e")
	line_numbers_main.pack_propagate(0)
	line_numbers_main.pack(side = "left", fill = "y")

	line_number = Label(line_numbers_main, text = "test", bg = "#0b082e", fg = "white", pady = 3, font = ("arial", 12))
	line_number.pack()"""

	#text area 	#272822
	global text_area;
	text_area = Text(root, bd = 0, font = ("arial", 12), yscrollcommand = scrollbar.set, wrap = NONE, xscrollcommand = scrollbar2.set, bg = "#272822", fg = "white", insertbackground = "white", highlightthickness = 0, padx = 0, pady = 0, relief = FLAT, selectbackground = "#32322a", selectforeground = "white", tabs = 28)
	text_area.pack(fill = "both", expand = 1)
	text_area.bind("<Button-3>", rightclick_menu_activate)
	text_area.tag_configure("current_line", background = "#383830")
	highlight_current_line()
	countlines()

	scrollbar.config(command = text_area.yview)
	scrollbar2.config(command = text_area.xview)
	root.config(menu = menubar)
	root.bind_all('<Control-n>', lambda e: file_operations("NA", "new file", "NA", "no"))
	root.bind_all('<Control-N>', lambda e: file_operations("NA", "new file", "NA", "no"))
	root.bind_all('<Control-o>', lambda e: file_operations("NA", "open file", "NA", "no"))
	root.bind_all('<Control-O>', lambda e: file_operations("NA", "open file", "NA", "no"))
	root.bind_all('<Control-s>', lambda e: file_operations("NA", "save file", "save", "no"))
	root.bind_all('<Control-S>', lambda e: file_operations("NA", "save file", "save", "no"))
	root.bind_all('<Control-Shift-s>', lambda e: file_operations("NA", "save file", "save as", "no"))
	root.bind_all('<Control-Shift-S>', lambda e: file_operations("NA", "save file", "save as", "no"))
	"""
	root.bind_all('<Control-m>', menu_visible)
	root.bind_all('<Control-M>', menu_visible)
	"""
	root.bind_all('<Control-a>', lambda e: text_area.tag_add(SEL, "1.0", END))
	root.bind_all('<Control-A>', lambda e: text_area.tag_add(SEL, "1.0", END))
	root.bind_all("<Button-1>", rightclick_menu_release)
	file_operations("NA", "new file", "NA", "no")

	root.mainloop()

def highlight_current_line(interval = 50):
	"""
	gives the current line a different background
	"""
	text_area.tag_remove("current_line", 1.0, "end")
	text_area.tag_add("current_line", "insert linestart", "insert lineend+1c")
	text_area.after(interval, highlight_current_line)

def countlines(interval = 50):
    line, column = text_area.index('insert').split('.')
    Line_info.config(text = "Line %s, column %s" % (line, column))
    text_area.after(interval, countlines)

"""def lineCount(interval = 50):
	line, column = text_area.index('insert').split('.')
	int(line)

	i = 0
	line_count = ""
	while i < int(line):
		line_count += str(int(i) + 1) + "\n"
		i += 1

	line_number.config(text = line_count)
	text_area.after(interval, lineCount)"""

def menu_visible(event):
	#shows or hides the menu bar
	menuon = 1

	if menuon == 1:
		root.config(menu = "")
		menuon = 0

	else:
		root.config(menu = menubar)
		menuon = 1

def file_operations(event, operation, savetype, close):
	global new_file_check, file_to_open, File;

	if operation == "new file":
		#creates new file
		text_area.delete(1.0, END)
		root.title("untitled ~ M-Text")
		File = ""

	elif operation == "open file":
		#opens files
		File = askopenfilename()

		try:
			root.title("%s ~ M-Text" % File)
			file_to_open = open(File, "r")
			data = file_to_open.read()
			text_area.delete(0.0, END)
			text_area.insert(INSERT, data)
			file_to_open.close()

		except IOError:
			pass

	elif operation == "save file":
		#saves files - also checks wheather the user is trying to save a new file
		if savetype == "save" and len(File) != 0:
			try:
				file_to_save = open(File, "w")
				data_to_write = text_area.get("1.0", END)
				file_to_save.write(data_to_write)
				file_to_save.close()

				if close == "yes":
					root.destroy()

				else:
					pass

			except IOError:
				pass

		elif savetype == "save as" or len(File) == 0:
			try:
				saveas_name = asksaveasfilename()
				save_to_file = open(saveas_name, "w")
				data_to_write = text_area.get("1.0", END)
				save_to_file.write(data_to_write)
				save_to_file.close()
				File = saveas_name
				root.title("%s ~ M-Text" % saveas_name)

				if close == "yes":
					root.destroy()

				else:
					pass

			except IOError:
				pass

	else:
		pass

global close_options;
def close_options():
	#asks the users if they would like to save, not save or cancel on close
	"""
	close_root = Toplevel()
	close_root.title("Save Changes Made?")
	padd_x = (close_root.winfo_screenwidth() - 620) / 2
	padd_y = (close_root.winfo_screenheight() - 300) / 2
	close_root.geometry("620x120+%s+%s" % (padd_x, padd_y))
	close_root.resizable(0, 0)
	close_root.config(bg = "#ededed")

	#frames for close options
	close_top_main = Frame(close_root, width = 600, height = 70, bg = "#ededed")
	close_top_main.pack_propagate(0)
	close_top_main.pack(side = "top")

	close_bottom_main = Frame(close_root, width = 600, height = 50, bg = "#ededed")
	close_bottom_main.pack_propagate(0)
	close_bottom_main.pack(side = "top")

	close_top_image = Frame(close_top_main, width = 140, height = 130, bg = "#ededed")
	close_top_image.pack_propagate(0)
	close_top_image.pack(side = "left")

	close_top_info = Frame(close_top_main, width = 460, height = 130, bg = "#ededed")
	close_top_info.pack_propagate(0)
	close_top_info.pack(side = "left")

	close_bottom_buttons = Frame(close_bottom_main, width = 350, height = 130, bg = "#ededed")
	close_bottom_buttons.pack_propagate(0)
	close_bottom_buttons.pack(side = "right")

	
	close_bottom_button_yes = Frame(close_bottom_buttons, width = 90, height = 130, bg = "#ededed")
	close_bottom_button_yes.pack_propagate(0)
	close_bottom_button_yes.pack(side = "left", padx = 0)

	close_bottom_button_no = Frame(close_bottom_buttons, width = 180, height = 130, bg = "#ededed")
	close_bottom_button_no.pack_propagate(0)
	close_bottom_button_no.pack(side = "left")

	close_bottom_button_cancel = Frame(close_bottom_buttons, width = 100, height = 130, bg = "#ededed")
	close_bottom_button_cancel.pack_propagate(0)
	close_bottom_button_cancel.pack(side = "left")
	
	#buttons(yes, no, cancel) for close options
	close_button_yes = Button(close_bottom_button_yes, width = 7, height = 1, text = "Save", font = ("verdana", 10), bg = "#d8d8d8", fg = "#1c1c1c", relief = "flat", activebackground = "#ededed", command = lambda: file_operations("NA", "save file", "save", "yes"))
	close_button_yes.pack(pady = 10, anchor = "e")

	close_button_no = Button(close_bottom_button_no, width = 18, height = 1, text = "Close Without Saving", font = ("verdana", 10), bg = "#d8d8d8", fg = "#1c1c1c", relief = "flat", activebackground = "#ededed", command = lambda: root.destroy())
	close_button_no.pack(pady = 10)

	close_button_cancel = Button(close_bottom_button_cancel, width = 7, height = 1, text = "Cancel", font = ("verdana", 10), bg = "#d8d8d8", fg = "#1c1c1c", relief = "flat", activebackground = "#ededed", command = lambda: close_root.destroy())
	close_button_cancel.pack(pady = 10, anchor = "w")

	#info for close options
	close_info = Label(close_top_info, text = "Would you like to save changes made?", font = ("arial", 19), fg = "#282828", bg = "#ededed")
	close_info.pack(pady = 15)

	#image for close options
	save_icon = PhotoImage(file = "save_icon.gif")
	save_image = Label(close_top_image, width = 70, height = 60, image = save_icon, bg = "#ededed")
	save_image.image = save_icon
	save_image.pack(side = "top", pady = 5)"""

"""global preferences;
def preferences():
	#font and colour options can be changed and selected from here
	#CALL A FUNCTION TO HIDE THE OTHER FRAMES AND THEN HAVE THAT FUNCTION CALL ANTOTHER FUNCTION - DEPENDING ON THE PARAMETER IT RECIEVES - THAT
	#LOADS THE MAIN FRAME AND WIDGETS FOR THE SELECTED PREFERENCE

	global pref_root;
	pref_root = Toplevel()
	pref_root.title("Preferences - Text Editor ~ M-Text")
	padd_x = (pref_root.winfo_screenwidth() - 550) / 2
	padd_y = (pref_root.winfo_screenheight() - 500) / 2
	pref_root.geometry("550x300+%s+%s" % (padd_x, padd_y))
	pref_root.resizable(0, 0)
	#pref_root.iconbitmap("@icon.xbm")

	#adds frames
	global pref_main;
	pref_container = Frame(pref_root, width = 550, height = 60, bg = "#d9d9d9")
	pref_container.pack_propagate(0)
	pref_container.pack(side = "top", fill = "x", anchor = "n")

	border_frame = Frame(pref_root, width = 550, height  = 1, bg = "black")
	border_frame.pack(side = "top", fill = "x", anchor = "n")

	pref_main = Frame(pref_root, width = 550, height = 339, bg = "#E8E8E8")
	pref_main.pack_propagate(0)
	pref_main.pack(side = "top", fill = "both", anchor = "n")

	#styling for ttk.button
	ttk.Style().configure("TButton", relief = "flat", background = "#D0D0D0", font = ("Verdana", 12))

	#loads images
	font_icon = PhotoImage(file = "font_icon.gif")
	colour_icon = PhotoImage(file = "colour_icon.gif")
	text_editor_icon = PhotoImage(file = "text_editor_icon.gif")

	#adds buttons
	text_editor_button = Button(pref_container, width = 120, image = text_editor_icon, text = "Text Editor", relief = "flat", compound = "left", command = lambda: pref_hide_widgets("text editor"))
	text_editor_button.pack(side = "left", padx = 5)

	font_button = Button(pref_container, width = 80, image = font_icon, text = "Font", compound = "left", relief = "flat", command = lambda: pref_hide_widgets("font"))
	font_button.pack(side = "left", padx = 5)

	colour_button = Button(pref_container, width = 90, image = colour_icon, text = "Colour", compound = "left", relief = "flat", command = lambda: pref_hide_widgets("colour"))
	colour_button.pack(side = "left", padx = 5)

	pref_options("font")
	pref_options("colour")
	pref_options("text editor")
	#pref_hide_widgets("text editor")
	pref_hide_widgets("colour")
	pref_root.mainloop()

def pref_options(choice):
	#options for prefs
	global pref_textEditor_main, pref_font_main, pref_colour_main;
	if choice == "text editor":
		#pref for text-editor
		pref_root.title("Preferences - Text Editor ~ M-Text")
		pref_textEditor_main = Frame(pref_main, width = 550, height = 339, bg = "red")
		pref_textEditor_main.pack_propagate(0)
		pref_textEditor_main.pack()

	elif choice == "font":
		#pref for font
		#main frame
		pref_root.title("Preferences - Font ~ M-Text")
		pref_font_main = Frame(pref_main, width = 550, height = 339, bg = "blue")
		pref_font_main.pack_propagate(0)
		pref_font_main.pack()

		#frames for font
		pref_font_familys_main = Frame(pref_font_main, width = 200, height = 339, bg = "red")
		pref_font_familys_main.pack_propagate(0)
		pref_font_familys_main.pack(side = "left")

		pref_font_size_main = Frame(pref_font_main, width = 170, height = 339, bg = "black")
		pref_font_size_main.pack_propagate(0)
		pref_font_size_main.pack(side = "left")

		pref_style_size_main = Frame(pref_font_main, width = 180, height = 339, bg = "blue")
		pref_style_size_main.pack_propagate(0)
		pref_style_size_main.pack(side = "left")


	elif choice == "colour":
		#pref for colour
		TO ADD - select colour, cursor colour
		pref_root.title("Preferences - Colour ~ M-Text")
		pref_colour_main = Frame(pref_main, width = 550, height = 339, bg = "#ededed")
		pref_colour_main.pack_propagate(0)
		pref_colour_main.pack()

		#frames for colour options(bg, fg, lc, sc and cc)
		pref_colour_row1_main = Frame(pref_colour_main, width = 550, height = 60, bg = "#edeaea")
		pref_colour_row1_main.pack_propagate(0)
		pref_colour_row1_main.pack(side = "top", anchor = "n")

		pref_colour_row2_main = Frame(pref_colour_main, width = 550, height = 50, bg = "#edeaea")
		pref_colour_row2_main.pack_propagate(0)
		pref_colour_row2_main.pack(side = "top", anchor = "n")

		pref_colour_row3_main = Frame(pref_colour_main, width = 550, height = 50, bg = "#edeaea")
		pref_colour_row3_main.pack_propagate(0)
		pref_colour_row3_main.pack(side = "top", anchor = "n")

		#row 1
		pref_colour_row1_col1_main = Frame(pref_colour_row1_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row1_col1_main.pack_propagate(0)
		pref_colour_row1_col1_main.pack(side = "left", anchor = "s")

		pref_colour_row1_col2_main = Frame(pref_colour_row1_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row1_col2_main.pack_propagate(0)
		pref_colour_row1_col2_main.pack(side = "left", anchor = "s")

		pref_colour_row1_col3_main = Frame(pref_colour_row1_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row1_col3_main.pack_propagate(0)
		pref_colour_row1_col3_main.pack(side = "left", anchor = "s")

		pref_colour_row1_col4_main = Frame(pref_colour_row1_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row1_col4_main.pack_propagate(0)
		pref_colour_row1_col4_main.pack(side = "left", anchor = "s")

		#row 2
		pref_colour_row2_col1_main = Frame(pref_colour_row2_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row2_col1_main.pack_propagate(0)
		pref_colour_row2_col1_main.pack(side = "left", anchor = "s")

		pref_colour_row2_col2_main = Frame(pref_colour_row2_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row2_col2_main.pack_propagate(0)
		pref_colour_row2_col2_main.pack(side = "left", anchor = "s")

		pref_colour_row2_col3_main = Frame(pref_colour_row2_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row2_col3_main.pack_propagate(0)
		pref_colour_row2_col3_main.pack(side = "left", anchor = "s")

		pref_colour_row2_col4_main = Frame(pref_colour_row2_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row2_col4_main.pack_propagate(0)
		pref_colour_row2_col4_main.pack(side = "left", anchor = "s")

		#row 3
		pref_colour_row3_col1_main = Frame(pref_colour_row3_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row3_col1_main.pack_propagate(0)
		pref_colour_row3_col1_main.pack(side = "left", anchor = "s")

		pref_colour_row3_col2_main = Frame(pref_colour_row3_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row3_col2_main.pack_propagate(0)
		pref_colour_row3_col2_main.pack(side = "left", anchor = "s")

		pref_colour_row3_col3_main = Frame(pref_colour_row3_main, width = 174, height = 50, bg = "#edeaea")
		pref_colour_row3_col3_main.pack_propagate(0)
		pref_colour_row3_col3_main.pack(side = "left", anchor = "s")

		pref_colour_row3_col4_main = Frame(pref_colour_row3_main, width = 100, height = 50, bg = "#edeaea")
		pref_colour_row3_col4_main.pack_propagate(0)
		pref_colour_row3_col4_main.pack(side = "left", anchor = "s")

		global pref_colour_row1_col2_bg_button, pref_colour_row1_col4_fg_button, pref_colour_row2_col2_lc_button, pref_colour_row3_col2_ic_button, pref_colour_row2_col4_sb_button, pref_colour_row3_col4_sf_button;

		#row 1 - column 1
		pref_colour_row1_col1_bg_text = Label(pref_colour_row1_col1_main, text = "Background Colour:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row1_col1_bg_text.pack(side = "left", padx = 10)

		#row 1 - column 2
		pref_colour_row1_col2_bg_button = Button(pref_colour_row1_col2_main, width = 5, relief = "flat", command = lambda: colorChanger("bg"))
		pref_colour_row1_col2_bg_button.pack(side = "left", padx = 10)

		#row 1 - column 3
		pref_colour_row1_col3_fg_text = Label(pref_colour_row1_col3_main, text = "Foreground Colour:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row1_col3_fg_text.pack(side = "left", padx = 10)

		#row 1 - column 4
		pref_colour_row1_col4_fg_button = Button(pref_colour_row1_col4_main, width = 5, relief = "flat", command = lambda: colorChanger("fg"))
		pref_colour_row1_col4_fg_button.pack(side = "left", padx = 10)

		#row 2 - column 1
		pref_colour_row2_col1_lc_text = Label(pref_colour_row2_col1_main, text = "Line Colour:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row2_col1_lc_text.pack(side = "left", padx = 10)

		#row 2 - column 2
		pref_colour_row2_col2_lc_button = Button(pref_colour_row2_col2_main, width = 5, relief = "flat", command = lambda: colorChanger("lc"))
		pref_colour_row2_col2_lc_button.pack(side = "left", padx = 10)

		#row 2 - column 3
		pref_colour_row2_col3_sb_text = Label(pref_colour_row2_col3_main, text = "Selection Background:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row2_col3_sb_text.pack(side = "left", padx = 10)

		#row 2 - column 4
		pref_colour_row2_col4_sb_button = Button(pref_colour_row2_col4_main, width = 5, relief = "flat", command = lambda: colorChanger("sb"))
		pref_colour_row2_col4_sb_button.pack(side = "left", padx = 10)

		#row 3 - column 1
		pref_colour_row3_col1_ic_text = Label(pref_colour_row3_col1_main, text = "Insert Colour:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row3_col1_ic_text.pack(side = "left", padx = 10)

		#row 3 - column 2
		pref_colour_row3_col2_ic_button = Button(pref_colour_row3_col2_main, width = 5, relief = "flat", command = lambda: colorChanger("ic"))
		pref_colour_row3_col2_ic_button.pack(side = "left", padx = 10)

		#row 3 - column 3
		pref_colour_row3_col3_sf_text = Label(pref_colour_row3_col3_main, text = "Selection Foreground:", font = ("arial", 11), fg = "gray", bg = "#edeaea")
		pref_colour_row3_col3_sf_text.pack(side = "left", padx = 10)

		#row 3 - column 4
		pref_colour_row3_col4_sf_button = Button(pref_colour_row3_col4_main, width = 5, relief = "flat", command = lambda: colorChanger("sf"))
		pref_colour_row3_col4_sf_button.pack(side = "left", padx = 10)

	else:
		pass

def colorChanger(choice):
	rgb_colour, hex_colour = askcolor()

	if choice == "bg":
		pref_colour_row1_col2_bg_button.config(bg = hex_colour)
		pref_colour_row1_col2_bg_button.config(activebackground = hex_colour)

		text_area.config(bg = hex_colour)

	elif choice == "fg":
		pref_colour_row1_col4_fg_button.config(bg = hex_colour)
		pref_colour_row1_col4_fg_button.config(activebackground = hex_colour)

		text_area.config(fg = hex_colour)
		text_area.config(selectforeground = hex_colour)

	elif choice == "lc":
		pref_colour_row2_col2_lc_button.config(bg = hex_colour)
		pref_colour_row2_col2_lc_button.config(activebackground = hex_colour)

		text_area.tag_configure("current_line", background = hex_colour)

	elif choice == "sb":
		pref_colour_row2_col3_sb_button.config(bg = hex_colour)
		pref_colour_row2_col3_sb_button.config(activebackground = hex_colour)

		text_area.config(selectbackground = hex_colour)

	elif choice == "sf":
		pref_colour_row3_col4_sf_button.config(bg = hex_colour)
		pref_colour_row3_col4_sf_button.config(activebackground = hex_colour)

		text_area.config(selectforeground = hex_colour)

	elif choice == "ic":
		pref_colour_row3_col2_ic_button.config(bg = hex_colour)
		pref_colour_row3_col2_ic_button.config(activebackground = hex_colour)

		text_area.config(insertbackground = hex_colour)

	else:
		pass

def pref_hide_widgets(choice):
	pref_textEditor_main.pack_forget()
	pref_font_main.pack_forget()
	pref_colour_main.pack_forget()

	if choice == "text editor":
		pref_options(choice)

	elif choice == "font":
		pref_options(choice)

	elif choice == "colour":
		pref_options(choice)

	else:
		pass"""

main_window()
#preferences()