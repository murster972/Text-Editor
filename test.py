import gtk

class TabLabel(gtk.Box):
    __gsignals__ = {
        "close-clicked": (GObject.SIGNAL_RUN_FIRST, GObject.TYPE_NONE, ()),
    }
    def __init__(self, label_text):
        gtk.Box.__init__(self)
        self.set_orientation(gtk.Orientation.HORIZONTAL)
        self.set_spacing(5) # spacing: [icon|5px|label|5px|close]  
        
        # icon
        icon = gtk.Image.new_from_stock(gtk.STOCK_FILE, gtk.IconSize.MENU)
        self.pack_start(icon, False, False, 0)
        
        # label 
        label = gtk.Label(label_text)
        self.pack_start(label, True, True, 0)
        
        # close button
        button = gtk.Button()
        button.set_relief(gtk.ReliefStyle.NONE)
        button.set_focus_on_click(False)
        button.add(gtk.Image.new_from_stock(gtk.STOCK_CLOSE, gtk.IconSize.MENU))
        button.connect("clicked", self.button_clicked)
        data =  ".button {\n" \
                "-gtkButton-default-border : 0px;\n" \
                "-gtkButton-default-outside-border : 0px;\n" \
                "-gtkButton-inner-border: 0px;\n" \
                "-gtkWidget-focus-line-width : 0px;\n" \
                "-gtkWidget-focus-padding : 0px;\n" \
                "padding: 0px;\n" \
                "}"
        provider = gtk.CssProvider()
        provider.load_from_data(data)
        # 600 = gtk_STYLE_PROVIDER_PRIORITY_APPLICATION
        button.get_style_context().add_provider(provider, 600) 
        self.pack_start(button, False, False, 0)
        
        self.show_all()
    
    def button_clicked(self, button, data=None):
        self.emit("close-clicked")

def on_close_clicked(tab_label, notebook, tab_widget):
    """ Callback for the "close-clicked" emitted by custom TabLabel widget. """
    notebook.remove_page(notebook.page_num(tab_widget))

if __name__ == "__main__":
    notebook = gtk.Notebook()
    for x in xrange(1, 4):
        tab_widget = gtk.TextView()
        tab_label = TabLabel("Page %d" % x)
        tab_label.connect("close-clicked", on_close_clicked, notebook, tab_widget)
        notebook.append_page(tab_widget, tab_label)
          
    window = gtk.Window(title="gtk.Notebook Close Buttons")
    window.set_default_size(350, 200)
    window.connect("destroy", lambda w: gtk.main_quit())
    window.add(notebook)
    window.show_all()

    gtk.main()
