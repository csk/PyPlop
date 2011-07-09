#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import gtk
import re
    
class Plop:

    def _get_username(self):
        self.p = os.popen("who|grep ':0'")
        self.cmd_output = self.p.readline()
        self.p.close()
        return self.cmd_output.split(" ")[0]

    def _get_fullname(self):
        self.p = os.popen("getent passwd " + self._get_username())
        self.cmd_output = self.p.readline()
        return self.cmd_output.split(":")[4]

    def _get_hostname(self):
        self.p = os.popen("hostname ")
        self.cmd_output = self.p.readline()
        return self.cmd_output

    def on_window_destroy(self, widget, data=None):
        gtk.main_quit()
     
    def unlock(self, widget, data=None):
        if len(data[0].get_text()) <= 4 :
            data[1].set_label(u"Contraseña incorrecta.")
        else:
            print self._get_username()        
            print data[0].get_text()        
            gtk.main_quit()
     
    def __init__(self):
    
        builder = gtk.Builder()
        builder.add_from_file("blocked.glade") 
        
        self.color = gtk.gdk.Color(red=0, green=0, blue=0, pixel=0)
        self.window0 = builder.get_object("window0")
        self.window0.modify_bg (gtk.STATE_ACTIVE, self.color);
        self.window0.modify_bg (gtk.STATE_NORMAL, self.color);
        self.window0.modify_bg (gtk.STATE_SELECTED, self.color);
        self.window0.modify_bg (gtk.STATE_PRELIGHT, self.color);
        self.window0.modify_bg (gtk.STATE_INSENSITIVE, self.color);

        imagename = "/usr/share/backgrounds/laughlin/default/standard/laughlin.png"
        pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(imagename, \
                gtk.gdk.screen_width(), \
                gtk.gdk.screen_height()) 
        pixmap, mask = pixbuf.render_pixmap_and_mask() 
        image = gtk.Image()
        image.set_from_pixmap(pixmap, mask)
        image.show()
        self.window0.add(image)
        self.window0.fullscreen()

        self.label0 = builder.get_object("label_fullname")
        self.label1 = builder.get_object("label_user_on_host")
        self.label2 = builder.get_object("label_err")

        self.label0.set_label(self._get_fullname())
        self.label1.set_label(self._get_username() + " on " + self._get_hostname())
        self.entry = builder.get_object("entry_password")
        self.button = builder.get_object("button_unlock")
        self.button.connect("clicked", self.unlock, [self.entry, self.label2])
        self.window1 = builder.get_object("window1")
        builder.connect_signals(self)       
    
if __name__ == "__main__":
    editor = Plop()
    editor.window0.show()
    editor.window1.show()
    gtk.main()

