import requests
webhook_url = ' https://webhook.site/d14f38a6-ecc5-422f-94c1-9a4aa31c62d7'
i = 0
while i < 3:
    r = requests.get(webhook_url)
    info = r.headers
    print(info)
    i += 1