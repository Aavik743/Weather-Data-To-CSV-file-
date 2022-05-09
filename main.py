import codecs
import csv
import json
import urllib.request
import asyncio


def get_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = urllib.request.urlopen(url)

    text = response.read()
    json_data = {"record": json.loads(text)}
    return json_data


def update_data(json_data):
    with codecs.open('data.csv', 'a', encoding='utf-8') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(["Name", "Longitude", "Latitude", "Temp", "Max Temp", "Min Temp"])
        for data in json_data.values():
            csv_file.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                               data['main']['temp_max'], data['main']['temp_min']])

        print('CSV file updated')
        return 0


if __name__ == '__main__':
    city = input("Enter the name of a city\n")
    data = get_data(city)
    update_data(data)
