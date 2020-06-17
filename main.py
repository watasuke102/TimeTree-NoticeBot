#!/usr/bin/env python
#coding:utf-8
import timetree
import discord
from discord.ext  import tasks
from datetime     import datetime

# トークン等の読み込み
with open('settings', 'r') as file:
	token      = file.readline()
	channelID  = file.readline()
	keyAPI     = file.readline()
	calenderID = file.readline()
	# 改行の削除
	token     =''.join(token     .split())
	channelID =''.join(channelID .split())
	keyAPI    =''.join(keyAPI    .split())
	calenderID=''.join(calenderID.split())

# TimeTree APIの設定
timetree.keyAPI     = keyAPI
timetree.calenderID = calenderID

# 接続用オブジェクト生成
client = discord.Client()


# 1分ごとに更新
@tasks.loop(minutes=1)
async def loop():
	channel = client.get_channel(int(channelID))
	# 現在時刻を取得
	now = datetime.now().strftime('%H:%M')
	# 8時ならおはようする
	# デバッグのため時間を変えてる
	if now == '08:00':
		await channel.send(timetree.getTodaysEvents())


loop.start()
client.run(token)
