WiFi Door Unlock Server
=======================

This is a [Heroku](http://www.heroku.com/)-ready webapp for sending control
messages to a subscribed [Pusher](http://pusher.com/) client.

My primary use is to control an arduino powered servo for unlocking a door.

Usage
=====

If you have the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed,
installation of this app should be as easy as:

1. ``virtualenv venv --distribute``
2. ``pip install -r requirements.txt``
3. ``foreman start``