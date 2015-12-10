# CheckMk - HipChat Notification

This plugin for CheckMk let's you send notification to HipChat.
Underneath it uses the python library hipsaint (https://github.com/hannseman/hipsaint).

## Installation
 This package can be installed by placing the "hipchat.mkp" package in the
root of your checkmk site. For ex. /opt/omd/sites/<mymonitor>/hipchat.mkp

Then login in as the user which is running the site:

    sudo su mymonitor

And finally install it
    
    check_mk -vP install hipchat.mkp
