from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummarizeMapReduce")


@_attrs_define
class SummarizeMapReduce:
    """
    Attributes:
        core_prompt (Union[None, Unset, str]): Provides a role, context, and instructions for the LLM. LLM will
            summarize the content using this prompt. This is a string with brackets around template variables. At a minimum,
            prompt should include page_content in brackets like this: {page_content} where the contents of each summarized
            document will be inserted.
        collapse_prompt (Union[None, Unset, str]): In a map-reduce summarization strategy, the LLM will summarize the
            summaries to reduce the total amount of text. LLM will use this prompt to summarize the summaries. Use template
            variables {core_prompt} to include the core prompt, and {context} wherever the summaries to summarize will be
            inserted.
        combine_prompt (Union[None, Unset, str]): In a map-reduce summarization strategy, the last step is for the LLM
            to combine the summaries. LLM will use this prompt to combine the summaries. Use template variables
            {core_prompt} to include the core prompt, and {context} wherever the list of summaries to combine will be
            inserted.
        max_concurrency (Union[Unset, int]): Maximum number of parallel calls to the LLM the summarizer is allowed to
            make. Default: 3.
        iteration_limit (Union[Unset, int]): In a map-reduce summarization strategy, this is the maximum number of times
            the LLM will "summarize the summaries". Default: 3.
        collapse_token_max (Union[Unset, int]): In a map-reduce summarization strategy, this is the maximum number of
            tokens to include in the combined summaries that the LLM will summarize. Default: 6000.
    """

    core_prompt: Union[None, Unset, str] = UNSET
    collapse_prompt: Union[None, Unset, str] = UNSET
    combine_prompt: Union[None, Unset, str] = UNSET
    max_concurrency: Union[Unset, int] = 3
    iteration_limit: Union[Unset, int] = 3
    collapse_token_max: Union[Unset, int] = 6000
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        core_prompt: Union[None, Unset, str]
        if isinstance(self.core_prompt, Unset):
            core_prompt = UNSET
        else:
            core_prompt = self.core_prompt

        collapse_prompt: Union[None, Unset, str]
        if isinstance(self.collapse_prompt, Unset):
            collapse_prompt = UNSET
        else:
            collapse_prompt = self.collapse_prompt

        combine_prompt: Union[None, Unset, str]
        if isinstance(self.combine_prompt, Unset):
            combine_prompt = UNSET
        else:
            combine_prompt = self.combine_prompt

        max_concurrency = self.max_concurrency

        iteration_limit = self.iteration_limit

        collapse_token_max = self.collapse_token_max

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if core_prompt is not UNSET:
            field_dict["core_prompt"] = core_prompt
        if collapse_prompt is not UNSET:
            field_dict["collapse_prompt"] = collapse_prompt
        if combine_prompt is not UNSET:
            field_dict["combine_prompt"] = combine_prompt
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if iteration_limit is not UNSET:
            field_dict["iteration_limit"] = iteration_limit
        if collapse_token_max is not UNSET:
            field_dict["collapse_token_max"] = collapse_token_max

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_core_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        core_prompt = _parse_core_prompt(d.pop("core_prompt", UNSET))

        def _parse_collapse_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        collapse_prompt = _parse_collapse_prompt(d.pop("collapse_prompt", UNSET))

        def _parse_combine_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        combine_prompt = _parse_combine_prompt(d.pop("combine_prompt", UNSET))

        max_concurrency = d.pop("max_concurrency", UNSET)

        iteration_limit = d.pop("iteration_limit", UNSET)

        collapse_token_max = d.pop("collapse_token_max", UNSET)

        summarize_map_reduce = cls(
            core_prompt=core_prompt,
            collapse_prompt=collapse_prompt,
            combine_prompt=combine_prompt,
            max_concurrency=max_concurrency,
            iteration_limit=iteration_limit,
            collapse_token_max=collapse_token_max,
        )

        summarize_map_reduce.additional_properties = d
        return summarize_map_reduce

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
