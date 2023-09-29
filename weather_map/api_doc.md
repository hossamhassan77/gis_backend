### **`GET /forcast/specific-point`**

Forecast weather for 5 days/3 days steps for a point in earth.

#### `Request`

1.  lat(required/float): Latitude.
2.  lng(required/float): Longitude.
    

#### `Example`

`Request:`

lat: 32.2561  
lng: 36.1852

Response:

``` json
{
    "cod": "200",
    "message": 0,
    "cnt": 40,
    "list": [
        {
            "dt": 1681225200,
            "main": {
                "temp": 22.71,
                "feels_like": 21.64,
                "temp_min": 22.71,
                "temp_max": 23.34,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 1004,
                "humidity": 23,
                "temp_kf": -0.63
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "clouds": {
                "all": 21
            },
            "wind": {
                "speed": 7.14,
                "deg": 281,
                "gust": 7.92
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-11 15:00:00"
        },
        {
            "dt": 1681236000,
            "main": {
                "temp": 19.95,
                "feels_like": 18.91,
                "temp_min": 18.73,
                "temp_max": 19.95,
                "pressure": 1009,
                "sea_level": 1009,
                "grnd_level": 1006,
                "humidity": 35,
                "temp_kf": 1.22
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "clouds": {
                "all": 43
            },
            "wind": {
                "speed": 6.7,
                "deg": 313,
                "gust": 7.83
            },
            "visibility": 10000,
            "pop": 0.01,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-11 18:00:00"
        },
        {
            "dt": 1681246800,
            "main": {
                "temp": 15.97,
                "feels_like": 15.11,
                "temp_min": 15.97,
                "temp_max": 15.97,
                "pressure": 1010,
                "sea_level": 1010,
                "grnd_level": 1006,
                "humidity": 57,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 81
            },
            "wind": {
                "speed": 2.77,
                "deg": 19,
                "gust": 3.46
            },
            "visibility": 10000,
            "pop": 0.78,
            "rain": {
                "3h": 0.74
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-11 21:00:00"
        },
        {
            "dt": 1681257600,
            "main": {
                "temp": 13.93,
                "feels_like": 13.13,
                "temp_min": 13.93,
                "temp_max": 13.93,
                "pressure": 1009,
                "sea_level": 1009,
                "grnd_level": 1006,
                "humidity": 67,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 81
            },
            "wind": {
                "speed": 2.83,
                "deg": 329,
                "gust": 3.69
            },
            "visibility": 10000,
            "pop": 0.85,
            "rain": {
                "3h": 0.27
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-12 00:00:00"
        },
        {
            "dt": 1681268400,
            "main": {
                "temp": 13.55,
                "feels_like": 12.66,
                "temp_min": 13.55,
                "temp_max": 13.55,
                "pressure": 1010,
                "sea_level": 1010,
                "grnd_level": 1007,
                "humidity": 65,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 50
            },
            "wind": {
                "speed": 5.02,
                "deg": 282,
                "gust": 8.2
            },
            "visibility": 10000,
            "pop": 0.93,
            "rain": {
                "3h": 1.43
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-12 03:00:00"
        },
        {
            "dt": 1681279200,
            "main": {
                "temp": 15.17,
                "feels_like": 14.15,
                "temp_min": 15.17,
                "temp_max": 15.17,
                "pressure": 1012,
                "sea_level": 1012,
                "grnd_level": 1009,
                "humidity": 54,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 57
            },
            "wind": {
                "speed": 6.96,
                "deg": 276,
                "gust": 8.37
            },
            "visibility": 10000,
            "pop": 0.87,
            "rain": {
                "3h": 0.17
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-12 06:00:00"
        },
        {
            "dt": 1681290000,
            "main": {
                "temp": 19.9,
                "feels_like": 18.83,
                "temp_min": 19.9,
                "temp_max": 19.9,
                "pressure": 1012,
                "sea_level": 1012,
                "grnd_level": 1009,
                "humidity": 34,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "clouds": {
                "all": 46
            },
            "wind": {
                "speed": 7.38,
                "deg": 296,
                "gust": 9.49
            },
            "visibility": 10000,
            "pop": 0.16,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-12 09:00:00"
        },
        {
            "dt": 1681300800,
            "main": {
                "temp": 20.84,
                "feels_like": 19.76,
                "temp_min": 20.84,
                "temp_max": 20.84,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1009,
                "humidity": 30,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 64
            },
            "wind": {
                "speed": 9.47,
                "deg": 296,
                "gust": 10.81
            },
            "visibility": 10000,
            "pop": 0.03,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-12 12:00:00"
        },
        {
            "dt": 1681311600,
            "main": {
                "temp": 20.27,
                "feels_like": 19.19,
                "temp_min": 20.27,
                "temp_max": 20.27,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1010,
                "humidity": 32,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 77
            },
            "wind": {
                "speed": 8.62,
                "deg": 292,
                "gust": 10.32
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-12 15:00:00"
        },
        {
            "dt": 1681322400,
            "main": {
                "temp": 17.21,
                "feels_like": 16.29,
                "temp_min": 17.21,
                "temp_max": 17.21,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 50,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 67
            },
            "wind": {
                "speed": 5.93,
                "deg": 304,
                "gust": 8.56
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-12 18:00:00"
        },
        {
            "dt": 1681333200,
            "main": {
                "temp": 15.65,
                "feels_like": 14.73,
                "temp_min": 15.65,
                "temp_max": 15.65,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1012,
                "humidity": 56,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 3.82,
                "deg": 274,
                "gust": 6.22
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-12 21:00:00"
        },
        {
            "dt": 1681344000,
            "main": {
                "temp": 14.52,
                "feels_like": 13.72,
                "temp_min": 14.52,
                "temp_max": 14.52,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 65,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 1
            },
            "wind": {
                "speed": 4.06,
                "deg": 247,
                "gust": 7.15
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-13 00:00:00"
        },
        {
            "dt": 1681354800,
            "main": {
                "temp": 13.62,
                "feels_like": 12.71,
                "temp_min": 13.62,
                "temp_max": 13.62,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 64,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 4.08,
                "deg": 239,
                "gust": 6.58
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-13 03:00:00"
        },
        {
            "dt": 1681365600,
            "main": {
                "temp": 17.15,
                "feels_like": 16.02,
                "temp_min": 17.15,
                "temp_max": 17.15,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 42,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 5.27,
                "deg": 243,
                "gust": 7.9
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-13 06:00:00"
        },
        {
            "dt": 1681376400,
            "main": {
                "temp": 22.58,
                "feels_like": 21.57,
                "temp_min": 22.58,
                "temp_max": 22.58,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 26,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.17,
                "deg": 249,
                "gust": 8.48
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-13 09:00:00"
        },
        {
            "dt": 1681387200,
            "main": {
                "temp": 25.72,
                "feels_like": 24.82,
                "temp_min": 25.72,
                "temp_max": 25.72,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1010,
                "humidity": 18,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.63,
                "deg": 275,
                "gust": 8.22
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-13 12:00:00"
        },
        {
            "dt": 1681398000,
            "main": {
                "temp": 25.22,
                "feels_like": 24.29,
                "temp_min": 25.22,
                "temp_max": 25.22,
                "pressure": 1014,
                "sea_level": 1014,
                "grnd_level": 1010,
                "humidity": 19,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.22,
                "deg": 294,
                "gust": 6.58
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-13 15:00:00"
        },
        {
            "dt": 1681408800,
            "main": {
                "temp": 20.54,
                "feels_like": 19.59,
                "temp_min": 20.54,
                "temp_max": 20.54,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1012,
                "humidity": 36,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.37,
                "deg": 348,
                "gust": 8.76
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-13 18:00:00"
        },
        {
            "dt": 1681419600,
            "main": {
                "temp": 17.15,
                "feels_like": 16.49,
                "temp_min": 17.15,
                "temp_max": 17.15,
                "pressure": 1017,
                "sea_level": 1017,
                "grnd_level": 1014,
                "humidity": 60,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 3.62,
                "deg": 25,
                "gust": 4.48
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-13 21:00:00"
        },
        {
            "dt": 1681430400,
            "main": {
                "temp": 16.41,
                "feels_like": 15.8,
                "temp_min": 16.41,
                "temp_max": 16.41,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 65,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2.14,
                "deg": 30,
                "gust": 2.43
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-14 00:00:00"
        },
        {
            "dt": 1681441200,
            "main": {
                "temp": 15.72,
                "feels_like": 15.15,
                "temp_min": 15.72,
                "temp_max": 15.72,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 69,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2,
                "deg": 33,
                "gust": 2.21
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-14 03:00:00"
        },
        {
            "dt": 1681452000,
            "main": {
                "temp": 18.32,
                "feels_like": 17.7,
                "temp_min": 18.32,
                "temp_max": 18.32,
                "pressure": 1017,
                "sea_level": 1017,
                "grnd_level": 1014,
                "humidity": 57,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 1.57,
                "deg": 17,
                "gust": 1.37
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-14 06:00:00"
        },
        {
            "dt": 1681462800,
            "main": {
                "temp": 22.73,
                "feels_like": 22,
                "temp_min": 22.73,
                "temp_max": 22.73,
                "pressure": 1017,
                "sea_level": 1017,
                "grnd_level": 1013,
                "humidity": 36,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 3
            },
            "wind": {
                "speed": 1.06,
                "deg": 334,
                "gust": 1.2
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-14 09:00:00"
        },
        {
            "dt": 1681473600,
            "main": {
                "temp": 26.08,
                "feels_like": 26.08,
                "temp_min": 26.08,
                "temp_max": 26.08,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1011,
                "humidity": 24,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "clouds": {
                "all": 26
            },
            "wind": {
                "speed": 1.19,
                "deg": 310,
                "gust": 2.09
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-14 12:00:00"
        },
        {
            "dt": 1681484400,
            "main": {
                "temp": 27.09,
                "feels_like": 26.2,
                "temp_min": 27.09,
                "temp_max": 27.09,
                "pressure": 1014,
                "sea_level": 1014,
                "grnd_level": 1011,
                "humidity": 22,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.83,
                "deg": 291,
                "gust": 3.77
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-14 15:00:00"
        },
        {
            "dt": 1681495200,
            "main": {
                "temp": 21.04,
                "feels_like": 20.48,
                "temp_min": 21.04,
                "temp_max": 21.04,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 49,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 8.38,
                "deg": 24,
                "gust": 10.18
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-14 18:00:00"
        },
        {
            "dt": 1681506000,
            "main": {
                "temp": 19.17,
                "feels_like": 18.63,
                "temp_min": 19.17,
                "temp_max": 19.17,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 57,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 99
            },
            "wind": {
                "speed": 5.3,
                "deg": 35,
                "gust": 7.38
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-14 21:00:00"
        },
        {
            "dt": 1681516800,
            "main": {
                "temp": 18.09,
                "feels_like": 17.55,
                "temp_min": 18.09,
                "temp_max": 18.09,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 61,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 95
            },
            "wind": {
                "speed": 4.46,
                "deg": 35,
                "gust": 6.66
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-15 00:00:00"
        },
        {
            "dt": 1681527600,
            "main": {
                "temp": 17.31,
                "feels_like": 16.74,
                "temp_min": 17.31,
                "temp_max": 17.31,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 63,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 89
            },
            "wind": {
                "speed": 4.01,
                "deg": 34,
                "gust": 6.13
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-15 03:00:00"
        },
        {
            "dt": 1681538400,
            "main": {
                "temp": 20.37,
                "feels_like": 19.69,
                "temp_min": 20.37,
                "temp_max": 20.37,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 1013,
                "humidity": 47,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 95
            },
            "wind": {
                "speed": 4.78,
                "deg": 41,
                "gust": 5.84
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-15 06:00:00"
        },
        {
            "dt": 1681549200,
            "main": {
                "temp": 26.19,
                "feels_like": 26.19,
                "temp_min": 26.19,
                "temp_max": 26.19,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 27,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "clouds": {
                "all": 26
            },
            "wind": {
                "speed": 4.5,
                "deg": 36,
                "gust": 4.93
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-15 09:00:00"
        },
        {
            "dt": 1681560000,
            "main": {
                "temp": 29.96,
                "feels_like": 28.14,
                "temp_min": 29.96,
                "temp_max": 29.96,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1010,
                "humidity": 17,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "clouds": {
                "all": 13
            },
            "wind": {
                "speed": 3.83,
                "deg": 36,
                "gust": 4.93
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-15 12:00:00"
        },
        {
            "dt": 1681570800,
            "main": {
                "temp": 30.16,
                "feels_like": 28.29,
                "temp_min": 30.16,
                "temp_max": 30.16,
                "pressure": 1011,
                "sea_level": 1011,
                "grnd_level": 1008,
                "humidity": 17,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 6.31,
                "deg": 48,
                "gust": 6.34
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-15 15:00:00"
        },
        {
            "dt": 1681581600,
            "main": {
                "temp": 22.13,
                "feels_like": 21.31,
                "temp_min": 22.13,
                "temp_max": 22.13,
                "pressure": 1014,
                "sea_level": 1014,
                "grnd_level": 1011,
                "humidity": 35,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 7.92,
                "deg": 43,
                "gust": 10.19
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-15 18:00:00"
        },
        {
            "dt": 1681592400,
            "main": {
                "temp": 18.86,
                "feels_like": 18.16,
                "temp_min": 18.86,
                "temp_max": 18.86,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 1012,
                "humidity": 52,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 5.4,
                "deg": 32,
                "gust": 7.89
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-15 21:00:00"
        },
        {
            "dt": 1681603200,
            "main": {
                "temp": 17.35,
                "feels_like": 16.76,
                "temp_min": 17.35,
                "temp_max": 17.35,
                "pressure": 1014,
                "sea_level": 1014,
                "grnd_level": 1010,
                "humidity": 62,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 4.51,
                "deg": 35,
                "gust": 6.95
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-16 00:00:00"
        },
        {
            "dt": 1681614000,
            "main": {
                "temp": 16.09,
                "feels_like": 15.58,
                "temp_min": 16.09,
                "temp_max": 16.09,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1010,
                "humidity": 70,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 4.79,
                "deg": 38,
                "gust": 7.62
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2023-04-16 03:00:00"
        },
        {
            "dt": 1681624800,
            "main": {
                "temp": 19.88,
                "feels_like": 19.18,
                "temp_min": 19.88,
                "temp_max": 19.88,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 1010,
                "humidity": 48,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 5.38,
                "deg": 49,
                "gust": 7.25
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-16 06:00:00"
        },
        {
            "dt": 1681635600,
            "main": {
                "temp": 26.91,
                "feels_like": 26.06,
                "temp_min": 26.91,
                "temp_max": 26.91,
                "pressure": 1012,
                "sea_level": 1012,
                "grnd_level": 1009,
                "humidity": 21,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 1
            },
            "wind": {
                "speed": 5.49,
                "deg": 51,
                "gust": 6.27
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-16 09:00:00"
        },
        {
            "dt": 1681646400,
            "main": {
                "temp": 31.03,
                "feels_like": 28.96,
                "temp_min": 31.03,
                "temp_max": 31.03,
                "pressure": 1010,
                "sea_level": 1010,
                "grnd_level": 1006,
                "humidity": 13,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 3
            },
            "wind": {
                "speed": 4.94,
                "deg": 52,
                "gust": 5.16
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-04-16 12:00:00"
        }
    ],
    "city": {
        "id": 360630,
        "name": "Cairo",
        "coord": {
            "lat": 30.0582,
            "lon": 31.1971
        },
        "country": "EG",
        "population": 7734614,
        "timezone": 7200,
        "sunrise": 1681183992,
        "sunset": 1681229947
    }
}

```

