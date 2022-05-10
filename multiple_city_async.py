import codecs
import csv
import json
import time
import asyncio
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
             'dhaka'
             ]


async def get_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = requests.get(url)  # get weather from file by city name
    # about datastructures and datatypes 4 points

    text = response.text
    json_data = {"record": json.loads(text)}
    await update_data(json_data)


async def update_data(json_data):
    with codecs.open('data.csv', 'a', encoding='utf-8') as file:
        csv_file = csv.writer(file)
        for data in json_data.values():
            csv_file.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                               data['main']['temp_max'], data['main']['temp_min']])


async def main(cities):
    for city in cities:
        task = asyncio.create_task(get_data(city))
        await task


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main(city_list))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(total_time)
