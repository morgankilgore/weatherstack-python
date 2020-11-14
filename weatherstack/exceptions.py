
class WeatherStackAPIError(Exception):

    def __init__(self, code: int, error_type: str, info: str):
        self.code = code
        self.error_type = error_type
        self.info = info
        super().__init__(self.info)

