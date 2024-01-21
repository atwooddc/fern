# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid

import pydantic

from ...core.datetime_utils import serialize_datetime


class ObjectWithOptionalField(pydantic.BaseModel):
    string: typing.Optional[str]
    integer: typing.Optional[int]
    long: typing.Optional[int]
    double: typing.Optional[float]
    bool: typing.Optional[bool]
    datetime: typing.Optional[dt.datetime]
    date: typing.Optional[dt.date]
    uuid: typing.Optional[uuid.UUID]
    base_64: typing.Optional[str] = pydantic.Field(alias="base64")
    list: typing.Optional[typing.List[str]]
    set: typing.Optional[typing.Set[str]]
    map: typing.Optional[typing.Dict[int, str]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
