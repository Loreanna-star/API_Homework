import requests
from datetime import date,timedelta

def get_questions_info(tag):
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "fromdate": date.today()-timedelta(days=2),
        "todate": date.today(),
        "tagged": tag,
        "site": "stackoverflow"
    }
    response = requests.get(url, params=params).json()
    for question in response["items"]:
        print(question["title"])   
    return

if __name__ == '__main__':
    get_questions_info("python")