StartFragment

### POST /weather-map/current-weather/random-points-in-bound

gets current weather for multiple points in the map.

#### `Request`

1.  **bound(required/list): List of polygon vertex.__**
2.  **points_number(required/int) how many points do you want to get weather?**
    

#### `Example`

`Request:`


``` json
{
    "bound": [{"lat":40.38427119123016,"lng":-105.18831674093013},{"lat":40.35078901802308,"lng":-104.38631478780513},{"lat":39.84234491122627,"lng":-104.50167123311763},{"lat":39.93507177126157,"lng":-105.61129037374263},{"lat":40.44700542822942,"lng":-105.52889291280513}],
    "points_number": 5
}

```

Response:

```json
[
    {
        "Point number 1": {
            "coord": {
                "lon": -104.9773,
                "lat": 40.3649
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 7.91,
                "feels_like": 5.37,
                "temp_min": 2.23,
                "temp_max": 13.83,
                "pressure": 1020,
                "humidity": 53
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.12,
                "deg": 20
            },
            "clouds": {
                "all": 0
            },
            "dt": 1681216626,
            "sys": {
                "type": 1,
                "id": 4120,
                "country": "US",
                "sunrise": 1681216067,
                "sunset": 1681263224
            },
            "timezone": -21600,
            "id": 5578536,
            "name": "Johnstown",
            "cod": 200
        }
    },
    {
        "Point number 2": {
            "coord": {
                "lon": -104.5248,
                "lat": 39.9076
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 8.81,
                "feels_like": 6.05,
                "temp_min": 6.33,
                "temp_max": 12.47,
                "pressure": 1016,
                "humidity": 34
            },
            "visibility": 10000,
            "wind": {
                "speed": 5.14,
                "deg": 160
            },
            "clouds": {
                "all": 20
            },
            "dt": 1681216627,
            "sys": {
                "type": 2,
                "id": 2002531,
                "country": "US",
                "sunrise": 1681215988,
                "sunset": 1681263086
            },
            "timezone": -21600,
            "id": 5411363,
            "name": "Adams",
            "cod": 200
        }
    },
    {
        "Point number 3": {
            "coord": {
                "lon": -105.5086,
                "lat": 40.0888
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 1.4,
                "feels_like": -3.17,
                "temp_min": -4.81,
                "temp_max": 5.09,
                "pressure": 1021,
                "humidity": 46,
                "sea_level": 1021,
                "grnd_level": 725
            },
            "visibility": 10000,
            "wind": {
                "speed": 5,
                "deg": 272,
                "gust": 5.39
            },
            "clouds": {
                "all": 7
            },
            "dt": 1681216628,
            "sys": {
                "type": 2,
                "id": 2081400,
                "country": "US",
                "sunrise": 1681216212,
                "sunset": 1681263334
            },
            "timezone": -21600,
            "id": 5583173,
            "name": "Ward",
            "cod": 200
        }
    },
    {
        "Point number 4": {
            "coord": {
                "lon": -105.4358,
                "lat": 40.418
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 4.81,
                "feels_like": 3.95,
                "temp_min": -1.73,
                "temp_max": 7.05,
                "pressure": 1016,
                "humidity": 41
            },
            "visibility": 10000,
            "wind": {
                "speed": 1.34,
                "deg": 199,
                "gust": 4.02
            },
            "clouds": {
                "all": 8
            },
            "dt": 1681216628,
            "sys": {
                "type": 2,
                "id": 2020882,
                "country": "US",
                "sunrise": 1681216173,
                "sunset": 1681263338
            },
            "timezone": -21600,
            "id": 5580569,
            "name": "Olympus Heights",
            "cod": 200
        }
    },
    {
        "Point number 5": {
            "coord": {
                "lon": -105.5016,
                "lat": 40.4227
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 5.57,
                "feels_like": 4.81,
                "temp_min": -1.52,
                "temp_max": 7.27,
                "pressure": 1016,
                "humidity": 41
            },
            "visibility": 10000,
            "wind": {
                "speed": 1.34,
                "deg": 199,
                "gust": 4.02
            },
            "clouds": {
                "all": 7
            },
            "dt": 1681216629,
            "sys": {
                "type": 2,
                "id": 2020882,
                "country": "US",
                "sunrise": 1681216189,
                "sunset": 1681263354
            },
            "timezone": -21600,
            "id": 5580569,
            "name": "Olympus Heights",
            "cod": 200
        }
    }
]

```

### POST /weather-map/forecast/random-points-in-bound


gets forecast 5 Days/ 3 hours steps weather for multiple points in map bound.

#### `Request`

1.  **bound(required/list): List of polygon vertex.__**
2.  **points_number(required/int) how many points do you want to get weather?**
    

#### `Example`

`Request:`

```json
 {
    "bound": [{"lat":40.38427119123016,"lng":-105.18831674093013},{"lat":40.35078901802308,"lng":-104.38631478780513},{"lat":39.84234491122627,"lng":-104.50167123311763},{"lat":39.93507177126157,"lng":-105.61129037374263},{"lat":40.44700542822942,"lng":-105.52889291280513}],
    "points_number": 4
}

```

Response:

