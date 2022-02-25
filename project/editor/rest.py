import requests
import json
from PIL import Image
import numpy as np
import asyncio
import time

def postData(url, data):
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)


def arrayToImageRGB(response):
    r = response.json()['lhs']
    if len(r[1]["mwdata"]) != 1:
        imgnpR = np.asarray(r[0]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpG = np.asarray(r[1]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpB = np.asarray(r[2]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpRGB = np.dstack((imgnpR, imgnpG, imgnpB))
    else:
        imgnpRGB = imgnpR = np.asarray(r[0]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
    imgnpRGB = np.rot90(np.flip(imgnpRGB), 3)
    return Image.fromarray(imgnpRGB)

def waitForResourceAvailable(response, timeout = 90, timewait = 20):
    timer = 0
    while response.status_code == 204:
        time.sleep(timewait)
        timer += timewait
        if timer > timeout:
            return False
        if response.status_code == 200:
            return True