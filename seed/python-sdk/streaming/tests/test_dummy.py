# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedStreaming, SeedStreaming

from .utilities import validate_response


async def test_generate_stream(client: SeedStreaming, async_client: AsyncSeedStreaming) -> None:
    expected_response = {}
    response = client.dummy.generate_stream(num_events=1)
    validate_response(response, expected_response)

    async_response = await async_client.dummy.generate_stream(num_events=1)
    validate_response(async_response, expected_response)