```json
 [
    {
        "Point(1): 'lng':-105.51378947354362, 'lat': 40.07249405714103": {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                    "dt": 1683633600,
                    "main": {
                        "temp": 0.58,
                        "feels_like": -3.21,
                        "temp_min": 0.35,
                        "temp_max": 0.58,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 720,
                        "humidity": 61,
                        "temp_kf": 0.23
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 2
                    },
                    "wind": {
                        "speed": 3.5,
                        "deg": 268,
                        "gust": 3.31
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 12:00:00"
                },
                {
                    "dt": 1683644400,
                    "main": {
                        "temp": 7.09,
                        "feels_like": 6.39,
                        "temp_min": 7.09,
                        "temp_max": 10.29,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 727,
                        "humidity": 39,
                        "temp_kf": -3.2
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 1
                    },
                    "wind": {
                        "speed": 1.45,
                        "deg": 178,
                        "gust": 5.45
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 15:00:00"
                },
                {
                    "dt": 1683655200,
                    "main": {
                        "temp": 13.81,
                        "feels_like": 11.87,
                        "temp_min": 13.81,
                        "temp_max": 13.81,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 728,
                        "humidity": 24,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "clouds": {
                        "all": 15
                    },
                    "wind": {
                        "speed": 2.48,
                        "deg": 112,
                        "gust": 7.17
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 18:00:00"
                },
                {
                    "dt": 1683666000,
                    "main": {
                        "temp": 10.7,
                        "feels_like": 8.87,
                        "temp_min": 10.7,
                        "temp_max": 10.7,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 726,
                        "humidity": 40,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.27,
                        "deg": 81,
                        "gust": 3.74
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 21:00:00"
                },
                {
                    "dt": 1683676800,
                    "main": {
                        "temp": 9.11,
                        "feels_like": 9.11,
                        "temp_min": 9.11,
                        "temp_max": 9.11,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 726,
                        "humidity": 50,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.1,
                        "deg": 87,
                        "gust": 2.96
                    },
                    "visibility": 10000,
                    "pop": 0.24,
                    "rain": {
                        "3h": 0.52
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 00:00:00"
                },
                {
                    "dt": 1683687600,
                    "main": {
                        "temp": 4.97,
                        "feels_like": 2.39,
                        "temp_min": 4.97,
                        "temp_max": 4.97,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 723,
                        "humidity": 59,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.11,
                        "deg": 263,
                        "gust": 2.82
                    },
                    "visibility": 10000,
                    "pop": 0.2,
                    "rain": {
                        "3h": 0.11
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 03:00:00"
                },
                {
                    "dt": 1683698400,
                    "main": {
                        "temp": 2.7,
                        "feels_like": 2.7,
                        "temp_min": 2.7,
                        "temp_max": 2.7,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 722,
                        "humidity": 65,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 76
                    },
                    "wind": {
                        "speed": 0.6,
                        "deg": 226,
                        "gust": 1.15
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 06:00:00"
                },
                {
                    "dt": 1683709200,
                    "main": {
                        "temp": 1.36,
                        "feels_like": 1.36,
                        "temp_min": 1.36,
                        "temp_max": 1.36,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 721,
                        "humidity": 83,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01n"
                        }
                    ],
                    "clouds": {
                        "all": 1
                    },
                    "wind": {
                        "speed": 1.09,
                        "deg": 278,
                        "gust": 1.27
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 09:00:00"
                },
                {
                    "dt": 1683720000,
                    "main": {
                        "temp": 1.31,
                        "feels_like": -0.67,
                        "temp_min": 1.31,
                        "temp_max": 1.31,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 720,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "clouds": {
                        "all": 12
                    },
                    "wind": {
                        "speed": 1.79,
                        "deg": 271,
                        "gust": 1.68
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 12:00:00"
                },
                {
                    "dt": 1683730800,
                    "main": {
                        "temp": 9.4,
                        "feels_like": 8.15,
                        "temp_min": 9.4,
                        "temp_max": 9.4,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 724,
                        "humidity": 57,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "clouds": {
                        "all": 12
                    },
                    "wind": {
                        "speed": 2.44,
                        "deg": 98,
                        "gust": 2.94
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 15:00:00"
                },
                {
                    "dt": 1683741600,
                    "main": {
                        "temp": 12.83,
                        "feels_like": 11.29,
                        "temp_min": 12.83,
                        "temp_max": 12.83,
                        "pressure": 1007,
                        "sea_level": 1007,
                        "grnd_level": 724,
                        "humidity": 43,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 16
                    },
                    "wind": {
                        "speed": 4.83,
                        "deg": 103,
                        "gust": 7.53
                    },
                    "visibility": 10000,
                    "pop": 0.39,
                    "rain": {
                        "3h": 0.69
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 18:00:00"
                },
                {
                    "dt": 1683752400,
                    "main": {
                        "temp": 9.74,
                        "feels_like": 8.87,
                        "temp_min": 9.74,
                        "temp_max": 9.74,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 721,
                        "humidity": 64,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 2.02,
                        "deg": 137,
                        "gust": 4.97
                    },
                    "visibility": 9741,
                    "pop": 0.59,
                    "rain": {
                        "3h": 3.59
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 21:00:00"
                },
                {
                    "dt": 1683763200,
                    "main": {
                        "temp": 6.07,
                        "feels_like": 6.07,
                        "temp_min": 6.07,
                        "temp_max": 6.07,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 718,
                        "humidity": 81,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 0.84,
                        "deg": 258,
                        "gust": 2.76
                    },
                    "visibility": 10000,
                    "pop": 0.84,
                    "rain": {
                        "3h": 3.75
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 00:00:00"
                },
                {
                    "dt": 1683774000,
                    "main": {
                        "temp": 3.87,
                        "feels_like": 2.63,
                        "temp_min": 3.87,
                        "temp_max": 3.87,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 718,
                        "humidity": 99,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.52,
                        "deg": 85,
                        "gust": 2.51
                    },
                    "visibility": 205,
                    "pop": 0.96,
                    "rain": {
                        "3h": 1.62
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 03:00:00"
                },
                {
                    "dt": 1683784800,
                    "main": {
                        "temp": 3.4,
                        "feels_like": 3.4,
                        "temp_min": 3.4,
                        "temp_max": 3.4,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 716,
                        "humidity": 97,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 0.79,
                        "deg": 299,
                        "gust": 1.2
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 2.66
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 06:00:00"
                },
                {
                    "dt": 1683795600,
                    "main": {
                        "temp": 2.47,
                        "feels_like": 0.46,
                        "temp_min": 2.47,
                        "temp_max": 2.47,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 713,
                        "humidity": 90,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 98
                    },
                    "wind": {
                        "speed": 1.97,
                        "deg": 314,
                        "gust": 1.83
                    },
                    "visibility": 9561,
                    "pop": 1,
                    "rain": {
                        "3h": 1.77
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 09:00:00"
                },
                {
                    "dt": 1683806400,
                    "main": {
                        "temp": 2.49,
                        "feels_like": -0.41,
                        "temp_min": 2.49,
                        "temp_max": 2.49,
                        "pressure": 1003,
                        "sea_level": 1003,
                        "grnd_level": 713,
                        "humidity": 85,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 2.88,
                        "deg": 293,
                        "gust": 3.24
                    },
                    "visibility": 4167,
                    "pop": 1,
                    "rain": {
                        "3h": 3.09
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 12:00:00"
                },
                {
                    "dt": 1683817200,
                    "main": {
                        "temp": 3.12,
                        "feels_like": 0.62,
                        "temp_min": 3.12,
                        "temp_max": 3.12,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 715,
                        "humidity": 91,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.56,
                        "deg": 335,
                        "gust": 4.92
                    },
                    "visibility": 87,
                    "pop": 1,
                    "rain": {
                        "3h": 1.94
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 15:00:00"
                },
                {
                    "dt": 1683828000,
                    "main": {
                        "temp": 2.75,
                        "feels_like": -0.01,
                        "temp_min": 2.75,
                        "temp_max": 2.75,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 715,
                        "humidity": 92,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.77,
                        "deg": 286,
                        "gust": 3.95
                    },
                    "visibility": 705,
                    "pop": 1,
                    "rain": {
                        "3h": 7.12
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 18:00:00"
                },
                {
                    "dt": 1683838800,
                    "main": {
                        "temp": 1.17,
                        "feels_like": -1.44,
                        "temp_min": 1.17,
                        "temp_max": 1.17,
                        "pressure": 1009,
                        "sea_level": 1009,
                        "grnd_level": 716,
                        "humidity": 95,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 601,
                            "main": "Snow",
                            "description": "snow",
                            "icon": "13d"
                        }
                    ],
                    "clouds": {
                        "all": 95
                    },
                    "wind": {
                        "speed": 2.31,
                        "deg": 289,
                        "gust": 5.85
                    },
                    "visibility": 523,
                    "pop": 1,
                    "snow": {
                        "3h": 10.87
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 21:00:00"
                },
                {
                    "dt": 1683849600,
                    "main": {
                        "temp": 2.28,
                        "feels_like": -1.65,
                        "temp_min": 2.28,
                        "temp_max": 2.28,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 718,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 97
                    },
                    "wind": {
                        "speed": 4.27,
                        "deg": 272,
                        "gust": 8.12
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 2.05
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 00:00:00"
                },
                {
                    "dt": 1683860400,
                    "main": {
                        "temp": 0.09,
                        "feels_like": -4.26,
                        "temp_min": 0.09,
                        "temp_max": 0.09,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 718,
                        "humidity": 93,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13n"
                        }
                    ],
                    "clouds": {
                        "all": 92
                    },
                    "wind": {
                        "speed": 4.13,
                        "deg": 267,
                        "gust": 6.34
                    },
                    "visibility": 5899,
                    "pop": 0.42,
                    "snow": {
                        "3h": 0.28
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 03:00:00"
                },
                {
                    "dt": 1683871200,
                    "main": {
                        "temp": 0.36,
                        "feels_like": -3.77,
                        "temp_min": 0.36,
                        "temp_max": 0.36,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 719,
                        "humidity": 94,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13n"
                        }
                    ],
                    "clouds": {
                        "all": 96
                    },
                    "wind": {
                        "speed": 3.9,
                        "deg": 268,
                        "gust": 6.21
                    },
                    "visibility": 4943,
                    "pop": 0.42,
                    "snow": {
                        "3h": 0.2
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 06:00:00"
                },
                {
                    "dt": 1683882000,
                    "main": {
                        "temp": 0.58,
                        "feels_like": -3.85,
                        "temp_min": 0.58,
                        "temp_max": 0.58,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 719,
                        "humidity": 91,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.43,
                        "deg": 273,
                        "gust": 9.35
                    },
                    "visibility": 10000,
                    "pop": 0.35,
                    "snow": {
                        "3h": 0.26
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 09:00:00"
                },
                {
                    "dt": 1683892800,
                    "main": {
                        "temp": 0.6,
                        "feels_like": -3.78,
                        "temp_min": 0.6,
                        "temp_max": 0.6,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 720,
                        "humidity": 88,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.35,
                        "deg": 271,
                        "gust": 9.56
                    },
                    "visibility": 10000,
                    "pop": 0.35,
                    "snow": {
                        "3h": 0.25
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 12:00:00"
                },
                {
                    "dt": 1683903600,
                    "main": {
                        "temp": 3.01,
                        "feels_like": -0.64,
                        "temp_min": 3.01,
                        "temp_max": 3.01,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 723,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.09,
                        "deg": 272,
                        "gust": 6.81
                    },
                    "visibility": 10000,
                    "pop": 0.27,
                    "rain": {
                        "3h": 0.23
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 15:00:00"
                },
                {
                    "dt": 1683914400,
                    "main": {
                        "temp": 5.78,
                        "feels_like": 3.11,
                        "temp_min": 5.78,
                        "temp_max": 5.78,
                        "pressure": 1017,
                        "sea_level": 1017,
                        "grnd_level": 726,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.51,
                        "deg": 277,
                        "gust": 5.66
                    },
                    "visibility": 10000,
                    "pop": 0.31,
                    "rain": {
                        "3h": 0.14
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 18:00:00"
                },
                {
                    "dt": 1683925200,
                    "main": {
                        "temp": 7.38,
                        "feels_like": 5.64,
                        "temp_min": 7.38,
                        "temp_max": 7.38,
                        "pressure": 1017,
                        "sea_level": 1017,
                        "grnd_level": 727,
                        "humidity": 64,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 97
                    },
                    "wind": {
                        "speed": 2.61,
                        "deg": 278,
                        "gust": 4.2
                    },
                    "visibility": 10000,
                    "pop": 0.41,
                    "rain": {
                        "3h": 0.17
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 21:00:00"
                },
                {
                    "dt": 1683936000,
                    "main": {
                        "temp": 6.35,
                        "feels_like": 4.9,
                        "temp_min": 6.35,
                        "temp_max": 6.35,
                        "pressure": 1018,
                        "sea_level": 1018,
                        "grnd_level": 727,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 94
                    },
                    "wind": {
                        "speed": 2.04,
                        "deg": 266,
                        "gust": 3.37
                    },
                    "visibility": 10000,
                    "pop": 0.38,
                    "rain": {
                        "3h": 0.14
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 00:00:00"
                },
                {
                    "dt": 1683946800,
                    "main": {
                        "temp": 1.35,
                        "feels_like": -0.43,
                        "temp_min": 1.35,
                        "temp_max": 1.35,
                        "pressure": 1023,
                        "sea_level": 1023,
                        "grnd_level": 726,
                        "humidity": 88,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 97
                    },
                    "wind": {
                        "speed": 1.65,
                        "deg": 261,
                        "gust": 1.94
                    },
                    "visibility": 10000,
                    "pop": 0.04,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 03:00:00"
                },
                {
                    "dt": 1683957600,
                    "main": {
                        "temp": -1.53,
                        "feels_like": -4.88,
                        "temp_min": -1.53,
                        "temp_max": -1.53,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 726,
                        "humidity": 85,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 89
                    },
                    "wind": {
                        "speed": 2.54,
                        "deg": 292,
                        "gust": 2.02
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 06:00:00"
                },
                {
                    "dt": 1683968400,
                    "main": {
                        "temp": -1.42,
                        "feels_like": -3.84,
                        "temp_min": -1.42,
                        "temp_max": -1.42,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 726,
                        "humidity": 84,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 52
                    },
                    "wind": {
                        "speed": 1.8,
                        "deg": 281,
                        "gust": 1.83
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 09:00:00"
                },
                {
                    "dt": 1683979200,
                    "main": {
                        "temp": -1.77,
                        "feels_like": -1.77,
                        "temp_min": -1.77,
                        "temp_max": -1.77,
                        "pressure": 1027,
                        "sea_level": 1027,
                        "grnd_level": 726,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 56
                    },
                    "wind": {
                        "speed": 1.04,
                        "deg": 269,
                        "gust": 1.09
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 12:00:00"
                },
                {
                    "dt": 1683990000,
                    "main": {
                        "temp": 3.93,
                        "feels_like": 1.71,
                        "temp_min": 3.93,
                        "temp_max": 3.93,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 730,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 85
                    },
                    "wind": {
                        "speed": 2.41,
                        "deg": 87,
                        "gust": 1.84
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 15:00:00"
                },
                {
                    "dt": 1684000800,
                    "main": {
                        "temp": 3.6,
                        "feels_like": 1.24,
                        "temp_min": 3.6,
                        "temp_max": 3.6,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 730,
                        "humidity": 84,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 91
                    },
                    "wind": {
                        "speed": 2.5,
                        "deg": 100,
                        "gust": 2.13
                    },
                    "visibility": 6147,
                    "pop": 0.2,
                    "rain": {
                        "3h": 0.16
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 18:00:00"
                },
                {
                    "dt": 1684011600,
                    "main": {
                        "temp": 2.62,
                        "feels_like": 0.34,
                        "temp_min": 2.62,
                        "temp_max": 2.62,
                        "pressure": 1027,
                        "sea_level": 1027,
                        "grnd_level": 730,
                        "humidity": 95,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.24,
                        "deg": 91,
                        "gust": 2.39
                    },
                    "visibility": 536,
                    "pop": 0.3,
                    "rain": {
                        "3h": 0.34
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 21:00:00"
                },
                {
                    "dt": 1684022400,
                    "main": {
                        "temp": 2.21,
                        "feels_like": 0.12,
                        "temp_min": 2.21,
                        "temp_max": 2.21,
                        "pressure": 1027,
                        "sea_level": 1027,
                        "grnd_level": 730,
                        "humidity": 97,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2,
                        "deg": 93,
                        "gust": 2.35
                    },
                    "visibility": 445,
                    "pop": 0.31,
                    "rain": {
                        "3h": 0.2
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-14 00:00:00"
                },
                {
                    "dt": 1684033200,
                    "main": {
                        "temp": 1.78,
                        "feels_like": -0.35,
                        "temp_min": 1.78,
                        "temp_max": 1.78,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 731,
                        "humidity": 99,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.97,
                        "deg": 96,
                        "gust": 2.2
                    },
                    "visibility": 430,
                    "pop": 0.49,
                    "rain": {
                        "3h": 0.49
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 03:00:00"
                },
                {
                    "dt": 1684044000,
                    "main": {
                        "temp": 1.41,
                        "feels_like": 1.41,
                        "temp_min": 1.41,
                        "temp_max": 1.41,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 731,
                        "humidity": 99,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.31,
                        "deg": 94,
                        "gust": 1.33
                    },
                    "visibility": 412,
                    "pop": 0.64,
                    "rain": {
                        "3h": 0.56
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 06:00:00"
                },
                {
                    "dt": 1684054800,
                    "main": {
                        "temp": 1.07,
                        "feels_like": -0.5,
                        "temp_min": 1.07,
                        "temp_max": 1.07,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 731,
                        "humidity": 99,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.48,
                        "deg": 84,
                        "gust": 1.7
                    },
                    "visibility": 60,
                    "pop": 0.56,
                    "snow": {
                        "3h": 0.37
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 09:00:00"
                }
            ],
            "city": {
                "id": 5583173,
                "name": "Ward",
                "coord": {
                    "lat": 40.0725,
                    "lon": -105.5138
                },
                "country": "US",
                "population": 150,
                "timezone": -21600,
                "sunrise": 1683633169,
                "sunset": 1683684253
            }
        }
    },
    {
        "Point(2): 'lng':-105.34078415422385, 'lat': 40.22726355493182": {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                    "dt": 1683633600,
                    "main": {
                        "temp": 6.32,
                        "feels_like": 4.57,
                        "temp_min": 5.83,
                        "temp_max": 6.32,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 810,
                        "humidity": 67,
                        "temp_kf": 0.49
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 1
                    },
                    "wind": {
                        "speed": 2.37,
                        "deg": 285,
                        "gust": 2.04
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 12:00:00"
                },
                {
                    "dt": 1683644400,
                    "main": {
                        "temp": 11.98,
                        "feels_like": 10.49,
                        "temp_min": 11.98,
                        "temp_max": 14.69,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 814,
                        "humidity": 48,
                        "temp_kf": -2.71
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 0
                    },
                    "wind": {
                        "speed": 0.54,
                        "deg": 135,
                        "gust": 2.77
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 15:00:00"
                },
                {
                    "dt": 1683655200,
                    "main": {
                        "temp": 19.18,
                        "feels_like": 17.91,
                        "temp_min": 19.18,
                        "temp_max": 19.18,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 815,
                        "humidity": 29,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 7
                    },
                    "wind": {
                        "speed": 3.44,
                        "deg": 101,
                        "gust": 4.8
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 18:00:00"
                },
                {
                    "dt": 1683666000,
                    "main": {
                        "temp": 19.02,
                        "feels_like": 17.87,
                        "temp_min": 19.02,
                        "temp_max": 19.02,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 815,
                        "humidity": 34,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 94
                    },
                    "wind": {
                        "speed": 2.15,
                        "deg": 189,
                        "gust": 4.08
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 21:00:00"
                },
                {
                    "dt": 1683676800,
                    "main": {
                        "temp": 18.21,
                        "feels_like": 17,
                        "temp_min": 18.21,
                        "temp_max": 18.21,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 814,
                        "humidity": 35,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 88
                    },
                    "wind": {
                        "speed": 2.34,
                        "deg": 220,
                        "gust": 4.08
                    },
                    "visibility": 10000,
                    "pop": 0.24,
                    "rain": {
                        "3h": 0.27
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 00:00:00"
                },
                {
                    "dt": 1683687600,
                    "main": {
                        "temp": 12.07,
                        "feels_like": 10.59,
                        "temp_min": 12.07,
                        "temp_max": 12.07,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 812,
                        "humidity": 48,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.6,
                        "deg": 277,
                        "gust": 2.98
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 03:00:00"
                },
                {
                    "dt": 1683698400,
                    "main": {
                        "temp": 8.63,
                        "feels_like": 8.63,
                        "temp_min": 8.63,
                        "temp_max": 8.63,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 812,
                        "humidity": 66,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 82
                    },
                    "wind": {
                        "speed": 1.32,
                        "deg": 233,
                        "gust": 1.48
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 06:00:00"
                },
                {
                    "dt": 1683709200,
                    "main": {
                        "temp": 7.47,
                        "feels_like": 6.8,
                        "temp_min": 7.47,
                        "temp_max": 7.47,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 811,
                        "humidity": 78,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01n"
                        }
                    ],
                    "clouds": {
                        "all": 2
                    },
                    "wind": {
                        "speed": 1.47,
                        "deg": 284,
                        "gust": 1.35
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 09:00:00"
                },
                {
                    "dt": 1683720000,
                    "main": {
                        "temp": 7.29,
                        "feels_like": 5.95,
                        "temp_min": 7.29,
                        "temp_max": 7.29,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 810,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "clouds": {
                        "all": 11
                    },
                    "wind": {
                        "speed": 2.09,
                        "deg": 273,
                        "gust": 1.73
                    },
                    "visibility": 10000,
                    "pop": 0.03,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 12:00:00"
                },
                {
                    "dt": 1683730800,
                    "main": {
                        "temp": 13.45,
                        "feels_like": 12.42,
                        "temp_min": 13.45,
                        "temp_max": 13.45,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 813,
                        "humidity": 60,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 8
                    },
                    "wind": {
                        "speed": 2.25,
                        "deg": 99,
                        "gust": 1.95
                    },
                    "visibility": 10000,
                    "pop": 0.2,
                    "rain": {
                        "3h": 0.18
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 15:00:00"
                },
                {
                    "dt": 1683741600,
                    "main": {
                        "temp": 17.31,
                        "feels_like": 16.4,
                        "temp_min": 17.31,
                        "temp_max": 17.31,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 812,
                        "humidity": 50,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 21
                    },
                    "wind": {
                        "speed": 3.44,
                        "deg": 106,
                        "gust": 4.1
                    },
                    "visibility": 10000,
                    "pop": 0.36,
                    "rain": {
                        "3h": 0.68
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 18:00:00"
                },
                {
                    "dt": 1683752400,
                    "main": {
                        "temp": 17.67,
                        "feels_like": 16.88,
                        "temp_min": 17.67,
                        "temp_max": 17.67,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 809,
                        "humidity": 53,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.23,
                        "deg": 99,
                        "gust": 4.67
                    },
                    "visibility": 10000,
                    "pop": 0.56,
                    "rain": {
                        "3h": 2.36
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 21:00:00"
                },
                {
                    "dt": 1683763200,
                    "main": {
                        "temp": 11.27,
                        "feels_like": 10.59,
                        "temp_min": 11.27,
                        "temp_max": 11.27,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 807,
                        "humidity": 82,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 2.08,
                        "deg": 331,
                        "gust": 2.72
                    },
                    "visibility": 10000,
                    "pop": 0.96,
                    "rain": {
                        "3h": 6.16
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 00:00:00"
                },
                {
                    "dt": 1683774000,
                    "main": {
                        "temp": 9.16,
                        "feels_like": 8.7,
                        "temp_min": 9.16,
                        "temp_max": 9.16,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 807,
                        "humidity": 93,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.49,
                        "deg": 356,
                        "gust": 3.02
                    },
                    "visibility": 10000,
                    "pop": 0.96,
                    "rain": {
                        "3h": 0.89
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 03:00:00"
                },
                {
                    "dt": 1683784800,
                    "main": {
                        "temp": 9.66,
                        "feels_like": 9.66,
                        "temp_min": 9.66,
                        "temp_max": 9.66,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 806,
                        "humidity": 90,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 1.28,
                        "deg": 350,
                        "gust": 1.83
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 1.94
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 06:00:00"
                },
                {
                    "dt": 1683795600,
                    "main": {
                        "temp": 8.55,
                        "feels_like": 7.3,
                        "temp_min": 8.55,
                        "temp_max": 8.55,
                        "pressure": 1003,
                        "sea_level": 1003,
                        "grnd_level": 803,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 84
                    },
                    "wind": {
                        "speed": 2.24,
                        "deg": 333,
                        "gust": 3.32
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 1.46
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 09:00:00"
                },
                {
                    "dt": 1683806400,
                    "main": {
                        "temp": 7.88,
                        "feels_like": 5.77,
                        "temp_min": 7.88,
                        "temp_max": 7.88,
                        "pressure": 1002,
                        "sea_level": 1002,
                        "grnd_level": 802,
                        "humidity": 84,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 92
                    },
                    "wind": {
                        "speed": 3.32,
                        "deg": 321,
                        "gust": 4.25
                    },
                    "visibility": 7547,
                    "pop": 1,
                    "rain": {
                        "3h": 3.97
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 12:00:00"
                },
                {
                    "dt": 1683817200,
                    "main": {
                        "temp": 10.98,
                        "feels_like": 10.01,
                        "temp_min": 10.98,
                        "temp_max": 10.98,
                        "pressure": 1003,
                        "sea_level": 1003,
                        "grnd_level": 804,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.71,
                        "deg": 349,
                        "gust": 7.08
                    },
                    "visibility": 4251,
                    "pop": 1,
                    "rain": {
                        "3h": 3.2
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 15:00:00"
                },
                {
                    "dt": 1683828000,
                    "main": {
                        "temp": 9.89,
                        "feels_like": 8.41,
                        "temp_min": 9.89,
                        "temp_max": 9.89,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 805,
                        "humidity": 80,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.94,
                        "deg": 334,
                        "gust": 5.26
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 6.2
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 18:00:00"
                },
                {
                    "dt": 1683838800,
                    "main": {
                        "temp": 6.87,
                        "feels_like": 5.09,
                        "temp_min": 6.87,
                        "temp_max": 6.87,
                        "pressure": 1009,
                        "sea_level": 1009,
                        "grnd_level": 806,
                        "humidity": 94,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.53,
                        "deg": 268,
                        "gust": 3.15
                    },
                    "visibility": 1816,
                    "pop": 1,
                    "rain": {
                        "3h": 5.68
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 21:00:00"
                },
                {
                    "dt": 1683849600,
                    "main": {
                        "temp": 9.5,
                        "feels_like": 8.63,
                        "temp_min": 9.5,
                        "temp_max": 9.5,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 808,
                        "humidity": 77,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 93
                    },
                    "wind": {
                        "speed": 1.97,
                        "deg": 306,
                        "gust": 4.1
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 4.51
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 00:00:00"
                },
                {
                    "dt": 1683860400,
                    "main": {
                        "temp": 6.66,
                        "feels_like": 4.22,
                        "temp_min": 6.66,
                        "temp_max": 6.66,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 809,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 78
                    },
                    "wind": {
                        "speed": 3.43,
                        "deg": 266,
                        "gust": 3.62
                    },
                    "visibility": 10000,
                    "pop": 0.38,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 03:00:00"
                },
                {
                    "dt": 1683871200,
                    "main": {
                        "temp": 6.78,
                        "feels_like": 4.86,
                        "temp_min": 6.78,
                        "temp_max": 6.78,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 810,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 81
                    },
                    "wind": {
                        "speed": 2.69,
                        "deg": 278,
                        "gust": 2.91
                    },
                    "visibility": 10000,
                    "pop": 0.31,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 06:00:00"
                },
                {
                    "dt": 1683882000,
                    "main": {
                        "temp": 6.05,
                        "feels_like": 3.45,
                        "temp_min": 6.05,
                        "temp_max": 6.05,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 809,
                        "humidity": 81,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.49,
                        "deg": 271,
                        "gust": 3.76
                    },
                    "visibility": 10000,
                    "pop": 0.27,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 09:00:00"
                },
                {
                    "dt": 1683892800,
                    "main": {
                        "temp": 5.68,
                        "feels_like": 3.01,
                        "temp_min": 5.68,
                        "temp_max": 5.68,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 810,
                        "humidity": 81,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 3.46,
                        "deg": 273,
                        "gust": 3.57
                    },
                    "visibility": 10000,
                    "pop": 0.27,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 12:00:00"
                },
                {
                    "dt": 1683903600,
                    "main": {
                        "temp": 10.86,
                        "feels_like": 9.65,
                        "temp_min": 10.86,
                        "temp_max": 10.86,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 813,
                        "humidity": 63,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.48,
                        "deg": 269,
                        "gust": 3.23
                    },
                    "visibility": 10000,
                    "pop": 0.21,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 15:00:00"
                },
                {
                    "dt": 1683914400,
                    "main": {
                        "temp": 13.92,
                        "feels_like": 12.78,
                        "temp_min": 13.92,
                        "temp_max": 13.92,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 815,
                        "humidity": 54,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 0.7,
                        "deg": 313,
                        "gust": 3.76
                    },
                    "visibility": 10000,
                    "pop": 0.23,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 18:00:00"
                },
                {
                    "dt": 1683925200,
                    "main": {
                        "temp": 15.07,
                        "feels_like": 13.94,
                        "temp_min": 15.07,
                        "temp_max": 15.07,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 816,
                        "humidity": 50,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 97
                    },
                    "wind": {
                        "speed": 1.29,
                        "deg": 5,
                        "gust": 3.85
                    },
                    "visibility": 10000,
                    "pop": 0.27,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 21:00:00"
                },
                {
                    "dt": 1683936000,
                    "main": {
                        "temp": 13.67,
                        "feels_like": 12.58,
                        "temp_min": 13.67,
                        "temp_max": 13.67,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 816,
                        "humidity": 57,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 94
                    },
                    "wind": {
                        "speed": 0.73,
                        "deg": 359,
                        "gust": 3.75
                    },
                    "visibility": 10000,
                    "pop": 0.27,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 00:00:00"
                },
                {
                    "dt": 1683946800,
                    "main": {
                        "temp": 7.64,
                        "feels_like": 6.11,
                        "temp_min": 7.64,
                        "temp_max": 7.64,
                        "pressure": 1022,
                        "sea_level": 1022,
                        "grnd_level": 817,
                        "humidity": 73,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 79
                    },
                    "wind": {
                        "speed": 2.39,
                        "deg": 269,
                        "gust": 2.53
                    },
                    "visibility": 10000,
                    "pop": 0.04,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 03:00:00"
                },
                {
                    "dt": 1683957600,
                    "main": {
                        "temp": 7.34,
                        "feels_like": 6.45,
                        "temp_min": 7.34,
                        "temp_max": 7.34,
                        "pressure": 1023,
                        "sea_level": 1023,
                        "grnd_level": 818,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 87
                    },
                    "wind": {
                        "speed": 1.65,
                        "deg": 310,
                        "gust": 1.88
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 06:00:00"
                },
                {
                    "dt": 1683968400,
                    "main": {
                        "temp": 7.19,
                        "feels_like": 7.19,
                        "temp_min": 7.19,
                        "temp_max": 7.19,
                        "pressure": 1024,
                        "sea_level": 1024,
                        "grnd_level": 818,
                        "humidity": 71,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 66
                    },
                    "wind": {
                        "speed": 0.52,
                        "deg": 316,
                        "gust": 1.12
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 09:00:00"
                },
                {
                    "dt": 1683979200,
                    "main": {
                        "temp": 6.42,
                        "feels_like": 6.42,
                        "temp_min": 6.42,
                        "temp_max": 6.42,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 819,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 68
                    },
                    "wind": {
                        "speed": 1.01,
                        "deg": 239,
                        "gust": 1.26
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 12:00:00"
                },
                {
                    "dt": 1683990000,
                    "main": {
                        "temp": 9.72,
                        "feels_like": 8.6,
                        "temp_min": 9.72,
                        "temp_max": 9.72,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 821,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 94
                    },
                    "wind": {
                        "speed": 2.35,
                        "deg": 99,
                        "gust": 1.62
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 15:00:00"
                },
                {
                    "dt": 1684000800,
                    "main": {
                        "temp": 10.65,
                        "feels_like": 9.55,
                        "temp_min": 10.65,
                        "temp_max": 10.65,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 822,
                        "humidity": 68,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 96
                    },
                    "wind": {
                        "speed": 3.85,
                        "deg": 77,
                        "gust": 2.81
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 18:00:00"
                },
                {
                    "dt": 1684011600,
                    "main": {
                        "temp": 9.89,
                        "feels_like": 8.35,
                        "temp_min": 9.89,
                        "temp_max": 9.89,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 822,
                        "humidity": 76,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.05,
                        "deg": 81,
                        "gust": 2.99
                    },
                    "visibility": 10000,
                    "pop": 0.22,
                    "rain": {
                        "3h": 0.12
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 21:00:00"
                },
                {
                    "dt": 1684022400,
                    "main": {
                        "temp": 8.57,
                        "feels_like": 7.7,
                        "temp_min": 8.57,
                        "temp_max": 8.57,
                        "pressure": 1027,
                        "sea_level": 1027,
                        "grnd_level": 822,
                        "humidity": 83,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.81,
                        "deg": 79,
                        "gust": 2.39
                    },
                    "visibility": 10000,
                    "pop": 0.06,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-14 00:00:00"
                },
                {
                    "dt": 1684033200,
                    "main": {
                        "temp": 7.38,
                        "feels_like": 6.59,
                        "temp_min": 7.38,
                        "temp_max": 7.38,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 823,
                        "humidity": 91,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.56,
                        "deg": 76,
                        "gust": 2.3
                    },
                    "visibility": 10000,
                    "pop": 0.59,
                    "rain": {
                        "3h": 0.42
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 03:00:00"
                },
                {
                    "dt": 1684044000,
                    "main": {
                        "temp": 6.97,
                        "feels_like": 6.97,
                        "temp_min": 6.97,
                        "temp_max": 6.97,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 823,
                        "humidity": 95,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 0.89,
                        "deg": 41,
                        "gust": 2.15
                    },
                    "visibility": 10000,
                    "pop": 0.8,
                    "rain": {
                        "3h": 0.69
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 06:00:00"
                },
                {
                    "dt": 1684054800,
                    "main": {
                        "temp": 6.9,
                        "feels_like": 6.9,
                        "temp_min": 6.9,
                        "temp_max": 6.9,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 823,
                        "humidity": 93,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.17,
                        "deg": 24,
                        "gust": 2.47
                    },
                    "visibility": 10000,
                    "pop": 0.72,
                    "rain": {
                        "3h": 0.38
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 09:00:00"
                }
            ],
            "city": {
                "id": 5579453,
                "name": "Lyons",
                "coord": {
                    "lat": 40.2273,
                    "lon": -105.3408
                },
                "country": "US",
                "population": 2033,
                "timezone": -21600,
                "sunrise": 1683633106,
                "sunset": 1683684232
            }
        }
    },
    {
        "Point(3): 'lng':-104.6040184556157, 'lat': 40.34133275612021": {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                    "dt": 1683633600,
                    "main": {
                        "temp": 8.65,
                        "feels_like": 8.65,
                        "temp_min": 8.08,
                        "temp_max": 8.65,
                        "pressure": 1015,
                        "sea_level": 1015,
                        "grnd_level": 850,
                        "humidity": 83,
                        "temp_kf": 0.57
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 2
                    },
                    "wind": {
                        "speed": 1.25,
                        "deg": 39,
                        "gust": 1.53
                    },
                    "visibility": 10000,
                    "pop": 0.06,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 12:00:00"
                },
                {
                    "dt": 1683644400,
                    "main": {
                        "temp": 12.41,
                        "feels_like": 11.53,
                        "temp_min": 12.41,
                        "temp_max": 14.14,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 853,
                        "humidity": 70,
                        "temp_kf": -1.73
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 0
                    },
                    "wind": {
                        "speed": 2.34,
                        "deg": 322,
                        "gust": 2.62
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 15:00:00"
                },
                {
                    "dt": 1683655200,
                    "main": {
                        "temp": 20.91,
                        "feels_like": 20,
                        "temp_min": 20.91,
                        "temp_max": 20.91,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 854,
                        "humidity": 36,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 0
                    },
                    "wind": {
                        "speed": 2.54,
                        "deg": 95,
                        "gust": 2.31
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 18:00:00"
                },
                {
                    "dt": 1683666000,
                    "main": {
                        "temp": 24.52,
                        "feels_like": 23.68,
                        "temp_min": 24.52,
                        "temp_max": 24.52,
                        "pressure": 1007,
                        "sea_level": 1007,
                        "grnd_level": 853,
                        "humidity": 25,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 8
                    },
                    "wind": {
                        "speed": 4.58,
                        "deg": 123,
                        "gust": 5.37
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 21:00:00"
                },
                {
                    "dt": 1683676800,
                    "main": {
                        "temp": 23.73,
                        "feels_like": 22.86,
                        "temp_min": 23.73,
                        "temp_max": 23.73,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 852,
                        "humidity": 27,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 802,
                            "main": "Clouds",
                            "description": "scattered clouds",
                            "icon": "03d"
                        }
                    ],
                    "clouds": {
                        "all": 42
                    },
                    "wind": {
                        "speed": 2.21,
                        "deg": 344,
                        "gust": 1.87
                    },
                    "visibility": 10000,
                    "pop": 0.03,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 00:00:00"
                },
                {
                    "dt": 1683687600,
                    "main": {
                        "temp": 16.21,
                        "feels_like": 15.11,
                        "temp_min": 16.21,
                        "temp_max": 16.21,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 851,
                        "humidity": 47,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 89
                    },
                    "wind": {
                        "speed": 6.59,
                        "deg": 47,
                        "gust": 11.75
                    },
                    "visibility": 10000,
                    "pop": 0.01,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 03:00:00"
                },
                {
                    "dt": 1683698400,
                    "main": {
                        "temp": 12.42,
                        "feels_like": 11.47,
                        "temp_min": 12.42,
                        "temp_max": 12.42,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 852,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 56
                    },
                    "wind": {
                        "speed": 0.91,
                        "deg": 56,
                        "gust": 1.33
                    },
                    "visibility": 10000,
                    "pop": 0.37,
                    "rain": {
                        "3h": 0.19
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 06:00:00"
                },
                {
                    "dt": 1683709200,
                    "main": {
                        "temp": 11.02,
                        "feels_like": 10.08,
                        "temp_min": 11.02,
                        "temp_max": 11.02,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 851,
                        "humidity": 73,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 0
                    },
                    "wind": {
                        "speed": 2.25,
                        "deg": 337,
                        "gust": 2.39
                    },
                    "visibility": 10000,
                    "pop": 0.4,
                    "rain": {
                        "3h": 0.14
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 09:00:00"
                },
                {
                    "dt": 1683720000,
                    "main": {
                        "temp": 10.87,
                        "feels_like": 10.08,
                        "temp_min": 10.87,
                        "temp_max": 10.87,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 851,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 802,
                            "main": "Clouds",
                            "description": "scattered clouds",
                            "icon": "03d"
                        }
                    ],
                    "clouds": {
                        "all": 31
                    },
                    "wind": {
                        "speed": 2.33,
                        "deg": 57,
                        "gust": 2.66
                    },
                    "visibility": 10000,
                    "pop": 0.28,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 12:00:00"
                },
                {
                    "dt": 1683730800,
                    "main": {
                        "temp": 13.31,
                        "feels_like": 12.76,
                        "temp_min": 13.31,
                        "temp_max": 13.31,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 851,
                        "humidity": 79,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 88
                    },
                    "wind": {
                        "speed": 1.09,
                        "deg": 65,
                        "gust": 1.1
                    },
                    "visibility": 10000,
                    "pop": 0.2,
                    "rain": {
                        "3h": 0.14
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 15:00:00"
                },
                {
                    "dt": 1683741600,
                    "main": {
                        "temp": 17.38,
                        "feels_like": 16.74,
                        "temp_min": 17.38,
                        "temp_max": 17.38,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 851,
                        "humidity": 60,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 93
                    },
                    "wind": {
                        "speed": 3.26,
                        "deg": 127,
                        "gust": 3.92
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 18:00:00"
                },
                {
                    "dt": 1683752400,
                    "main": {
                        "temp": 21.38,
                        "feels_like": 20.8,
                        "temp_min": 21.38,
                        "temp_max": 21.38,
                        "pressure": 1003,
                        "sea_level": 1003,
                        "grnd_level": 848,
                        "humidity": 47,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 70
                    },
                    "wind": {
                        "speed": 5.57,
                        "deg": 97,
                        "gust": 6.56
                    },
                    "visibility": 10000,
                    "pop": 0.1,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 21:00:00"
                },
                {
                    "dt": 1683763200,
                    "main": {
                        "temp": 11.21,
                        "feels_like": 10.58,
                        "temp_min": 11.21,
                        "temp_max": 11.21,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 845,
                        "humidity": 84,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 66
                    },
                    "wind": {
                        "speed": 8.87,
                        "deg": 278,
                        "gust": 13.08
                    },
                    "visibility": 9495,
                    "pop": 0.81,
                    "rain": {
                        "3h": 2.55
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 00:00:00"
                },
                {
                    "dt": 1683774000,
                    "main": {
                        "temp": 12.67,
                        "feels_like": 12.26,
                        "temp_min": 12.67,
                        "temp_max": 12.67,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 847,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.65,
                        "deg": 143,
                        "gust": 6.53
                    },
                    "visibility": 10000,
                    "pop": 0.96,
                    "rain": {
                        "3h": 6.87
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 03:00:00"
                },
                {
                    "dt": 1683784800,
                    "main": {
                        "temp": 11.92,
                        "feels_like": 11.54,
                        "temp_min": 11.92,
                        "temp_max": 11.92,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 845,
                        "humidity": 91,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.06,
                        "deg": 23,
                        "gust": 2.99
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 3.76
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 06:00:00"
                },
                {
                    "dt": 1683795600,
                    "main": {
                        "temp": 10.23,
                        "feels_like": 9.82,
                        "temp_min": 10.23,
                        "temp_max": 10.23,
                        "pressure": 1002,
                        "sea_level": 1002,
                        "grnd_level": 842,
                        "humidity": 96,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 62
                    },
                    "wind": {
                        "speed": 4.29,
                        "deg": 56,
                        "gust": 9.13
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 2.37
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 09:00:00"
                },
                {
                    "dt": 1683806400,
                    "main": {
                        "temp": 11.09,
                        "feels_like": 10.68,
                        "temp_min": 11.09,
                        "temp_max": 11.09,
                        "pressure": 1000,
                        "sea_level": 1000,
                        "grnd_level": 841,
                        "humidity": 93,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 74
                    },
                    "wind": {
                        "speed": 5.13,
                        "deg": 56,
                        "gust": 8.3
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 4.27
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 12:00:00"
                },
                {
                    "dt": 1683817200,
                    "main": {
                        "temp": 14.78,
                        "feels_like": 14.12,
                        "temp_min": 14.78,
                        "temp_max": 14.78,
                        "pressure": 1000,
                        "sea_level": 1000,
                        "grnd_level": 842,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 66
                    },
                    "wind": {
                        "speed": 9.07,
                        "deg": 46,
                        "gust": 10.88
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 4.7
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 15:00:00"
                },
                {
                    "dt": 1683828000,
                    "main": {
                        "temp": 15.85,
                        "feels_like": 14.74,
                        "temp_min": 15.85,
                        "temp_max": 15.85,
                        "pressure": 1001,
                        "sea_level": 1001,
                        "grnd_level": 844,
                        "humidity": 48,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 74
                    },
                    "wind": {
                        "speed": 2.79,
                        "deg": 53,
                        "gust": 5.29
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 6.14
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 18:00:00"
                },
                {
                    "dt": 1683838800,
                    "main": {
                        "temp": 12.66,
                        "feels_like": 11.86,
                        "temp_min": 12.66,
                        "temp_max": 12.66,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 845,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 9.47,
                        "deg": 318,
                        "gust": 11.47
                    },
                    "visibility": 10000,
                    "pop": 0.76,
                    "rain": {
                        "3h": 1.76
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 21:00:00"
                },
                {
                    "dt": 1683849600,
                    "main": {
                        "temp": 12.04,
                        "feels_like": 11.1,
                        "temp_min": 12.04,
                        "temp_max": 12.04,
                        "pressure": 1007,
                        "sea_level": 1007,
                        "grnd_level": 847,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 10.52,
                        "deg": 321,
                        "gust": 13.33
                    },
                    "visibility": 10000,
                    "pop": 0.94,
                    "rain": {
                        "3h": 1.19
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 00:00:00"
                },
                {
                    "dt": 1683860400,
                    "main": {
                        "temp": 10.82,
                        "feels_like": 9.71,
                        "temp_min": 10.82,
                        "temp_max": 10.82,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 849,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 98
                    },
                    "wind": {
                        "speed": 8.84,
                        "deg": 337,
                        "gust": 14.87
                    },
                    "visibility": 10000,
                    "pop": 0.16,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 03:00:00"
                },
                {
                    "dt": 1683871200,
                    "main": {
                        "temp": 9.86,
                        "feels_like": 6.54,
                        "temp_min": 9.86,
                        "temp_max": 9.86,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 850,
                        "humidity": 71,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 88
                    },
                    "wind": {
                        "speed": 7.81,
                        "deg": 334,
                        "gust": 14.21
                    },
                    "visibility": 10000,
                    "pop": 0.08,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 06:00:00"
                },
                {
                    "dt": 1683882000,
                    "main": {
                        "temp": 9.13,
                        "feels_like": 7.06,
                        "temp_min": 9.13,
                        "temp_max": 9.13,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 849,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 82
                    },
                    "wind": {
                        "speed": 3.74,
                        "deg": 314,
                        "gust": 7.66
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 09:00:00"
                },
                {
                    "dt": 1683892800,
                    "main": {
                        "temp": 8.67,
                        "feels_like": 7.11,
                        "temp_min": 8.67,
                        "temp_max": 8.67,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 850,
                        "humidity": 76,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 87
                    },
                    "wind": {
                        "speed": 2.69,
                        "deg": 296,
                        "gust": 6.06
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 12:00:00"
                },
                {
                    "dt": 1683903600,
                    "main": {
                        "temp": 12.65,
                        "feels_like": 11.51,
                        "temp_min": 12.65,
                        "temp_max": 12.65,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 853,
                        "humidity": 59,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 2.85,
                        "deg": 309,
                        "gust": 5.54
                    },
                    "visibility": 10000,
                    "pop": 0.08,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 15:00:00"
                },
                {
                    "dt": 1683914400,
                    "main": {
                        "temp": 15.48,
                        "feels_like": 14.34,
                        "temp_min": 15.48,
                        "temp_max": 15.48,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 855,
                        "humidity": 48,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 7.53,
                        "deg": 335,
                        "gust": 9.63
                    },
                    "visibility": 10000,
                    "pop": 0.2,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 18:00:00"
                },
                {
                    "dt": 1683925200,
                    "main": {
                        "temp": 14.2,
                        "feels_like": 13.03,
                        "temp_min": 14.2,
                        "temp_max": 14.2,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 856,
                        "humidity": 52,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 11.8,
                        "deg": 339,
                        "gust": 14.28
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 21:00:00"
                },
                {
                    "dt": 1683936000,
                    "main": {
                        "temp": 12.09,
                        "feels_like": 10.92,
                        "temp_min": 12.09,
                        "temp_max": 12.09,
                        "pressure": 1018,
                        "sea_level": 1018,
                        "grnd_level": 856,
                        "humidity": 60,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 12.33,
                        "deg": 349,
                        "gust": 15.78
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 00:00:00"
                },
                {
                    "dt": 1683946800,
                    "main": {
                        "temp": 9.67,
                        "feels_like": 5.55,
                        "temp_min": 9.67,
                        "temp_max": 9.67,
                        "pressure": 1022,
                        "sea_level": 1022,
                        "grnd_level": 858,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 80
                    },
                    "wind": {
                        "speed": 11.08,
                        "deg": 337,
                        "gust": 16.01
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 03:00:00"
                },
                {
                    "dt": 1683957600,
                    "main": {
                        "temp": 10.01,
                        "feels_like": 8.79,
                        "temp_min": 10.01,
                        "temp_max": 10.01,
                        "pressure": 1022,
                        "sea_level": 1022,
                        "grnd_level": 859,
                        "humidity": 66,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 83
                    },
                    "wind": {
                        "speed": 8.27,
                        "deg": 329,
                        "gust": 12.7
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 06:00:00"
                },
                {
                    "dt": 1683968400,
                    "main": {
                        "temp": 9.52,
                        "feels_like": 6.17,
                        "temp_min": 9.52,
                        "temp_max": 9.52,
                        "pressure": 1023,
                        "sea_level": 1023,
                        "grnd_level": 859,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 7.55,
                        "deg": 331,
                        "gust": 11.64
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 09:00:00"
                },
                {
                    "dt": 1683979200,
                    "main": {
                        "temp": 9.33,
                        "feels_like": 6.5,
                        "temp_min": 9.33,
                        "temp_max": 9.33,
                        "pressure": 1024,
                        "sea_level": 1024,
                        "grnd_level": 860,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 98
                    },
                    "wind": {
                        "speed": 5.67,
                        "deg": 336,
                        "gust": 10.04
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 12:00:00"
                },
                {
                    "dt": 1683990000,
                    "main": {
                        "temp": 9.83,
                        "feels_like": 6.95,
                        "temp_min": 9.83,
                        "temp_max": 9.83,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 861,
                        "humidity": 68,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 6.23,
                        "deg": 343,
                        "gust": 9.01
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 15:00:00"
                },
                {
                    "dt": 1684000800,
                    "main": {
                        "temp": 9.95,
                        "feels_like": 7.14,
                        "temp_min": 9.95,
                        "temp_max": 9.95,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 862,
                        "humidity": 71,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 6.13,
                        "deg": 346,
                        "gust": 8.38
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 18:00:00"
                },
                {
                    "dt": 1684011600,
                    "main": {
                        "temp": 11.49,
                        "feels_like": 10.5,
                        "temp_min": 11.49,
                        "temp_max": 11.49,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 862,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.55,
                        "deg": 350,
                        "gust": 7.55
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 21:00:00"
                },
                {
                    "dt": 1684022400,
                    "main": {
                        "temp": 10.94,
                        "feels_like": 10,
                        "temp_min": 10.94,
                        "temp_max": 10.94,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 863,
                        "humidity": 73,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 6.31,
                        "deg": 8,
                        "gust": 7.86
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-14 00:00:00"
                },
                {
                    "dt": 1684033200,
                    "main": {
                        "temp": 9.02,
                        "feels_like": 6.62,
                        "temp_min": 9.02,
                        "temp_max": 9.02,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 864,
                        "humidity": 85,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.38,
                        "deg": 351,
                        "gust": 7.99
                    },
                    "visibility": 10000,
                    "pop": 0.47,
                    "rain": {
                        "3h": 0.3
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 03:00:00"
                },
                {
                    "dt": 1684044000,
                    "main": {
                        "temp": 8.63,
                        "feels_like": 6.32,
                        "temp_min": 8.63,
                        "temp_max": 8.63,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 864,
                        "humidity": 91,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.99,
                        "deg": 332,
                        "gust": 7.17
                    },
                    "visibility": 10000,
                    "pop": 0.87,
                    "rain": {
                        "3h": 1.39
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 06:00:00"
                },
                {
                    "dt": 1684054800,
                    "main": {
                        "temp": 8.51,
                        "feels_like": 6.17,
                        "temp_min": 8.51,
                        "temp_max": 8.51,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 864,
                        "humidity": 90,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4,
                        "deg": 331,
                        "gust": 7.27
                    },
                    "visibility": 10000,
                    "pop": 0.76,
                    "rain": {
                        "3h": 0.78
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 09:00:00"
                }
            ],
            "city": {
                "id": 5578683,
                "name": "Kersey",
                "coord": {
                    "lat": 40.3413,
                    "lon": -104.604
                },
                "country": "US",
                "population": 1454,
                "timezone": -21600,
                "sunrise": 1683632914,
                "sunset": 1683684071
            }
        }
    },
    {
        "Point(4): 'lng':-104.57182060865499, 'lat': 40.21398514216906": {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                    "dt": 1683633600,
                    "main": {
                        "temp": 8.79,
                        "feels_like": 8.79,
                        "temp_min": 8.16,
                        "temp_max": 8.79,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 852,
                        "humidity": 89,
                        "temp_kf": 0.63
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "clouds": {
                        "all": 17
                    },
                    "wind": {
                        "speed": 0.61,
                        "deg": 57,
                        "gust": 1.38
                    },
                    "visibility": 10000,
                    "pop": 0.05,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 12:00:00"
                },
                {
                    "dt": 1683644400,
                    "main": {
                        "temp": 12.36,
                        "feels_like": 11.56,
                        "temp_min": 12.36,
                        "temp_max": 13.99,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 855,
                        "humidity": 73,
                        "temp_kf": -1.63
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 7
                    },
                    "wind": {
                        "speed": 2.42,
                        "deg": 319,
                        "gust": 2.77
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 15:00:00"
                },
                {
                    "dt": 1683655200,
                    "main": {
                        "temp": 20.64,
                        "feels_like": 19.75,
                        "temp_min": 20.64,
                        "temp_max": 20.64,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 855,
                        "humidity": 38,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 0
                    },
                    "wind": {
                        "speed": 2.28,
                        "deg": 77,
                        "gust": 1.81
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 18:00:00"
                },
                {
                    "dt": 1683666000,
                    "main": {
                        "temp": 24.61,
                        "feels_like": 23.81,
                        "temp_min": 24.61,
                        "temp_max": 24.61,
                        "pressure": 1007,
                        "sea_level": 1007,
                        "grnd_level": 855,
                        "humidity": 26,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": {
                        "all": 6
                    },
                    "wind": {
                        "speed": 4.73,
                        "deg": 108,
                        "gust": 5.25
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-09 21:00:00"
                },
                {
                    "dt": 1683676800,
                    "main": {
                        "temp": 23.96,
                        "feels_like": 23.14,
                        "temp_min": 23.96,
                        "temp_max": 23.96,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 853,
                        "humidity": 28,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 802,
                            "main": "Clouds",
                            "description": "scattered clouds",
                            "icon": "03d"
                        }
                    ],
                    "clouds": {
                        "all": 34
                    },
                    "wind": {
                        "speed": 3.4,
                        "deg": 354,
                        "gust": 2.62
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 00:00:00"
                },
                {
                    "dt": 1683687600,
                    "main": {
                        "temp": 16.3,
                        "feels_like": 15.21,
                        "temp_min": 16.3,
                        "temp_max": 16.3,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 853,
                        "humidity": 47,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 81
                    },
                    "wind": {
                        "speed": 6.26,
                        "deg": 53,
                        "gust": 11.33
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 03:00:00"
                },
                {
                    "dt": 1683698400,
                    "main": {
                        "temp": 12.55,
                        "feels_like": 11.64,
                        "temp_min": 12.55,
                        "temp_max": 12.55,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 854,
                        "humidity": 68,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 46
                    },
                    "wind": {
                        "speed": 1.17,
                        "deg": 44,
                        "gust": 1.51
                    },
                    "visibility": 10000,
                    "pop": 0.38,
                    "rain": {
                        "3h": 0.23
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 06:00:00"
                },
                {
                    "dt": 1683709200,
                    "main": {
                        "temp": 11.16,
                        "feels_like": 10.26,
                        "temp_min": 11.16,
                        "temp_max": 11.16,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 853,
                        "humidity": 74,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 1
                    },
                    "wind": {
                        "speed": 2.53,
                        "deg": 330,
                        "gust": 2.84
                    },
                    "visibility": 10000,
                    "pop": 0.48,
                    "rain": {
                        "3h": 0.27
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-10 09:00:00"
                },
                {
                    "dt": 1683720000,
                    "main": {
                        "temp": 11.07,
                        "feels_like": 10.32,
                        "temp_min": 11.07,
                        "temp_max": 11.07,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 852,
                        "humidity": 80,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 802,
                            "main": "Clouds",
                            "description": "scattered clouds",
                            "icon": "03d"
                        }
                    ],
                    "clouds": {
                        "all": 37
                    },
                    "wind": {
                        "speed": 2.12,
                        "deg": 55,
                        "gust": 2.57
                    },
                    "visibility": 10000,
                    "pop": 0.36,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 12:00:00"
                },
                {
                    "dt": 1683730800,
                    "main": {
                        "temp": 13.49,
                        "feels_like": 12.93,
                        "temp_min": 13.49,
                        "temp_max": 13.49,
                        "pressure": 1011,
                        "sea_level": 1011,
                        "grnd_level": 853,
                        "humidity": 78,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 88
                    },
                    "wind": {
                        "speed": 1.04,
                        "deg": 42,
                        "gust": 0.88
                    },
                    "visibility": 10000,
                    "pop": 0.2,
                    "rain": {
                        "3h": 0.11
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 15:00:00"
                },
                {
                    "dt": 1683741600,
                    "main": {
                        "temp": 17.55,
                        "feels_like": 16.93,
                        "temp_min": 17.55,
                        "temp_max": 17.55,
                        "pressure": 1008,
                        "sea_level": 1008,
                        "grnd_level": 852,
                        "humidity": 60,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 92
                    },
                    "wind": {
                        "speed": 3.05,
                        "deg": 124,
                        "gust": 3.74
                    },
                    "visibility": 10000,
                    "pop": 0.01,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 18:00:00"
                },
                {
                    "dt": 1683752400,
                    "main": {
                        "temp": 22.19,
                        "feels_like": 21.64,
                        "temp_min": 22.19,
                        "temp_max": 22.19,
                        "pressure": 1002,
                        "sea_level": 1002,
                        "grnd_level": 850,
                        "humidity": 45,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 56
                    },
                    "wind": {
                        "speed": 6.49,
                        "deg": 89,
                        "gust": 7.81
                    },
                    "visibility": 10000,
                    "pop": 0.06,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-10 21:00:00"
                },
                {
                    "dt": 1683763200,
                    "main": {
                        "temp": 11.93,
                        "feels_like": 11.35,
                        "temp_min": 11.93,
                        "temp_max": 11.93,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 847,
                        "humidity": 83,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 57
                    },
                    "wind": {
                        "speed": 7.28,
                        "deg": 268,
                        "gust": 11.93
                    },
                    "visibility": 6728,
                    "pop": 0.84,
                    "rain": {
                        "3h": 1.93
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 00:00:00"
                },
                {
                    "dt": 1683774000,
                    "main": {
                        "temp": 12.87,
                        "feels_like": 12.48,
                        "temp_min": 12.87,
                        "temp_max": 12.87,
                        "pressure": 1006,
                        "sea_level": 1006,
                        "grnd_level": 848,
                        "humidity": 87,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 3.84,
                        "deg": 122,
                        "gust": 7.51
                    },
                    "visibility": 9502,
                    "pop": 0.96,
                    "rain": {
                        "3h": 8.25
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 03:00:00"
                },
                {
                    "dt": 1683784800,
                    "main": {
                        "temp": 12.07,
                        "feels_like": 11.68,
                        "temp_min": 12.07,
                        "temp_max": 12.07,
                        "pressure": 1004,
                        "sea_level": 1004,
                        "grnd_level": 846,
                        "humidity": 90,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 2.3,
                        "deg": 31,
                        "gust": 3.71
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 3.41
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 06:00:00"
                },
                {
                    "dt": 1683795600,
                    "main": {
                        "temp": 10.34,
                        "feels_like": 9.96,
                        "temp_min": 10.34,
                        "temp_max": 10.34,
                        "pressure": 1002,
                        "sea_level": 1002,
                        "grnd_level": 843,
                        "humidity": 97,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 49
                    },
                    "wind": {
                        "speed": 4.78,
                        "deg": 57,
                        "gust": 9.93
                    },
                    "visibility": 7997,
                    "pop": 1,
                    "rain": {
                        "3h": 2.99
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-11 09:00:00"
                },
                {
                    "dt": 1683806400,
                    "main": {
                        "temp": 11.35,
                        "feels_like": 10.97,
                        "temp_min": 11.35,
                        "temp_max": 11.35,
                        "pressure": 1000,
                        "sea_level": 1000,
                        "grnd_level": 843,
                        "humidity": 93,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 70
                    },
                    "wind": {
                        "speed": 5.28,
                        "deg": 63,
                        "gust": 8.56
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 3.74
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 12:00:00"
                },
                {
                    "dt": 1683817200,
                    "main": {
                        "temp": 15.23,
                        "feels_like": 14.48,
                        "temp_min": 15.23,
                        "temp_max": 15.23,
                        "pressure": 999,
                        "sea_level": 999,
                        "grnd_level": 844,
                        "humidity": 64,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 53
                    },
                    "wind": {
                        "speed": 8.5,
                        "deg": 53,
                        "gust": 10.26
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 4.37
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 15:00:00"
                },
                {
                    "dt": 1683828000,
                    "main": {
                        "temp": 16.46,
                        "feels_like": 15.28,
                        "temp_min": 16.46,
                        "temp_max": 16.46,
                        "pressure": 1000,
                        "sea_level": 1000,
                        "grnd_level": 845,
                        "humidity": 43,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 501,
                            "main": "Rain",
                            "description": "moderate rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 67
                    },
                    "wind": {
                        "speed": 2.7,
                        "deg": 40,
                        "gust": 4.95
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 4.51
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 18:00:00"
                },
                {
                    "dt": 1683838800,
                    "main": {
                        "temp": 12.58,
                        "feels_like": 11.77,
                        "temp_min": 12.58,
                        "temp_max": 12.58,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 847,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 9.65,
                        "deg": 307,
                        "gust": 11.6
                    },
                    "visibility": 10000,
                    "pop": 0.73,
                    "rain": {
                        "3h": 1.08
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-11 21:00:00"
                },
                {
                    "dt": 1683849600,
                    "main": {
                        "temp": 12.25,
                        "feels_like": 11.33,
                        "temp_min": 12.25,
                        "temp_max": 12.25,
                        "pressure": 1007,
                        "sea_level": 1007,
                        "grnd_level": 849,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 10.37,
                        "deg": 323,
                        "gust": 13.33
                    },
                    "visibility": 10000,
                    "pop": 0.9,
                    "rain": {
                        "3h": 1.14
                    },
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 00:00:00"
                },
                {
                    "dt": 1683860400,
                    "main": {
                        "temp": 11,
                        "feels_like": 9.88,
                        "temp_min": 11,
                        "temp_max": 11,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 851,
                        "humidity": 66,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 96
                    },
                    "wind": {
                        "speed": 8.82,
                        "deg": 344,
                        "gust": 14.7
                    },
                    "visibility": 10000,
                    "pop": 0.1,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 03:00:00"
                },
                {
                    "dt": 1683871200,
                    "main": {
                        "temp": 9.75,
                        "feels_like": 6.64,
                        "temp_min": 9.75,
                        "temp_max": 9.75,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 852,
                        "humidity": 72,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 84
                    },
                    "wind": {
                        "speed": 6.91,
                        "deg": 338,
                        "gust": 13.49
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 06:00:00"
                },
                {
                    "dt": 1683882000,
                    "main": {
                        "temp": 8.99,
                        "feels_like": 7.66,
                        "temp_min": 8.99,
                        "temp_max": 8.99,
                        "pressure": 1012,
                        "sea_level": 1012,
                        "grnd_level": 851,
                        "humidity": 74,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 71
                    },
                    "wind": {
                        "speed": 2.45,
                        "deg": 320,
                        "gust": 5.73
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-12 09:00:00"
                },
                {
                    "dt": 1683892800,
                    "main": {
                        "temp": 7.84,
                        "feels_like": 6.61,
                        "temp_min": 7.84,
                        "temp_max": 7.84,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 852,
                        "humidity": 83,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 81
                    },
                    "wind": {
                        "speed": 2.07,
                        "deg": 234,
                        "gust": 2.74
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 12:00:00"
                },
                {
                    "dt": 1683903600,
                    "main": {
                        "temp": 12.41,
                        "feels_like": 11.3,
                        "temp_min": 12.41,
                        "temp_max": 12.41,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 854,
                        "humidity": 61,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 0.83,
                        "deg": 189,
                        "gust": 1.33
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 15:00:00"
                },
                {
                    "dt": 1683914400,
                    "main": {
                        "temp": 16.55,
                        "feels_like": 15.44,
                        "temp_min": 16.55,
                        "temp_max": 16.55,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 857,
                        "humidity": 45,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.55,
                        "deg": 344,
                        "gust": 7.1
                    },
                    "visibility": 10000,
                    "pop": 0.12,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 18:00:00"
                },
                {
                    "dt": 1683925200,
                    "main": {
                        "temp": 15.3,
                        "feels_like": 14.17,
                        "temp_min": 15.3,
                        "temp_max": 15.3,
                        "pressure": 1016,
                        "sea_level": 1016,
                        "grnd_level": 858,
                        "humidity": 49,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 12.46,
                        "deg": 344,
                        "gust": 14.23
                    },
                    "visibility": 10000,
                    "pop": 0.02,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-12 21:00:00"
                },
                {
                    "dt": 1683936000,
                    "main": {
                        "temp": 12.36,
                        "feels_like": 11.19,
                        "temp_min": 12.36,
                        "temp_max": 12.36,
                        "pressure": 1018,
                        "sea_level": 1018,
                        "grnd_level": 858,
                        "humidity": 59,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 98
                    },
                    "wind": {
                        "speed": 12.48,
                        "deg": 355,
                        "gust": 15.99
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 00:00:00"
                },
                {
                    "dt": 1683946800,
                    "main": {
                        "temp": 9.77,
                        "feels_like": 5.67,
                        "temp_min": 9.77,
                        "temp_max": 9.77,
                        "pressure": 1022,
                        "sea_level": 1022,
                        "grnd_level": 860,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 72
                    },
                    "wind": {
                        "speed": 11.15,
                        "deg": 344,
                        "gust": 16.29
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 03:00:00"
                },
                {
                    "dt": 1683957600,
                    "main": {
                        "temp": 10.12,
                        "feels_like": 8.88,
                        "temp_min": 10.12,
                        "temp_max": 10.12,
                        "pressure": 1022,
                        "sea_level": 1022,
                        "grnd_level": 861,
                        "humidity": 65,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "broken clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 74
                    },
                    "wind": {
                        "speed": 8.53,
                        "deg": 333,
                        "gust": 13
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 06:00:00"
                },
                {
                    "dt": 1683968400,
                    "main": {
                        "temp": 9.78,
                        "feels_like": 6.52,
                        "temp_min": 9.78,
                        "temp_max": 9.78,
                        "pressure": 1023,
                        "sea_level": 1023,
                        "grnd_level": 861,
                        "humidity": 68,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 7.49,
                        "deg": 335,
                        "gust": 11.37
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-13 09:00:00"
                },
                {
                    "dt": 1683979200,
                    "main": {
                        "temp": 9.46,
                        "feels_like": 6.78,
                        "temp_min": 9.46,
                        "temp_max": 9.46,
                        "pressure": 1024,
                        "sea_level": 1024,
                        "grnd_level": 862,
                        "humidity": 68,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.37,
                        "deg": 341,
                        "gust": 9.71
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 12:00:00"
                },
                {
                    "dt": 1683990000,
                    "main": {
                        "temp": 10.07,
                        "feels_like": 8.88,
                        "temp_min": 10.07,
                        "temp_max": 10.07,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 863,
                        "humidity": 67,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 99
                    },
                    "wind": {
                        "speed": 6.26,
                        "deg": 348,
                        "gust": 8.52
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 15:00:00"
                },
                {
                    "dt": 1684000800,
                    "main": {
                        "temp": 10,
                        "feels_like": 7.21,
                        "temp_min": 10,
                        "temp_max": 10,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 864,
                        "humidity": 71,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 6.09,
                        "deg": 349,
                        "gust": 8.22
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 18:00:00"
                },
                {
                    "dt": 1684011600,
                    "main": {
                        "temp": 11.57,
                        "feels_like": 10.58,
                        "temp_min": 11.57,
                        "temp_max": 11.57,
                        "pressure": 1025,
                        "sea_level": 1025,
                        "grnd_level": 864,
                        "humidity": 69,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.42,
                        "deg": 344,
                        "gust": 7.56
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-13 21:00:00"
                },
                {
                    "dt": 1684022400,
                    "main": {
                        "temp": 11.13,
                        "feels_like": 10.23,
                        "temp_min": 11.13,
                        "temp_max": 11.13,
                        "pressure": 1026,
                        "sea_level": 1026,
                        "grnd_level": 864,
                        "humidity": 74,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 804,
                            "main": "Clouds",
                            "description": "overcast clouds",
                            "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.95,
                        "deg": 8,
                        "gust": 7.57
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2023-05-14 00:00:00"
                },
                {
                    "dt": 1684033200,
                    "main": {
                        "temp": 9.25,
                        "feels_like": 6.86,
                        "temp_min": 9.25,
                        "temp_max": 9.25,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 866,
                        "humidity": 84,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.49,
                        "deg": 353,
                        "gust": 7.67
                    },
                    "visibility": 10000,
                    "pop": 0.45,
                    "rain": {
                        "3h": 0.21
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 03:00:00"
                },
                {
                    "dt": 1684044000,
                    "main": {
                        "temp": 8.65,
                        "feels_like": 6.29,
                        "temp_min": 8.65,
                        "temp_max": 8.65,
                        "pressure": 1030,
                        "sea_level": 1030,
                        "grnd_level": 866,
                        "humidity": 92,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.12,
                        "deg": 329,
                        "gust": 7.1
                    },
                    "visibility": 10000,
                    "pop": 0.89,
                    "rain": {
                        "3h": 1.34
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 06:00:00"
                },
                {
                    "dt": 1684054800,
                    "main": {
                        "temp": 8.59,
                        "feels_like": 6.24,
                        "temp_min": 8.59,
                        "temp_max": 8.59,
                        "pressure": 1029,
                        "sea_level": 1029,
                        "grnd_level": 866,
                        "humidity": 92,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.06,
                        "deg": 327,
                        "gust": 7.09
                    },
                    "visibility": 10000,
                    "pop": 0.81,
                    "rain": {
                        "3h": 0.91
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-05-14 09:00:00"
                }
            ],
            "city": {
                "id": 5578653,
                "name": "Keenesburg",
                "coord": {
                    "lat": 40.214,
                    "lon": -104.5718
                },
                "country": "US",
                "population": 1127,
                "timezone": -21600,
                "sunrise": 1683632924,
                "sunset": 1683684046
            }
        }
    }
]

```

