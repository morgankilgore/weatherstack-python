from unittest import TestCase

import responses

from tests.fixtures import current_weather_responses
from weatherstack import WeatherStackClient
from weatherstack.exceptions import WeatherStackAPIError
from weatherstack.models import CurrentWeather, CurrentWeatherResponse, Request, Location


class WeatherStackClientTestCase(TestCase):
    def setUp(self) -> None:
        self.api_key = '123-test'
        self.client = WeatherStackClient(api_key=self.api_key)

    @responses.activate
    def test_get_current_weather_success(self):
        responses.add(
            responses.GET,
            f'http://{self.client.api_domain}/current',
            json=current_weather_responses.success_response
        )

        response = self.client.get_current_weather(location='houston, texas')

        self.assertIsInstance(response, CurrentWeatherResponse)

        with self.subTest('"request" field should be mapped to Request'):
            self.assertEqual(
                response.request,
                Request(**current_weather_responses.success_response['request'])
            )

        with self.subTest('"location" should be mapped to Location'):
            self.assertEqual(
                response.location,
                Location(**current_weather_responses.success_response['location'])
            )

        with self.subTest('"current" should be mapped to CurrentWeather'):
            self.assertEqual(
                response.current,
                CurrentWeather(**current_weather_responses.success_response['current'])
            )

    @responses.activate
    def test_get_current_weather_raises_weatherstack_api_exception(self):
        responses.add(
            responses.GET,
            f'http://{self.client.api_domain}/current',
            json=current_weather_responses.error_response
        )

        with self.assertRaises(WeatherStackAPIError) as ex:
            self.client.get_current_weather(location='austin, texas')

        self.assertEqual(ex.exception.code, current_weather_responses.error_response['error']['code'])
        self.assertEqual(ex.exception.error_type, current_weather_responses.error_response['error']['type'])
        self.assertEqual(ex.exception.info, current_weather_responses.error_response['error']['info'])

    def test_base_url(self):
        with self.subTest('should use http'):
            self.client.https = False
            self.assertEqual(self.client.base_url, f'http://{self.client.api_domain}')

        with self.subTest('should use https'):
            self.client.https = True
            self.assertEqual(self.client.base_url, f'https://{self.client.api_domain}')

    def test_get_base_payload(self):
        self.assertEqual(self.client.get_base_payload(), {'access_key': self.api_key})
