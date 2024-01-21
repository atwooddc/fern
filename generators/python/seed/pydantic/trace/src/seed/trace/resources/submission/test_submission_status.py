# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

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

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestSubmissionStatus_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]


class TestSubmissionStatus_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo


class TestSubmissionStatus_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState


class TestSubmissionStatus_TestCaseIdToState(pydantic.BaseModel):
    type: typing_extensions.Literal["testCaseIdToState"]
    value: typing.Dict[str, SubmissionStatusForTestCase]


TestSubmissionStatus = typing.Union[
    TestSubmissionStatus_Stopped,
    TestSubmissionStatus_Errored,
    TestSubmissionStatus_Running,
    TestSubmissionStatus_TestCaseIdToState,
]
from ..commons.key_value_pair import KeyValuePair  # noqa: E402
from ..commons.map_value import MapValue  # noqa: E402
from ..commons.variable_value import VariableValue  # noqa: E402
