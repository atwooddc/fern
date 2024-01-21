# This file was auto-generated by Fern from our API Definition.

from ....core.exceptions.fern_http_exception import FernHTTPException
from ..types.weather_report import WeatherReport
class ErrorWithEnumBody(FernHTTPException):
    def __init__(self, error: WeatherReport):
        super().__init__(status_code=400, name="ErrorWithEnumBody", content=error)
