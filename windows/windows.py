# This module provide the classes for the clock-window
# and the window for the alarm.

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Gdk

from datetime import datetime

start_time = '21:26:00' # Ora di inizio del giornale radio
stop_time = '21:30:00' # Ora di fine del giornale radio


class NewsAlarm(Gtk.Window):
    
   def __init__(self):

      Gtk.Window.__init__(self,title='Timer') # Call the Gtk.Window constructor 
      self.set_name('AlarmWindow')
      self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1) 
      self.message = Gtk.Label('Il radiogiornale cominciera` in:')
      self.message.set_line_wrap(True)
      self.timer = Gtk.Label('') # Container for the countdown
      self.timer.set_name('Countdown')
      self.vbox.pack_start(self.message, True, True, 0) 
      self.vbox.pack_start(self.timer, True, True, 0) # Put the labels inside the container vbox
      self.add(self.vbox) # Put the box inside the window
      self.connect('delete-event', Gtk.main_quit) # Connect the termination function to the event 
                                                  # of deletion of the window
      self.show_all() # Make visible the window and every element it contains
      self.setTimeLabel()
      GLib.timeout_add(500,self.setTimeLabel) # Refresh the window every half second

   def setTimeLabel(self):

      now = datetime.today()
      day_info = str(now).split(' ')[0] # extract the date part
      newscast_start = datetime.strptime(day_info+' '+start_time,'%Y-%m-%d %H:%M:%S')
      newscast_end = datetime.strptime(day_info+' '+stop_time,'%Y-%m-%d %H:%M:%S')
      delta = newscast_start-now
      timer = (str(delta).split('.')[0]).split(':',1)[1]
      if delta.total_seconds() >= 0:
         self.timer.set_text('-'+timer)
         return True
      else:
         self.message.set_text('Il radiogiornale finira` in:')
         delta = newscast_end-now # If we arrive here then newscast is already started
         timer = (str(delta).split('.')[0]).split(':',1)[1]
         if delta.total_seconds() >= 0:
            self.timer.set_text('-'+timer)
            return True
         else: 
            self.close()
            return False




