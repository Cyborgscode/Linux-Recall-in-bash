#!/usr/bin/python

import os
import gi
import sys

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

restart = 1
indicator = appindicator.Indicator.new("customtray", "gtk-media-pause", appindicator.IndicatorCategory.APPLICATION_STATUS)

def main():
  global indicator  
  while restart == 1:
#    print('Looping start')
    status = os.system("systemctl --user is-active recall.timer 2>/dev/null")
#    print("status=" + str(status))
    if status != 0:
      indicator = appindicator.Indicator.new("customtray", "gtk-media-pause", appindicator.IndicatorCategory.APPLICATION_STATUS)
      indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
      indicator.set_menu(startmenu())
    else:
      indicator = appindicator.Indicator.new("customtray", "gtk-media-record", appindicator.IndicatorCategory.APPLICATION_STATUS)
      indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
      indicator.set_menu(stopmenu())
  
    gtk.main()
    
  print('App beendet')

def startmenu():
  menu = gtk.Menu()
  label = gtk.Label("Recall")    
  menu.add(label)

  command_one = gtk.MenuItem('Recall starten')
  command_one.connect('activate', start)
  menu.append(command_one)

  return basemenu(menu)

def stopmenu():
  menu = gtk.Menu()
 
  command_one = gtk.MenuItem('Recall beenden')
  command_one.connect('activate', kill)
  menu.append(command_one)

  return basemenu(menu)

def basemenu(menu):

  status = os.system("systemctl --user is-enabled recall.timer 2>/dev/null")
  if status != 0:
    command_er = gtk.MenuItem('aktiviere Recall')
    command_er.connect('activate', enablerecall)
    menu.append(command_er)
  else:
    command_dr = gtk.MenuItem('deaktiviere Recall')
    command_dr.connect('activate', disablerecall)
    menu.append(command_dr)

  command_cc = gtk.MenuItem('Cache löschen')
  command_cc.connect('activate', cacheclr)
  menu.append(command_cc)

  command_cs = gtk.MenuItem('Cache Status')
  command_cs.connect('activate', cachestatus)
  menu.append(command_cs)

  command_search = gtk.MenuItem('Suchen')
  command_search.connect('activate', search)
  menu.append(command_search)

  exittray = gtk.MenuItem('Tray beenden')
  exittray.connect('activate', quit)
  menu.append(exittray)

  menu.show_all()
  return menu

def start(_):
  global indicator
  os.system("systemctl --user start recall.timer")
#  os.system("systemctl --user enable recall.timer")
  indicator.set_menu(stopmenu())
  gtk.main_quit()
  
def kill(_):
  global indicator
  os.system("systemctl --user stop recall.timer")
#  os.system("systemctl --user disable recall.timer")
  indicator.set_menu(startmenu())
  gtk.main_quit()

def cacheclr(_):
  os.system("/usr/sbin/recall-cache-clear")

def cachestatus(_):
  os.system("/usr/sbin/recall-cache-status")
  
def enablerecall(_):
  os.system("systemctl --user enable --now recall.timer")
  gtk.main_quit()
  
def disablerecall(_):
  os.system("systemctl --user disable recall.timer")
  gtk.main_quit()

def search(_):
  os.system("/usr/sbin/recall-ui")

def quit(_):
  global restart
  restart = 0
  gtk.main_quit()
  

if __name__ == "__main__":
  main()
