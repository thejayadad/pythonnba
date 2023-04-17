import requests

url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

querystring = {"id":"236","season":"2020"}

headers = {
	"X-RapidAPI-Key": "a07a9e7046msh29a34c2afef602ep18181ejsn56c05bf013f2",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response['player']['firstname'])