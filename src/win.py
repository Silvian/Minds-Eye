#!/usr/bin/python
from gi.repository import Gtk

class mainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Minds-Eye")

		self.button = Gtk.Button(label="Click Here!")
		self.button.connect = ("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):
		print("Hello World")

win = mainWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
