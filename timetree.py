from timetree_sdk import TimeTreeApi
import urllib.request
import json

keyAPI     = ''
calenderID = ''


def getTodaysEvents():
	url = 'https://timetreeapis.com/calendars/{}/upcoming_events?timezone=Asia/Tokyo'.format(calenderID.join(calenderID.split()))
	req = urllib.request.Request(url)
	req.add_header('Authorization', 'Bearer ' + keyAPI)
	with urllib.request.urlopen(req) as res:
		print(res.read().decode('UTF-8'))