import requests
key = 'efa048c730c59eabf46c03d2d32ad768'
targetDt = '20190713' #yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
print(response)
