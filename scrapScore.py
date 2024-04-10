import requests
import json
import math
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from pprint import pprint
import csv


rBody  = {'userName': 'guest@qubic.li', 'password': 'guest13@Qubic.li', 'twoFactorCode': ''}
rHeaders = {'Accept': 'application/json', 'Content-Type': 'application/json-patch+json'}

try:
    r = requests.post('https://api.qubic.li/Auth/Login', data=json.dumps(rBody), headers=rHeaders,timeout=10)
    # print(r.status_code)
    token = r.json()['token']
    rHeaders = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    try:
        r = requests.get('https://api.qubic.li/Score/Get', headers=rHeaders, timeout=10)
        networkStat = r.json()

        # score=networkStat['scores'][0]['identity']
        # pprint (networkStat['scores'])

        scores = networkStat['scores']
        print(scores)
        s = sorted(scores, key=lambda t: t['score'], reverse=True)
        # pprint (s)
        rank = 0
        for comp in s:
            rank = rank + 1
            if comp['identity'] == 'NJFZJBBJLJIZYEYPXSMWDYINUPKBYOEDOYGQXVSOGHJAKCGDFAJJCTWANYLI' or comp[
                'identity'] == 'GDXYIXYSWTZHOEMBWFUTQCNIOYTBOTWJQNMQHXOGBFWUYVCPZDNKWSFHSGKL':
                print(
                    '----------------------------------------------------------------------------------------------------')
                print('Id: ', comp['identity'])
                print('rank:', rank, 'score:', comp['score'], 'BC score:', comp['adminScore'], 'avance sur le dernier:',comp['score']-s[676]['score'] )
                print('Next Computor:')
                print('rank:', rank + 1, 'score:', s[rank + 1]['score'], 'BC score:', s[rank + 1]['adminScore'])
        print('----------------------------------------------------------------------------------------------------')
        print('Last computor:')
        print('rank:', '676', 'score:', s[676]['score'], 'BC score:', s[676]['adminScore'])

    except requests.exceptions.Timeout as errt:
        print('Time out Error:', errt)

except requests.exceptions.Timeout as errt:
    print('Time out Error:',errt)
except requests.exceptions.RequestException as err:
    print("Oops l'api est encore dans le jus!")



# epochNumber = networkStat['scoreStatistics'][0]['epoch']
# epoch97Begin = date_time_obj = datetime.strptime('2024-02-21 12:00:00', '%Y-%m-%d %H:%M:%S')
# curEpochBegin = epoch97Begin + timedelta(days=7 * (epochNumber - 97))
# curEpochEnd = curEpochBegin + timedelta(days=7) - timedelta(seconds=1)
# #curEpochProgress = (datetime.utcnow() - curEpochBegin) / timedelta(days=7)
#
# print('\n\nCurrent epoch info:')
# print('Current epoch:',  epochNumber)
# print('Epoch start UTC:',  curEpochBegin)
# print('Epoch end UTC:',  curEpochEnd)