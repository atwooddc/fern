# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedTrace, SeedTrace

from .utilities import validate_response


async def test_get_homepage_problems(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    expected_response = ["string"]
    response = client.homepage.get_homepage_problems()
    validate_response(response, expected_response)

    async_response = await async_client.homepage.get_homepage_problems()
    validate_response(async_response, expected_response)


async def test_set_homepage_problems(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.homepage.set_homepage_problems(request=["string"]) is None  # type: ignore[func-returns-value]

    assert await async_client.homepage.set_homepage_problems(request=["string"]) is None  # type: ignore[func-returns-value]
