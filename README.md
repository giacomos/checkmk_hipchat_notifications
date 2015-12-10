# CheckMK - HipChat Notification

This plugin for CheckMK let's you send notification to HipChat.
Underneath it uses the python library [hipsaint](https://github.com/hannseman/hipsaint).

## Installation
 This package can be installed by placing the "hipchat.mkp" package in the
root of your checkmk site. For ex.:

    /opt/omd/sites/<mymonitor>/hipchat.mkp

Then login in as the user which is running the site:

    $ sudo su mymonitor

And finally install it
    
    OMD[mymonitor]:~$ check_mk -vP install hipchat.mkp

Now we can create the new notification settings, by going to the CheckMK
interface, and navigating to "WATO" -> "Notifications" -> "New Rule"

![Screenshot](https://raw.githubusercontent.com/giacomos/checkmk_hipchat_notifications/master/screenshot.png)
