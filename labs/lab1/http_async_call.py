import asyncio
import requests

webhook_url = 'https://webhook.site/d14f38a6-ecc5-422f-94c1-9a4aa31c62d7'

@asyncio.coroutine
def get_header1():
    r1 = requests.get(webhook_url)
    info1 = r1.headers
    print(info1)

@asyncio.coroutine
def get_header2():
    r2 = requests.get(webhook_url)
    info2 = r2.headers
    print(info2)

@asyncio.coroutine
def get_header3():
    r3 = requests.get(webhook_url)
    info3 = r3.headers 
    print(info3)

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(get_header1()),
    asyncio.ensure_future(get_header2()),
    asyncio.ensure_future(get_header3())]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

