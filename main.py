import asyncio
import os
import platform
import subprocess
import sys

import requests


async def get_image():
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    full_path = f'{path}/today_image.jpg'
    response = requests.get(url)
    if response.status_code == 200:
        with open(full_path, 'wb') as f:
            f.write(response.content)
    return full_path


async def req_to_api(api_url, headers=None, params=None):
    if headers:
        return requests.get(api_url, headers=headers).json()
    return requests.get(api_url).json()


async def get_currency_exchange(currency_fut, api_url):
    json_currency = await req_to_api(api_url)
    currency_fut.set_result(json_currency)


async def get_ip(ip_fut, api_ip):
    api_json = await req_to_api(api_ip)
    ip_fut.set_result(api_json["ip"])


async def get_geo_by_ip(geo_fut, ip, api_geo):
    geo_json = await req_to_api(f"{api_geo}{ip.result()}")
    geo_fut.set_result(geo_json)


async def get_weather(weather_fut, api_weather, geo, weatherbit_key):
    geo_dict = geo.result()
    api_url = api_weather.format(geo_dict["lat"], geo_dict["lon"])
    headers = {
        "X-RapidAPI-Key": weatherbit_key,
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    weather_json = await req_to_api(api_url=api_url, headers=headers)
    weather_fut.set_result(weather_json)


async def get_day_image():
    image_path = await get_image()
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    if platform.system() == "Windows":
        os.startfile(image_path)
    else:
        subprocess.call([opener, image_path])


async def format_output(loop, currency_fut, ip_fut, weather_fut, geo_fut):
    geo = geo_fut.result()
    weather = weather_fut.result()
    currency_list = currency_fut.result()
    print("*" * 20, "Asynchronous data", "*" * 20)
    print(f"You geo info: \n{geo['country']}\n{geo['city']}, {geo['regionName']}")
    print(f"Weather on today: \nTemperature: {weather['data'][0]['temp']}C \
    \nWind speed: {weather['data'][0]['wind_spd']} m/s, {weather['data'][0]['wind_cdir_full']}")
    print("Currency")
    for item in currency_list:
        print(f"{item['ccy']}: {round(float(item['buy']), 2)} {item['base_ccy']}")
    print(f"You IP: {ip_fut.result()}")
    print("*" * 59)
    loop.stop()


async def main():
    api_currency_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    api_ip = "https://api.ipify.org?format=json"
    api_geo_by_ip = "http://ip-api.com/json/"
    weatherbit_key = "835e22b1a5msh82c8caa13bd25bap1940ccjsnc4005ce15b3a"
    api_weather = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly?lat={}&lon={}"
    loop = asyncio.get_running_loop()
    currency_fut = loop.create_future()
    ip_fut = loop.create_future()
    geo_fut = loop.create_future()
    weather_fut = loop.create_future()
    loop.create_task(get_currency_exchange(currency_fut, api_currency_url))
    loop.create_task(get_ip(ip_fut, api_ip))
    loop.create_task(get_geo_by_ip(geo_fut, ip_fut, api_geo_by_ip))
    loop.create_task(get_weather(weather_fut, api_weather, geo_fut, weatherbit_key))
    loop.create_task(get_day_image())
    loop.create_task(format_output(loop, currency_fut, ip_fut, weather_fut, geo_fut))


if __name__ == "__main__":
    asyncio.run(main())



