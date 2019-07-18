import xmltodict
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Аргументы скрипта обнаружения')
parser.add_argument('--discover', action="store_true", help='Обранужение имен лицензий')
parser.add_argument('--license', type=str, action='store', help='Имя лицензии')
parser.add_argument('--count', action="store_true", help='Получить общее количество лицензий')
parser.add_argument('--usedcount', action="store_true", help='Получить количество использованных лицензий')
args = parser.parse_args()

URI = 'http://yr-cinegycore:8989/getinfo'

parsed = xmltodict.parse(requests.get(URI).content.decode())

if args.discover:
    result = {'data': []}
    for item in parsed.get('LicensingService').get('AvailableLicenses').get('LicenseType'):
        result['data'].append({
            "{#LICENCE_NAME}": item.get('@name'),
        })
    print(json.dumps(result))

if args.license:
    for item in parsed.get('LicensingService').get('AvailableLicenses').get('LicenseType'):
        if item.get('@name') == args.license:
            if args.count:
                print(item.get('License').get('@count'))
            if args.usedcount:
                print(item.get('License').get('@usedCount'))
