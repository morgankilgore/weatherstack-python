from typing import Dict, List, Optional, Type, Union

import requests

from weatherstack.exceptions import WeatherStackAPIError
from weatherstack.models import CurrentWeatherResponse


class WeatherStackClient:

    def __init__(self, api_key: str, https: bool = False) -> None:
        self.api_key = api_key
        self.https = https
        self.api_domain = 'api.weatherstack.com'

    @property
    def base_url(self) -> str:
        if self.https:
            base_url = 'https://'
        else:
            base_url = 'http://'

        return f'{base_url}{self.api_domain}'

    def get_base_payload(self) -> dict:
        return {'access_key': self.api_key}

    def get_current_weather(
            self,
            location: str,
            unit: str = 'm'
    ) -> CurrentWeatherResponse:
        params = self.get_base_payload()
        params.update({'query': location, 'units': unit})

        response = self.get_request(self.base_url + '/current', query_params=params)

        return self.deserialize_response(CurrentWeatherResponse, response)

    @classmethod
    def get_request(cls, url: str, query_params: Optional[Dict[str, str]]) -> dict:
        response = requests.get(url, params=query_params)
        response.raise_for_status()

        response_dict = response.json()
        cls.raise_weather_stack_exception(response_dict)

        return response_dict

    @staticmethod
    def deserialize_response(
            model_to: Union[Type[CurrentWeatherResponse]],
            response: dict
    ) -> Union[CurrentWeatherResponse]:
        return model_to(**response)

    @staticmethod
    def raise_weather_stack_exception(response: dict) -> None:
        success = response.get('success', True)
        error = response.get('error', {})

        if success is False and error:
            raise WeatherStackAPIError(
                code=error['code'],
                error_type=error['type'],
                info=error['info']
            )
