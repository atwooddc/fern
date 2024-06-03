# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PrimitiveClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_and_return_string(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_string(
            request="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/string", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_int(self, *, request: int, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_int(
            request=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/integer", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(int, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_long(self, *, request: int, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_long(
            request=1000000,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/long", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(int, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_double(
        self, *, request: float, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        request : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_double(
            request=1.1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/double", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(float, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_bool(self, *, request: bool, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Parameters
        ----------
        request : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_bool(
            request=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/boolean", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(bool, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_datetime(
        self, *, request: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> dt.datetime:
        """
        Parameters
        ----------
        request : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dt.datetime

        Examples
        --------
        import datetime

        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_datetime(
            request=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/datetime", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(dt.datetime, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_date(
        self, *, request: dt.date, request_options: typing.Optional[RequestOptions] = None
    ) -> dt.date:
        """
        Parameters
        ----------
        request : dt.date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dt.date

        Examples
        --------
        import datetime

        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_date(
            request=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/date", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(dt.date, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_uuid(
        self, *, request: uuid.UUID, request_options: typing.Optional[RequestOptions] = None
    ) -> uuid.UUID:
        """
        Parameters
        ----------
        request : uuid.UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        uuid.UUID

        Examples
        --------
        import uuid

        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_uuid(
            request=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/uuid", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(uuid.UUID, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_base_64(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.primitive.get_and_return_base_64(
            request="SGVsbG8gd29ybGQh",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "primitive/base64", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPrimitiveClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_and_return_string(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_string(
            request="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/string", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_int(self, *, request: int, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_int(
            request=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/integer", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(int, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_long(
        self, *, request: int, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Parameters
        ----------
        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_long(
            request=1000000,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/long", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(int, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_double(
        self, *, request: float, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        request : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_double(
            request=1.1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/double", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(float, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_bool(
        self, *, request: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Parameters
        ----------
        request : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_bool(
            request=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/boolean", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(bool, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_datetime(
        self, *, request: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> dt.datetime:
        """
        Parameters
        ----------
        request : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dt.datetime

        Examples
        --------
        import datetime

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_datetime(
            request=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/datetime", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(dt.datetime, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_date(
        self, *, request: dt.date, request_options: typing.Optional[RequestOptions] = None
    ) -> dt.date:
        """
        Parameters
        ----------
        request : dt.date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dt.date

        Examples
        --------
        import datetime

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_date(
            request=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/date", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(dt.date, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_uuid(
        self, *, request: uuid.UUID, request_options: typing.Optional[RequestOptions] = None
    ) -> uuid.UUID:
        """
        Parameters
        ----------
        request : uuid.UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        uuid.UUID

        Examples
        --------
        import uuid

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_uuid(
            request=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/uuid", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(uuid.UUID, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_base_64(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.endpoints.primitive.get_and_return_base_64(
            request="SGVsbG8gd29ybGQh",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "primitive/base64", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
