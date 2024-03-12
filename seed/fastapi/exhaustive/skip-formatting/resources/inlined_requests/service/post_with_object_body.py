# This file was auto-generated by Fern from our API Definition.

from ...types.resources.object.types.object_with_optional_field import ObjectWithOptionalField
import typing
import datetime as dt
from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic # type: ignore
except ImportError:
    import pydantic # type: ignore
            
class PostWithObjectBody(pydantic.BaseModel):
    string: str
    integer: int
    nested_object: ObjectWithOptionalField = pydantic.Field(alias="NestedObject")
    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().json(**kwargs_with_defaults)
    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().dict(**kwargs_with_defaults)
    class Config:
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
