shit-talk
=========

Fork of Shawn McCool's [shit talk] (https://github.com/ShawnMcCool/shit-talk)

## Dependencies
- bash
- jq
- python3
- Google Api key (look below)

## Before using
1. Get an apy key and put in the directory of the script. Filename should be `key.txt`
2. Copy `commands.json` in `$HOME/.config/shit-talk/`
3. If you don't, create the directory `~/.cache`

## How to use
1. Start the script `record` to start recording and then again to stop recording an analyze the recording.



### to get an api key
From [ORlON](https://gist.github.com/ORlON)'s [post](https://gist.github.com/alotaiba/1730160#comment-1230466). 

- Go to this link : https://cloud.google.com/console and create your own project.
- Join this group here : https://groups.google.com/a/chromium.org/forum/?fromgroups#!forum/chromium-dev.
- In your project go to APIs & auth > APIs , and activate Speech API (only 50 requests for each key).
- Go to Credentials and make your client.
- Generate a Browser key.
