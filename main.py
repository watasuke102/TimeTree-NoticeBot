#!/usr/bin/env python
import discord
from discord.ext import tasks
from datetime import datetime
from timetree_sdk import TimeTreeApi

# トークンの読み込み
file       = open('settings')
token      = file.readline()
channelID  = file.readline()
keyAPI     = file.readline()
calenderID = file.readline()
file.close()

print('token: '            + token    )
print('channel: '          + channelID)
print('TimeTree API Key: ' + keyAPI   )
print('Read Settings...Done')

# TimeTree APIの設定
api      = TimeTreeApi(keyAPI)
#calender = api.get_calendar(calenderID)
#print(calender.data.attributes.name)

# 接続用オブジェクト生成
client  = discord.Client()
print('Create Client...Done')

@client.event
async def on_ready():
	channel = client.get_channel(int(channelID))
	await channel.send('起動しました')

# 10分ごとに更新
# 今はテスト用に10秒ごとにしている
@tasks.loop(seconds=10)
async def loop():
	print('Begin of the loop')
	channel = client.get_channel(int(channelID))
	await channel.send('こんにちは(send this every 10s)')
	print('End of the loop')

loop.start()
print('Running client...')
client.run(token)
