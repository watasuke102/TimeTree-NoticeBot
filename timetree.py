import urllib.request
import json
import datetime

keyAPI     = ''
calenderID = ''
isDebugMode = False

# デバッグ表示
def debug(string):
	if (isDebugMode):
		print(string)


# APIでjsonを取得
def getEventFromAPI():
	url = 'https://timetreeapis.com/calendars/{}/upcoming_events?timezone=Asia/Tokyo'.format(calenderID.join(calenderID.split()))
	req = urllib.request.Request(url)
	req.add_header('Authorization', 'Bearer ' + keyAPI)
	with urllib.request.urlopen(req) as res:
		data = json.loads(res.read().decode('UTF-8'))
	return data


# イベントの開始時間を返す
def getEventStartAt(content):
	return content['attributes']['start_at'][11:16]

# イベントの終了時間を返す
def getEventEndAt(content):
	return content['attributes']['start_at'][11:16]

# イベントの名前を返す
def getEventTitle(content):
	content['attributes']['title']

# その日のイベントを取得し、一覧にした文字列を返す
def getTodaysEvents():
	data = getEventFromAPI()
	# 予定の件数を取得
	todaysEvents = '@everyone\nおはようございます。今日の予定は{}件です。\n\n'.format(len(data['data']))
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
		debug(now + '  (now):(start)  ' + getEventStartAt(content))
		if getEventStartAt(content) == now:
			event += ('@everyone\n10分後：' + getEventTitle(content))
	return event