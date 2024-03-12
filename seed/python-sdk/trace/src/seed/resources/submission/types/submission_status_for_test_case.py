# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_case_grade import TestCaseGrade
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SubmissionStatusForTestCase_Graded(TestCaseResultWithStdout):
    type: typing.Literal["graded"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class SubmissionStatusForTestCase_GradedV2(pydantic.BaseModel):
    type: typing.Literal["gradedV2"]
    value: TestCaseGrade

    class Config:
        frozen = True
        smart_union = True


class SubmissionStatusForTestCase_Traced(TracedTestCase):
    type: typing.Literal["traced"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


SubmissionStatusForTestCase = typing.Union[
    SubmissionStatusForTestCase_Graded, SubmissionStatusForTestCase_GradedV2, SubmissionStatusForTestCase_Traced
]
