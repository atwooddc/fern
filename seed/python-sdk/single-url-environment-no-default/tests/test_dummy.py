# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedSingleUrlEnvironmentNoDefault, SeedSingleUrlEnvironmentNoDefault

from .utilities import validate_response


async def test_get_dummy(
    client: SeedSingleUrlEnvironmentNoDefault, async_client: AsyncSeedSingleUrlEnvironmentNoDefault
) -> None:
    expected_response = "string"
    response = client.dummy.get_dummy()
    validate_response(response, expected_response)

    async_response = await async_client.dummy.get_dummy()
    validate_response(async_response, expected_response)
