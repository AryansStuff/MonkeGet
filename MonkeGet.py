#!/usr/bin/env python

import wget
import os
import subprocess



PiDict = {
        'Discord/unixitry-bot':'https://github.com/DiscordBotCreator-png/Unixitry/archive/refs/heads/main.zip', 
        'MonkeLang/main':'https://raw.githubusercontent.com/DiscordBotCreator-png/MonkeLang/master/main.py', 
        'MonkeLang/basic':'https://raw.githubusercontent.com/DiscordBotCreator-png/MonkeLang/master/basic.py',
        'MonkeLang/all':'https://github.com/DiscordBotCreator-png/MonkeLang/archive/refs/heads/master.zip',
        'Misc/neofetch':'https://github.com/dylanaraps/neofetch/archive/refs/heads/master.zip'
        }

HLi = input('URL or Package Identifier > ')

if 'https://' in HLi:
    print("Download Started!")
    wget.download(HLi)
else:
    url = PiDict[HLi]
    print("Download Started!")
    urlname=wget.download(url)
    if '.zip' in urlname:
        os.system('unzip {urlname}'.format(urlname=urlname))
        os.system('rm -rf {urlname}'.format(urlname=urlname))
        if HLi == 'Misc/neofetch':
            os.system("echo 'Please change directory into neofetch-master, and type sudo make install.'")
        print('\n Download Complete! \n')
    else:
        print('\n Download Complete! \n')
