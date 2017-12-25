import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import sys
import os
from time import sleep
from threading import Thread

class LoadingIndicator(Gtk.Box):
    def __init__(self, body):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.set_spacing(10)

        spinner = Gtk.Spinner()
        spinner.start()
        self.pack_start(spinner, False, False, 20)

        label = Gtk.Label(xalign=0)
        label.set_markup("{}".format(body))
        self.pack_start(label, True, True, 0)

def call_function_and_quit(function, loop):
    function()
    loop.quit()

def show_loading_indicator(title, body, function):
    loop = GLib.MainLoop()

    win = Gtk.Window()
    win.set_default_size(600,100)
    win.set_position(Gtk.WindowPosition.CENTER)
    win.set_resizable(False)
    win.set_deletable(False)
    win.set_title(title)
    win.set_border_width(20)

    loading = LoadingIndicator(body)
    win.add(loading)

    win.show_all()

    thread = Thread(target=call_function_and_quit, args=(function, loop))
    thread.start()

    loop.run()
