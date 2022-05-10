import codecs
import csv
import json
import requests

city_list = ['mumbai',
             'kolkata',
             'delhi',
             'ambala',
             'dhanera',
             'disa',
             'bengaluru',
             'london',
             'moscow',
             'kathmandu',
             'pune',
             'jaipur',
             'goa',
             'gangtok',
             'manali',
             'chandigarh',
             'surat',
             'nagpur',
             'belgium',
             'Sharjah',
             'dhaka',
             'bhopal',
             'indore',
             'ujjain',
             'tokyo',
             'paris',
             'jakarta',
             'riva',
             'sagar',
             'jabalpur',
             'gwalior',
             'lucknow',
             'manhatten',
             'arizona',
             'berlin',
             'howrah',
             'boston',
             'kurnool',
             'satna',
             'sidhi',
             'mirzapur',
             'dhanbad',
             'raipur',
             'chapra',
             'bilaspur',
             'mysore',
             'chennai',
             'amritsar',
             'contai',
             'kota',
             'bundi',
             'bhind',
             'jhansi'
             ]


def get_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = requests.get(url)  # get weather from file by city name
    # about datastructures and datatypes 4 points

    text = response.text
    json_data = {"record": json.loads(text)}
    update_data(json_data)


def update_data(json_data):
    with codecs.open('data.csv', 'a', encoding='utf-8') as file:
        csv_file = csv.writer(file)
        for data in json_data.values():
            csv_file.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                               data['main']['temp_max'], data['main']['temp_min']])

        print('CSV file updated')


def main(cities):
    for city_ in cities:
        get_data(city_)


if __name__ == '__main__':
    main(city_list)
