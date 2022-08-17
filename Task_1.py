import requests

def determine_intelligent_hero(list_of_heroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    total_info = resp.json()
    intelligence = 0
    most_intelligent_hero = ""
    for hero in total_info:
        if hero["name"] in list_of_heroes:
            if hero["powerstats"]["intelligence"] > intelligence:
                intelligence = hero["powerstats"]["intelligence"]
                most_intelligent_hero = hero["name"]

    print(f'Самый умный супергерой - {most_intelligent_hero}, с интеллектом = {intelligence}.')
    return

if __name__ == '__main__':
    heroes_list = ["Hulk", "Captain America", "Thanos"]
    determine_intelligent_hero(heroes_list)
