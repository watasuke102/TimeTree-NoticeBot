import urllib.request
import json
import datetime

keyAPI     = ''
calenderID = ''
isDebugMode = False
isMentionEveryone = True

# デバッグ表示
def debug(string):
	if (isDebugMode):
		print(string)


# APIでjsonを取得
def getEventFromAPI():
	url = 'https://timetreeapis.com/calendars/{}/upcoming_events?timezone=Asia/Tokyo'.format(calenderID.join(calenderID.split()))
	req = urllib.request.Request(url)
	req.add_header('Authorization', 'Bearer ' + keyAPI)
	req.add_header('Accept', 'application/vnd.timetree.v1+json')
	with urllib.request.urlopen(req) as res:
		data = json.loads(res.read().decode('UTF-8'))
	return data

# 時刻はUTCで表示されるので，JST（UTC+0900）に変換する
# 20:00開始イベントの場合，取得した開始時間は11:00になっているので，
# int()で整数1100にする→900を足して2000にする→再度文字列に変換する

# イベントの開始時間をJSTで返す
def getEventStartAt(content):
	s = str(int(content['attributes']['start_at'][11:16].replace(':',''))+900)
	if len(s) == 3:
		return "0"+s[0:1]+":"+s[1:3]
	else:
		return s[0:2]+":"+s[2:4]

# イベントの終了時間をJSTで返す
def getEventEndAt(content):
	s = str(int(content['attributes']['end_at'][11:16].replace(':',''))+900)
	if len(s) == 3:
		return "0"+s[0:1]+":"+s[1:3]
	else:
		return s[0:2]+":"+s[2:4]

# イベントの名前を返す
def getEventTitle(content):
	return content['attributes']['title']

# その日のイベントを取得し、一覧にした文字列を返す
def getTodaysEvents():
	data = getEventFromAPI()
	todaysEvents = ''
	if isMentionEveryone:
		todaysEvents = '@everyone\n'
	# 予定の件数を取得
	todaysEvents += 'おはようございます。今日の予定は{}件です。\n\n'.format(len(data['data']))
	# 予定のタイトルを取得し表示
	for content in data['data']:
		todaysEvents += ('・' + getEventTitle(content) + '：')
		if content['attributes']['all_day']:
			todaysEvents += '終日\n'
		else:
			todaysEvents += (getEventStartAt(content) + '〜' + getEventEndAt(content) + '\n')
			debug(getEventTitle(content) + ' : ' + getEventStartAt(content) + '〜' + getEventEndAt(content) + '\n')
	return todaysEvents


# その日のイベントを取得し、現在時刻と比べる
# 10分後に開始されるイベントがあればそのイベント名を返す
def getEventAfterTenMinutes():
	data  = getEventFromAPI()
	event = ''
	a = datetime.datetime.now() + datetime.timedelta(minutes=10)
	now = a.strftime('%H:%M')
	for content in data['data']:
		debug(now + '  (now)'+getEventTitle(content)+'(start)  ' + getEventStartAt(content))
		if getEventStartAt(content) == now and content['attributes']['all_day'] == False:
			if isMentionEveryone:
				event+='@everyone\n'
			event += ('10分後：' + getEventTitle(content))
	return event