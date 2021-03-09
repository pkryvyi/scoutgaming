import requests
import time
import datetime
import calendar
import json
import os

api_key = "OAuth " + os.environ.get("API_KEY")
page_id = os.environ.get("PAGE_ID")
metric_id = os.environ.get("METRIC_ID")

get_header = {'Authorization': 'Bearer fanteam undefined'}
auth_header = {'Authorization': api_key}
service_url = 'https://fanteam-game.api.scoutgg-stg.net/users/@me'
statuspage_url = f"https://api.statuspage.io/v1/pages/{page_id}/metrics/data"

while True:
    get_request = requests.get(service_url, headers=get_header)
    latency = get_request.headers['X-Response-Time']

    timestamp = calendar.timegm(time.gmtime())

    data = {
        "data": {
        metric_id: [
            {
                "timestamp": timestamp,
                "value": latency
            }
        ]
        }
    }
    print(data)

    post_request = requests.post(statuspage_url, headers = auth_header, data = json.dumps(data) )
    print(post_request.status_code)

    time.sleep(30)
