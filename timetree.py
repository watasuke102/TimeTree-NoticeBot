from timetree_sdk import TimeTreeApi
import urllib.request
import json

keyAPI     = ''
calenderID = ''


def getTodaysEvents():
	url = 'https://timetreeapis.com/calendars/{}/upcoming_events?timezone=Asia/Tokyo'.format(calenderID.join(calenderID.split()))
	req = urllib.request.Request(url)
	req.add_header('Authorization', 'Bearer ' + keyAPI)
	todaysEvents = 'おはようございます。'
	# APIでjsonを取得
	with urllib.request.urlopen(req) as res:
		data = json.loads(res.read().decode('UTF-8'))
		todaysEvents += '今日の予定は{}件です。\n'.format(len(data['data']))
		for content in data['data']:
			todaysEvents += ('・' + content['attributes']['title'] + '\n')
	return todaysEvents