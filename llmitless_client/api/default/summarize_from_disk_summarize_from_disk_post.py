from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_summarize_from_disk_summarize_from_disk_post import BodySummarizeFromDiskSummarizeFromDiskPost
from ...models.http_validation_error import HTTPValidationError
from ...models.summarization_result import SummarizationResult
from ...types import Response


def _get_kwargs(
    *,
    body: BodySummarizeFromDiskSummarizeFromDiskPost,
    api_key: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["api-key"] = api_key

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/summarize_from_disk",
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
    client: Union[AuthenticatedClient, Client],
    body: BodySummarizeFromDiskSummarizeFromDiskPost,
    api_key: str,
) -> Response[Union[HTTPValidationError, SummarizationResult]]:
    """Summarize From Disk

     Select and summarize a subset of files from a dataset on the server.

    Args:
        api_key (str): API key for the LLM. Default LLM is OpenAI
        body (BodySummarizeFromDiskSummarizeFromDiskPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SummarizationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodySummarizeFromDiskSummarizeFromDiskPost,
    api_key: str,
) -> Optional[Union[HTTPValidationError, SummarizationResult]]:
    """Summarize From Disk

     Select and summarize a subset of files from a dataset on the server.

    Args:
        api_key (str): API key for the LLM. Default LLM is OpenAI
        body (BodySummarizeFromDiskSummarizeFromDiskPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SummarizationResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodySummarizeFromDiskSummarizeFromDiskPost,
    api_key: str,
) -> Response[Union[HTTPValidationError, SummarizationResult]]:
    """Summarize From Disk

     Select and summarize a subset of files from a dataset on the server.

    Args:
        api_key (str): API key for the LLM. Default LLM is OpenAI
        body (BodySummarizeFromDiskSummarizeFromDiskPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SummarizationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodySummarizeFromDiskSummarizeFromDiskPost,
    api_key: str,
) -> Optional[Union[HTTPValidationError, SummarizationResult]]:
    """Summarize From Disk

     Select and summarize a subset of files from a dataset on the server.

    Args:
        api_key (str): API key for the LLM. Default LLM is OpenAI
        body (BodySummarizeFromDiskSummarizeFromDiskPost):

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
            api_key=api_key,
        )
    ).parsed
