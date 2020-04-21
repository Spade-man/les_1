import requests as r
import json
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
z = r.get(url)
data = json.loads(z.text)
print(data)