# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .exception_info import ExceptionInfo

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def generic(self, value: ExceptionInfo) -> ExceptionV2:
        return ExceptionV2(__root__=_ExceptionV2.Generic(**value.dict(exclude_unset=True), type="generic"))

    def timeout(self) -> ExceptionV2:
        return ExceptionV2(__root__=_ExceptionV2.Timeout(type="timeout"))


class ExceptionV2(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ExceptionV2.Generic, _ExceptionV2.Timeout]:
        return self.__root__

    def visit(
        self, generic: typing.Callable[[ExceptionInfo], T_Result], timeout: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self.__root__.type == "generic":
            return generic(ExceptionInfo(**self.__root__.dict(exclude_unset=True, exclude={"type"})))
        if self.__root__.type == "timeout":
            return timeout()

    __root__: typing.Annotated[
        typing.Union[_ExceptionV2.Generic, _ExceptionV2.Timeout], pydantic.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _ExceptionV2:
    class Generic(ExceptionInfo):
        type: typing.Literal["generic"]

        class Config:
            allow_population_by_field_name = True
            populate_by_name = True

    class Timeout(pydantic.BaseModel):
        type: typing.Literal["timeout"]


ExceptionV2.update_forward_refs()
