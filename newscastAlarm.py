#! /usr/bin/python

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Gdk

import time

from windows.windows import NewsAlarm

window = NewsAlarm() # Create the window

provider = Gtk.CssProvider() # This object will serve to load the appearance property
display = Gdk.Display.get_default() 
screen = display.get_default_screen()

provider.load_from_data(b"""
#AlarmWindow {
background-color: #8F0000;
color: white;
}
GtkLabel {
font-size: 8ex;
padding: 10px;
color: white;
}
#Countdown {
font-size: 8em;
}
""")

# Next we tell the screen to use the appearance described in the provider
Gtk.StyleContext.add_provider_for_screen(screen,provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

Gtk.main() # Start the Gtk loop engine