### GET /weather-map/current-weather/specific-point

EndFragment

gets current weather for a specific point in the map.

#### `Request`

1.  **lat: 33.35887**
2.  lng:25.45588
    

#### `Example`

`Request:`

```
http://20.46.50.48:8090/weather-map/current-weather/specific-point?lat=32.15&lng=32.55

```

Response :

```json
{
    "coord": {
        "lon": 32.55,
        "lat": 32.15
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 19.07,
        "feels_like": 18.99,
        "temp_min": 19.07,
        "temp_max": 19.07,
        "pressure": 1014,
        "humidity": 75,
        "sea_level": 1014,
        "grnd_level": 1014
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.28,
        "deg": 29,
        "gust": 1.55
    },
    "clouds": {
        "all": 2
    },
    "dt": 1683628418,
    "sys": {
        "country": "EG",
        "sunrise": 1683601023,
        "sunset": 1683650129
    },
    "timezone": 10800,
    "id": 355392,
    "name": "Ezbet el-Burg",
    "cod": 200
}

```

## DEM Contour
Generates contour lines from a Digital Elevation Model (DEM) file.

**Endpoint:** `/dem-contour`

**Method:** GET

### Parameters

- `input_dem` (str): The path to the input DEM file.
- `elevation_interval` (float): The contour elevation interval.
### Request:
```
/dem-contour?input_dem=D:\Github\GIS\Land_use\wakeb_mapdata\ALPSMLC30_N021E039_DSM.tif&elevation_interval=100
```
### Response:

