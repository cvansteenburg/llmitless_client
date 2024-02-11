from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_summarize_test import BodySummarizeTest
from ...models.http_validation_error import HTTPValidationError
from ...models.input_doc_format import InputDocFormat
from ...models.summarization_result import SummarizationResult
from ...models.summarize_test_scenarios import SummarizeTestScenarios
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: BodySummarizeTest,
    input_doc_format: InputDocFormat,
    test_scenario: SummarizeTestScenarios,
    api_key: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["api-key"] = api_key

    params: Dict[str, Any] = {}

    json_input_doc_format = input_doc_format.value
    params["input_doc_format"] = json_input_doc_format

    json_test_scenario = test_scenario.value
    params["test_scenario"] = json_test_scenario

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/summarize_test",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SummarizationResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SummarizationResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, SummarizationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodySummarizeTest,
    input_doc_format: InputDocFormat,
    test_scenario: SummarizeTestScenarios,
    api_key: str,
) -> Response[Union[HTTPValidationError, SummarizationResult]]:
    r"""Summarize Test

     Simulates various outcomes of a summarization request based on the test scenario provided.

    This endpoint is designed for testing client-side handling of different API responses. By specifying
    a `test_scenario` query parameter, you can simulate various outcomes, such as successful
    summarization, server errors, or authentication failures. This allows client developers to test
    their code against predictable responses without triggering actual backend logic.

    Parameters:
    - `test_scenario`: Optional query parameter to specify the simulation scenario.

    Returns:
    - `SummarizationResult`: The simulated result of the summarization request, including status and
    optionally summary, usage report, and debug information.

    Available scenarios include:
    - \"INAUTHENTICATED\": Simulates an authentication failure response NOTE: **you must send invalid
    credentials** to make this fail.
    - \"INVALID_REQUEST\": Simulates a response for an invalid request NOTE: **you must send an invalid
    request** to make this fail.
    - \"FORBIDDEN_CONTENT\": Simulates a response for forbidden content.
    - \"SERVER_ERROR\": Simulates a server error response.
    - \"SUCCESS_WITH_DUMMY_DATA\": Returns a successful response with summary and dummy data for other
    fields.
    - \"SUCCESS_WITH_NONE\": Returns a successful response with no summary or other data.
    - \"SUCCESS_WITH_SUMMARY_ONLY\": Returns a successful response with a summary.

    Args:
        input_doc_format (InputDocFormat):
        test_scenario (SummarizeTestScenarios):
        api_key (str): API key for the LLM. This test endpoint *WILL NOT VALIDATE* your key, other
            than to check that it is a valid string.
        body (BodySummarizeTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SummarizationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        input_doc_format=input_doc_format,
        test_scenario=test_scenario,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodySummarizeTest,
    input_doc_format: InputDocFormat,
    test_scenario: SummarizeTestScenarios,
    api_key: str,
) -> Optional[Union[HTTPValidationError, SummarizationResult]]:
    r"""Summarize Test

     Simulates various outcomes of a summarization request based on the test scenario provided.

    This endpoint is designed for testing client-side handling of different API responses. By specifying
    a `test_scenario` query parameter, you can simulate various outcomes, such as successful
    summarization, server errors, or authentication failures. This allows client developers to test
    their code against predictable responses without triggering actual backend logic.

    Parameters:
    - `test_scenario`: Optional query parameter to specify the simulation scenario.

    Returns:
    - `SummarizationResult`: The simulated result of the summarization request, including status and
    optionally summary, usage report, and debug information.

    Available scenarios include:
    - \"INAUTHENTICATED\": Simulates an authentication failure response NOTE: **you must send invalid
    credentials** to make this fail.
    - \"INVALID_REQUEST\": Simulates a response for an invalid request NOTE: **you must send an invalid
    request** to make this fail.
    - \"FORBIDDEN_CONTENT\": Simulates a response for forbidden content.
    - \"SERVER_ERROR\": Simulates a server error response.
    - \"SUCCESS_WITH_DUMMY_DATA\": Returns a successful response with summary and dummy data for other
    fields.
    - \"SUCCESS_WITH_NONE\": Returns a successful response with no summary or other data.
    - \"SUCCESS_WITH_SUMMARY_ONLY\": Returns a successful response with a summary.

    Args:
        input_doc_format (InputDocFormat):
        test_scenario (SummarizeTestScenarios):
        api_key (str): API key for the LLM. This test endpoint *WILL NOT VALIDATE* your key, other
            than to check that it is a valid string.
        body (BodySummarizeTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SummarizationResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        input_doc_format=input_doc_format,
        test_scenario=test_scenario,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodySummarizeTest,
    input_doc_format: InputDocFormat,
    test_scenario: SummarizeTestScenarios,
    api_key: str,
) -> Response[Union[HTTPValidationError, SummarizationResult]]:
    r"""Summarize Test

     Simulates various outcomes of a summarization request based on the test scenario provided.

    This endpoint is designed for testing client-side handling of different API responses. By specifying
    a `test_scenario` query parameter, you can simulate various outcomes, such as successful
    summarization, server errors, or authentication failures. This allows client developers to test
    their code against predictable responses without triggering actual backend logic.

    Parameters:
    - `test_scenario`: Optional query parameter to specify the simulation scenario.

    Returns:
    - `SummarizationResult`: The simulated result of the summarization request, including status and
    optionally summary, usage report, and debug information.

    Available scenarios include:
    - \"INAUTHENTICATED\": Simulates an authentication failure response NOTE: **you must send invalid
    credentials** to make this fail.
    - \"INVALID_REQUEST\": Simulates a response for an invalid request NOTE: **you must send an invalid
    request** to make this fail.
    - \"FORBIDDEN_CONTENT\": Simulates a response for forbidden content.
    - \"SERVER_ERROR\": Simulates a server error response.
    - \"SUCCESS_WITH_DUMMY_DATA\": Returns a successful response with summary and dummy data for other
    fields.
    - \"SUCCESS_WITH_NONE\": Returns a successful response with no summary or other data.
    - \"SUCCESS_WITH_SUMMARY_ONLY\": Returns a successful response with a summary.

    Args:
        input_doc_format (InputDocFormat):
        test_scenario (SummarizeTestScenarios):
        api_key (str): API key for the LLM. This test endpoint *WILL NOT VALIDATE* your key, other
            than to check that it is a valid string.
        body (BodySummarizeTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SummarizationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        input_doc_format=input_doc_format,
        test_scenario=test_scenario,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodySummarizeTest,
    input_doc_format: InputDocFormat,
    test_scenario: SummarizeTestScenarios,
    api_key: str,
) -> Optional[Union[HTTPValidationError, SummarizationResult]]:
    r"""Summarize Test

     Simulates various outcomes of a summarization request based on the test scenario provided.

    This endpoint is designed for testing client-side handling of different API responses. By specifying
    a `test_scenario` query parameter, you can simulate various outcomes, such as successful
    summarization, server errors, or authentication failures. This allows client developers to test
    their code against predictable responses without triggering actual backend logic.

    Parameters:
    - `test_scenario`: Optional query parameter to specify the simulation scenario.

    Returns:
    - `SummarizationResult`: The simulated result of the summarization request, including status and
    optionally summary, usage report, and debug information.

    Available scenarios include:
    - \"INAUTHENTICATED\": Simulates an authentication failure response NOTE: **you must send invalid
    credentials** to make this fail.
    - \"INVALID_REQUEST\": Simulates a response for an invalid request NOTE: **you must send an invalid
    request** to make this fail.
    - \"FORBIDDEN_CONTENT\": Simulates a response for forbidden content.
    - \"SERVER_ERROR\": Simulates a server error response.
    - \"SUCCESS_WITH_DUMMY_DATA\": Returns a successful response with summary and dummy data for other
    fields.
    - \"SUCCESS_WITH_NONE\": Returns a successful response with no summary or other data.
    - \"SUCCESS_WITH_SUMMARY_ONLY\": Returns a successful response with a summary.

    Args:
        input_doc_format (InputDocFormat):
        test_scenario (SummarizeTestScenarios):
        api_key (str): API key for the LLM. This test endpoint *WILL NOT VALIDATE* your key, other
            than to check that it is a valid string.
        body (BodySummarizeTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SummarizationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            input_doc_format=input_doc_format,
            test_scenario=test_scenario,
            api_key=api_key,
        )
    ).parsed
