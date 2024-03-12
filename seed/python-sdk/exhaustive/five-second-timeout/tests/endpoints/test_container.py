# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedExhaustive, SeedExhaustive
from seed.resources.types import ObjectWithRequiredField

from ..utilities import validate_response


async def test_get_and_return_list_of_primitives(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = ["string"]
    response = client.endpoints.container.get_and_return_list_of_primitives(request=["string"])
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_list_of_primitives(request=["string"])
    validate_response(async_response, expected_response)


async def test_get_and_return_list_of_objects(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = [{}]
    response = client.endpoints.container.get_and_return_list_of_objects(
        request=[ObjectWithRequiredField(string="string")]
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_list_of_objects(
        request=[ObjectWithRequiredField(string="string")]
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_set_of_primitives(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = ["string"]
    response = client.endpoints.container.get_and_return_set_of_primitives(request=["string"])
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_set_of_primitives(request=["string"])
    validate_response(async_response, expected_response)


async def test_get_and_return_set_of_objects(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = [{}]
    response = client.endpoints.container.get_and_return_set_of_objects(
        request=[ObjectWithRequiredField(string="string")]
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_set_of_objects(
        request=[ObjectWithRequiredField(string="string")]
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_map_prim_to_prim(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {"string": "string"}
    response = client.endpoints.container.get_and_return_map_prim_to_prim(request={"string": "string"})
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_map_prim_to_prim(
        request={"string": "string"}
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_map_of_prim_to_object(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {"string": {}}
    response = client.endpoints.container.get_and_return_map_of_prim_to_object(
        request={"string": ObjectWithRequiredField(string="string")}
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_map_of_prim_to_object(
        request={"string": ObjectWithRequiredField(string="string")}
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_optional(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {}
    response = client.endpoints.container.get_and_return_optional(request=ObjectWithRequiredField(string="string"))
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.container.get_and_return_optional(
        request=ObjectWithRequiredField(string="string")
    )
    validate_response(async_response, expected_response)
