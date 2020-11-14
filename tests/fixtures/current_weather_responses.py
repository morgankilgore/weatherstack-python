success_response = {
    'request': {
        'type': 'City',
        'query': 'Austin, United States of America',
        'language': 'en',
        'unit': 'm'
    },
    'location': {
        'name': 'Austin',
        'country': 'United States of America',
        'region': 'Texas',
        'lat': '30.267',
        'lon': '-97.743',
        'timezone_id': 'America/Chicago',
        'localtime': '2020-11-07 17:28',
        'localtime_epoch': 1604770080,
        'utc_offset': '-6.0'
    },
    'current': {
        'observation_time': '11:28 PM',
        'temperature': 26,
        'weather_code': 113,
        'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'],
        'weather_descriptions': ['Sunny'],
        'wind_speed': 7,
        'wind_degree': 180,
        'wind_dir': 'S',
        'pressure': 1014,
        'precip': 0,
        'humidity': 40,
        'cloudcover': 0,
        'feelslike': 26,
        'uv_index': 7,
        'visibility': 16,
        'is_day': 'yes'
    }
}

error_response = {
    'success': False,
    'error': {
        'code': 615,
        'type': 'request_failed',
        'info': 'Your API request failed. Please try again or contact support.'
    }
}

