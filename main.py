#!/usr/bin/env python
import discord

# トークンの読み込み
file = open('settings')
TOKEN = file.readline()
CHANNEL = file.readline()
file.close()