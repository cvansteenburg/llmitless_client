from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreprocessorConfig")


@_attrs_define
class PreprocessorConfig:
    """
    Attributes:
        max_tokens_per_doc (Union[Unset, int]): The maximum number of tokens to include in each doc that the LLM will
            summarize. Change this to according the context window of the LLM and the length of the prompt. Default: 3000.
        metadata_to_include (Union[List[str], None, Unset]): In a map-reduce summarization strategy, docs are combined
            and presented together to the llm. The metadata keys are included in the combined documents to give the LLM more
            context.
    """

    max_tokens_per_doc: Union[Unset, int] = 3000
    metadata_to_include: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_tokens_per_doc = self.max_tokens_per_doc

        metadata_to_include: Union[List[str], None, Unset]
        if isinstance(self.metadata_to_include, Unset):
            metadata_to_include = UNSET
        elif isinstance(self.metadata_to_include, list):
            metadata_to_include = self.metadata_to_include

        else:
            metadata_to_include = self.metadata_to_include

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_tokens_per_doc is not UNSET:
            field_dict["max_tokens_per_doc"] = max_tokens_per_doc
        if metadata_to_include is not UNSET:
            field_dict["metadata_to_include"] = metadata_to_include

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_tokens_per_doc = d.pop("max_tokens_per_doc", UNSET)

        def _parse_metadata_to_include(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_to_include_type_0 = cast(List[str], data)

                return metadata_to_include_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        metadata_to_include = _parse_metadata_to_include(d.pop("metadata_to_include", UNSET))

        preprocessor_config = cls(
            max_tokens_per_doc=max_tokens_per_doc,
            metadata_to_include=metadata_to_include,
        )

        preprocessor_config.additional_properties = d
        return preprocessor_config

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
