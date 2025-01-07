import requests
import sys
import json


SMARTCAPTCHA_SERVER_KEY = "ysc2_4Y1ZxV5Zyyme7tQXujwZKyKwQa76UUNEsDfus36deb1c6a7d"


def check_captcha(token):
    resp = requests.get(
        "https://smartcaptcha.yandexcloud.net/validate",
        {
            "secret": ysc2_4Y1ZxV5Zyyme7tQXujwZKyKwQa76UUNEsDfus36deb1c6a7d,
            "token": ysc1_4Y1ZxV5Zyyme7tQXujwZsW9AikoIXYfjiorOf5gzc41223cd,
            "ip": "127.0.0.1"  # Pass user's IP
                               # How to get it may depend on your proxy or framework
        },
        timeout=1
    )
    server_output = resp.content.decode()
    if resp.status_code != 200:
        print(f"Allow access due to an error: code={resp.status_code}; message={server_output}", file=sys.stderr)
        return True
    return json.loads(server_output)["status"] == "ok"

token = "<token>"  # For example, request.form["smart-token"]
if check_captcha(token):
    print("Passed")
else:
    print("Robot")
