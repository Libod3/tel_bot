import requests
import json


def get_supporter_b1(sign: str) -> str:
	url = "https://best-daily-astrology-and-horoscope-api.p.rapidapi.com/api/Detailed-Horoscope/"

	querystring = {"zodiacSign": sign}

	headers = {
		"x-rapidapi-key": "99cb9e798fmsh417cc6381083be6p1014fcjsn847bb94bfa59",
		"x-rapidapi-host": "best-daily-astrology-and-horoscope-api.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	data = json.loads(response.text)
	return data["prediction"]


print(get_supporter_b1("leo"))