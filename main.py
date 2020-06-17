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

print('token: '            + token     )
print('channel: '          + channelID )
print('TimeTree API Key: ' + keyAPI    )
print('calender ID: '      + calenderID)
print('> Read Settings from file...Done')

# TimeTree APIの設定
timetree.keyAPI     = keyAPI
timetree.calenderID = calenderID
print('---EVENTS---')
timetree.getTodaysEvents()
print('---EVENTS END---')

# 接続用オブジェクト生成
client  = discord.Client()
print('> Create client...Done')


# 10分ごとに更新
# 今はテスト用に30秒ごとにしている
@tasks.loop(seconds=30)
async def loop():
	print('-- Begin of the loop --')
	channel = client.get_channel(int(channelID))
	print('  > Get Channel...Done')
	# 現在時刻を取得
	now = datetime.now().strftime('%H:%M')
	print('  > Get time...Done\nnow: ' + now)
	# 8時ならおはようする
	# デバッグのため時間を変えてる
	if now == '13:11':
		print('NOW')
		await channel.send('おはよう')
	print('-- End of the loop --\n')


loop.start()
print('\n---RUNNNING CLIENT---\n')
client.run(token)
