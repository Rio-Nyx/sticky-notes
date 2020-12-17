import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")

		self.text = Gtk.TextView()
		self.add(self.text)

	def on_button_clicked(self, widget):
		print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