- `Status` (str): The status of the contour generation process. Possible values: "Contour produced" or error message.
- `file_path` (str): The absolute file path of the generated contour file (GeoJSON format).

#### Example:
```JSON
{
    "Status": "Contour produced",
    "file_path": "D:\\Github\\GIS\\Land_use\\wakeb_mapdata\\a89evnU5A4.geojson"
}
```
---

## Map Bound Contour

Generates contour lines from a specified map boundary.

**Endpoint:** `/mapBound-contour`

**Method:** GET

### Parameters

- `north` (float): The northern latitude coordinate of the map boundary.
- `south` (float): The southern latitude coordinate of the map boundary.
- `west` (float): The western longitude coordinate of the map boundary.
- `east` (float): The eastern longitude coordinate of the map boundary.
- `elevation_interval` (float): The contour elevation interval.
### Request:
```
/mapBound-contour?west=32.13973602505795&south=29.88397934934521&east=32.956926480302506&north=30.22656908627855&elevation_interval=100
```
### Response

Returns a GeoJSON representation of the contour lines.

#### Example:
```JSON
    {
    "type": "FeatureCollection",
    "features": [
        {
            "id": "0",
            "type": "Feature",
            "properties": {
                "ID": 0,
                "elev": 0.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.562500000305874,
                        30.22680555555147
                    ],
                    [
                        32.562500000305874,
                        30.22666666666258
                    ],
                    [
                        32.56277777780587,
                        30.22638888916258
                    ],
                    [
                        32.56305555558365,
                        30.226388889023692
                    ],
                    [
                        32.56324074076883,
                        30.22666666666258
                    ],
                    [
                        32.56324074076883,
                        30.22680555555147
                    ]
                ]
            }
        },
        {
            "id": "1",
            "type": "Feature",
            "properties": {
                "ID": 1,
                "elev": 100.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.34930555572251,
                        30.22680555555147
                    ],
                    [
                        32.34930555572251,
                        30.22666666666258
                    ],
                    [
                        32.34944444447251,
                        30.22638888916258
                    ],
                    [
                        32.349722222250286,
                        30.22638888916258
                    ],
                    [
                        32.35000000002807,
                        30.22652777791258
                    ],
                    [
                        32.35027777752807,
                        30.22666666666258
                    ],
                    [
                        32.35027777752807,
                        30.22680555555147
                    ]
                ]
            }
        },
        {
            "id": "2",
            "type": "Feature",
            "properties": {
                "ID": 2,
                "elev": 100.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.35027777808362,
                        30.22680555555147
                    ],
                    [
                        32.35027777808362,
                        30.22666666666258
                    ],
                    [
                        32.350555555583625,
                        30.22652777791258
                    ],
                    [
                        32.35083333308362,
                        30.22666666666258
                    ],
                    [
                        32.35083333308362,
                        30.22680555555147
                    ]
                ]   
            }
        }
    }
```
