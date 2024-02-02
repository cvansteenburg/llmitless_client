from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document_contents import DocumentContents
    from ..models.llm_configs import LLMConfigs
    from ..models.map_reduce_configs import MapReduceConfigs
    from ..models.preprocessor_config import PreprocessorConfig


T = TypeVar("T", bound="BodySummarize")


@_attrs_define
class BodySummarize:
    """
    Attributes:
        docs_to_summarize (List['DocumentContents']):
        preprocessor (PreprocessorConfig):
        summarize_map_reduce (MapReduceConfigs):
        llm_config (LLMConfigs):
    """

    docs_to_summarize: List["DocumentContents"]
    preprocessor: "PreprocessorConfig"
    summarize_map_reduce: "MapReduceConfigs"
    llm_config: "LLMConfigs"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        docs_to_summarize = []
        for docs_to_summarize_item_data in self.docs_to_summarize:
            docs_to_summarize_item = docs_to_summarize_item_data.to_dict()
            docs_to_summarize.append(docs_to_summarize_item)

        preprocessor = self.preprocessor.to_dict()

        summarize_map_reduce = self.summarize_map_reduce.to_dict()

        llm_config = self.llm_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "docs_to_summarize": docs_to_summarize,
                "preprocessor": preprocessor,
                "summarize_map_reduce": summarize_map_reduce,
                "llm_config": llm_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_contents import DocumentContents
        from ..models.llm_configs import LLMConfigs
        from ..models.map_reduce_configs import MapReduceConfigs
        from ..models.preprocessor_config import PreprocessorConfig

        d = src_dict.copy()
        docs_to_summarize = []
        _docs_to_summarize = d.pop("docs_to_summarize")
        for docs_to_summarize_item_data in _docs_to_summarize:
            docs_to_summarize_item = DocumentContents.from_dict(docs_to_summarize_item_data)

            docs_to_summarize.append(docs_to_summarize_item)

        preprocessor = PreprocessorConfig.from_dict(d.pop("preprocessor"))

        summarize_map_reduce = MapReduceConfigs.from_dict(d.pop("summarize_map_reduce"))

        llm_config = LLMConfigs.from_dict(d.pop("llm_config"))

        body_summarize = cls(
            docs_to_summarize=docs_to_summarize,
            preprocessor=preprocessor,
            summarize_map_reduce=summarize_map_reduce,
            llm_config=llm_config,
        )

        body_summarize.additional_properties = d
        return body_summarize

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
