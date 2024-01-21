# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ..commons.problem_id import ProblemId
from .create_problem_error import CreateProblemError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateProblemResponse_Success(pydantic.BaseModel):
    type: typing_extensions.Literal["success"]
    value: ProblemId


class CreateProblemResponse_Error(pydantic.BaseModel):
    type: typing_extensions.Literal["error"]
    value: CreateProblemError


CreateProblemResponse = typing.Union[CreateProblemResponse_Success, CreateProblemResponse_Error]
