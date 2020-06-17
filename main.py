#!/usr/bin/env python
import discord
import timetree
from discord.ext  import tasks
from datetime     import datetime

# トークンの読み込み
file       = open('settings')
token      = file.readline()
channelID  = file.readline()
keyAPI     = file.readline()
calenderID = file.readline()
file.close()

print(
 'token: '            + token
+'channel: '          + channelID
+'TimeTree API Key: ' + keyAPI)
print('Read Settings from file...Done')

# TimeTree APIの設定
timetree.init(keyAPI)

# 接続用オブジェクト生成
client  = discord.Client()
print('Create client...Done')


# 10分ごとに更新
# 今はテスト用に30秒ごとにしている
@tasks.loop(seconds=30)
async def loop():
	print('-- Begin of the loop --')
	channel = client.get_channel(int(channelID))
	print('Get Channel...Done')
	# 現在時刻を取得
	now = datetime.now().strftime('%H:%M')
	print('Get time...Done\nnow: ' + now)
	# 8時ならおはようする
	# デバッグのため時間を変えてる
	if now == '13:11':
		print('NOW')
		await channel.send('おはよう')
	print('Send Message')
	print('-- End of the loop --\n')


loop.start()
print('\n---RUNNNING CLIENT---\n')
client.run(token)
