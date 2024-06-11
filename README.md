# Linux-Recall-in-bash

RECALL Functionality for Linux Desktops in Bash 

# What it does

Recall will take a screenshot, if no excluded window is open, every 10 seconds and stores the image into your choosen Image path.
It will use tesseract to OCR the image content and store it in a txt file in the same directory.

If the size of the directory is > 1G it starts deleting the oldest image. 
If a textfile is older than 180 days they will be deleted too.

If you wanne have a different timeframe or different volume, you need to change the "recall" script (for now).

# Dependencies:

- flameshot
- tesseract
- zenity
- wmctrl
- systemd

# How to Install

```
mv recall and recall-ui to .local/bin/
chmod 700 .local/bin/recall*
```

mv recall.timer and recall.service to .config/systemd/user/

edit recall.service and change the username to YOUR username

edit .config/recall/path to the path you want the recall images saved.
change or edit .config/recall/exclude to either a completly empty file or add line-by-line the windowtitles form wmctrl -l i.e.

```
[~]$ wmctrl -l
0x02e00007  0 linux-am-dienstag.de Desktop
0x02e0000f  0 linux-am-dienstag.de nemo-desktop
0x0460003a  0 linux-am-dienstag.de Bugzilla - Mozilla Thunderbird
0x0200002c  0 linux-am-dienstag.de Google News – Mozilla Firefox
0x0aa00004  0 linux-am-dienstag.de Easy Effects
0x020012e3  0 linux-am-dienstag.de Firefox - Share-Notice
```

Take i.e. "Easy Effects" and "Google News – Mozilla Firefox", put them without quotation marks into the exclude file:

```
Easy Effects
Google News – Mozilla Firefox
```

save it. If any of those windows are open, and this includes firefox tabs in front, recall won't make a screenshot.

Now, this depends on your desktop, add a shortcut for the "recall-ui" app to i.e. SUPER+R , so that you can start the search request.

Finally enter "systemctl --user start recall.timer" and your ready!




