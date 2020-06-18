#!/usr/bin/env python
#coding:utf-8
import timetree
import discord
import sys
from discord.ext  import tasks
from datetime     import datetime


# コマンドライン引数に-dがあればデバッグ表示をON
# コマンドライン引数に-eがあれば@everyoneをOFF
for arg in sys.argv:
	if arg == 'main.py':
		continue
	if arg == '-d' or arg == '--debug':
		timetree.isDebugMode = True
	if arg == '-e' or arg == '--everyone-disable':
		timetree.isMentionEveryone = False


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

@client.event
async def on_ready():
	timetree.debug(timetree.getTodaysEvents())

# 1分ごとに更新
@tasks.loop(minutes=1)
async def loop():
	timetree.debug('---Begin Loop---')
	channel = client.get_channel(int(channelID))
	afterTenMinutes = timetree.getEventAfterTenMinutes()
	# 10分後に予定があれば、それを通知
	if afterTenMinutes != '':
		await channel.send(afterTenMinutes)
	# 現在時刻を取得し、8時なら予定を表示
	now = datetime.now().strftime('%H:%M')
	if now == '08:00':
		await channel.send(timetree.getTodaysEvents())
	timetree.debug('---End Loop---\n')


loop.start()
client.run(token)
