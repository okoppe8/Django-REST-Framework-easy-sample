import base64
import json
import urllib.request

# 変数は必要に応じて外部化してください。
url = "http://localhost:8000/api/logs/"
method = "POST"
headers = {"Content-Type": "application/json", }

user = "user"
password = "password"

temperature = 20
humidity = 80

# PythonオブジェクトをJSONに変換する
obj = {"temperature": temperature, "humidity": humidity, }
json_data = json.dumps(obj).encode("utf-8")

credentials = ('%s:%s' % (user, password))
encoded_credentials = base64.b64encode(credentials.encode('ascii'))

# httpリクエストを準備してPOST
request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
request.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

with urllib.request.urlopen(request) as response:
    response_body = response.read().decode("utf-8")