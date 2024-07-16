# Linux-Recall-in-bash

RECALL Functionality for Linux Desktops in Bash 

# What it does

Recall will take a screenshot, if no excluded window is open, every 30 seconds and stores the image into your choosen Image path.
It will use tesseract to OCR the image content and store it in a txt file in the same directory.

If the size of the directory is > 10G it starts deleting the oldest image. 
If a textfile is older than 180 days they will be deleted too.

If you wanne have a different timeframe or different volume, you need to change the "recall" script (for now).

# Dependencies:

- flameshot
- tesseract
- zenity
- eyeofgnome
- wmctrl
- systemd
- ImageMagick / GraphicsMagic
- gtts (optional)
- notify-send
- python for trayicon

# How to Install it for Fedora

Install this [Repo](http://repo.linux-am-dienstag.de/pva.repo) i.e. by 

```
curl -L http://repo.linux-am-dienstag.de/pva.repo > /etc/yum.repos.d/linuxamdienstag.repo
dnf makecache
dnf install recall
```


# How to Install it manually

```
mv recall recall-* to /usr/sbin/
chmod 700 /usr/sbin/recall*
mv recall.desktop /usr/share/applications/
```

```
mv recall.timer and recall.service to /lib/systemd/user/
mv 97-recall.preset to /lib/systemd/user-preset/
```

edit .config/recall/config to the path you want the recall images saved, adjust the timeframe for caching and max. cachesize.
change or edit .config/recall/exclude to either a completly empty file or add line-by-line the windowtitles from wmctrl -l i.e.

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

Finally, start the Desktop TrayIcon APP and start up Recall from there:

- active Recall: means, you enable it permanently and start it up.
- start Recall: means, you just start it "for now" without automatic starts in the future.

Please remember: if it's not running, it does not record anything you can "recall" ;)


# Integrations

This project is now integrated into the Personal Voice Assistant (PVA) aka Carola. PVA is available in the same user repo or via precompiled RPM files for Fedora.


# Acknowledgments

This project was done while the [Linux am Dienstag](https://linux-am-dienstag.de) videoconference on 11.6.2024 just for fun and pleasure. 

This project is 100% local, it does not store or process files in any cloud service.
