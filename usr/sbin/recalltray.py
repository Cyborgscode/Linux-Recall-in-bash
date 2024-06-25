#!/usr/bin/python

import os
import gi
import sys

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

indicator = appindicator.Indicator.new("customtray", "gtk-media-record", appindicator.IndicatorCategory.APPLICATION_STATUS)
indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

def main():

  status = os.system("systemctl --user is-active recall.timer")
  if status == 1:
    indicator.set_menu(menu1())
  else:
    indicator.set_menu(menu2())
  
  gtk.main()

def menu1():
  menu = gtk.Menu()
 
  command_one = gtk.MenuItem('Recall starten')
  command_one.connect('activate', start)
  menu.append(command_one)

  command_drei = gtk.MenuItem('Suchen')
  command_drei.connect('activate', search)
  menu.append(command_drei)

  command_two = gtk.MenuItem('Cache clear')
  command_two.connect('activate', cacheclr)
  menu.append(command_two)

  command_vier = gtk.MenuItem('Cache Status')
  command_vier.connect('activate', cachestatus)
  menu.append(command_vier)

  exittray = gtk.MenuItem('Tray beenden')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def menu2():
  menu = gtk.Menu()
 
  command_one = gtk.MenuItem('Recall beenden')
  command_one.connect('activate', kill)
  menu.append(command_one)

  command_drei = gtk.MenuItem('Suchen')
  command_drei.connect('activate', search)
  menu.append(command_drei)

  command_two = gtk.MenuItem('Cache clear')
  command_two.connect('activate', cacheclr)
  menu.append(command_two)

  command_vier = gtk.MenuItem('Cache Status')
  command_vier.connect('activate', cachestatus)
  menu.append(command_vier)

  exittray = gtk.MenuItem('Tray beenden')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu

def start(_):
  os.system("systemctl --user start recall.timer")
  indicator.set_menu(menu2())

def kill(_):
  os.system("systemctl --user stop recall.timer")
  indicator.set_menu(menu1())

def cacheclr(_):
  os.system("/usr/sbin/recall-cache-clear")

def cachestatus(_):
  os.system("/usr/sbin/recall-cache-status")

def search(_):
  os.system("/usr/sbin/recall-ui")

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
