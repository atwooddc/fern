# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .deep_equality_correctness_check import DeepEqualityCorrectnessCheck
from .void_function_definition_that_takes_actual_result import VoidFunctionDefinitionThatTakesActualResult


class AssertCorrectnessCheck_DeepEquality(DeepEqualityCorrectnessCheck):
    type: typing.Literal["deepEquality"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class AssertCorrectnessCheck_Custom(VoidFunctionDefinitionThatTakesActualResult):
    type: typing.Literal["custom"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


AssertCorrectnessCheck = typing.Union[AssertCorrectnessCheck_DeepEquality, AssertCorrectnessCheck_Custom]
