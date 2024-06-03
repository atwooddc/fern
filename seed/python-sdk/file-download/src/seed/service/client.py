# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions


class ServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def download_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[bytes]

        Examples
        --------
        from seed.client import SeedFileDownload

        client = SeedFileDownload(
            base_url="https://yourhost.com/path/to/api",
        )
        client.service.download_file()
        """
        with self._client_wrapper.httpx_client.stream(method="POST", request_options=request_options) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def download_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[bytes]

        Examples
        --------
        from seed.client import AsyncSeedFileDownload

        client = AsyncSeedFileDownload(
            base_url="https://yourhost.com/path/to/api",
        )
        await client.service.download_file()
        """
        async with self._client_wrapper.httpx_client.stream(
            method="POST", request_options=request_options
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
