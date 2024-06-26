# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..commons.binary_tree_node_value import BinaryTreeNodeValue
from ..commons.binary_tree_value import BinaryTreeValue
from ..commons.doubly_linked_list_node_value import DoublyLinkedListNodeValue
from ..commons.doubly_linked_list_value import DoublyLinkedListValue
from ..commons.node_id import NodeId
from ..commons.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ..commons.singly_linked_list_value import SinglyLinkedListValue
from .actual_result import ActualResult
from .error_info import ErrorInfo
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .running_submission_state import RunningSubmissionState
from .submission_status_for_test_case import SubmissionStatusForTestCase
from .test_case_grade import TestCaseGrade
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade
from .test_case_result import TestCaseResult
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase


class TestSubmissionStatus_Stopped(pydantic_v1.BaseModel):
    type: typing.Literal["stopped"] = "stopped"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class TestSubmissionStatus_Errored(pydantic_v1.BaseModel):
    value: ErrorInfo
    type: typing.Literal["errored"] = "errored"


class TestSubmissionStatus_Running(pydantic_v1.BaseModel):
    value: RunningSubmissionState
    type: typing.Literal["running"] = "running"


class TestSubmissionStatus_TestCaseIdToState(pydantic_v1.BaseModel):
    value: typing.Dict[str, SubmissionStatusForTestCase]
    type: typing.Literal["testCaseIdToState"] = "testCaseIdToState"


TestSubmissionStatus = typing.Union[
    TestSubmissionStatus_Stopped,
    TestSubmissionStatus_Errored,
    TestSubmissionStatus_Running,
    TestSubmissionStatus_TestCaseIdToState,
]
from ..commons.key_value_pair import KeyValuePair  # noqa: E402
from ..commons.map_value import MapValue  # noqa: E402
from ..commons.variable_value import VariableValue  # noqa: E402
