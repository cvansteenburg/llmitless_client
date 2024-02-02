from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_filter import FileFilter
    from ..models.llm_configs import LLMConfigs
    from ..models.map_reduce_configs import MapReduceConfigs
    from ..models.preprocessor_config import PreprocessorConfig


T = TypeVar("T", bound="BodySummarizeFromDisk")


@_attrs_define
class BodySummarizeFromDisk:
    """
    Attributes:
        file_filter (FileFilter):
        preprocessor_config (PreprocessorConfig):
        summarize_map_reduce (MapReduceConfigs):
        llm_config (LLMConfigs):
    """

    file_filter: "FileFilter"
    preprocessor_config: "PreprocessorConfig"
    summarize_map_reduce: "MapReduceConfigs"
    llm_config: "LLMConfigs"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_filter = self.file_filter.to_dict()

        preprocessor_config = self.preprocessor_config.to_dict()

        summarize_map_reduce = self.summarize_map_reduce.to_dict()

        llm_config = self.llm_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_filter": file_filter,
                "preprocessor_config": preprocessor_config,
                "summarize_map_reduce": summarize_map_reduce,
                "llm_config": llm_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_filter import FileFilter
        from ..models.llm_configs import LLMConfigs
        from ..models.map_reduce_configs import MapReduceConfigs
        from ..models.preprocessor_config import PreprocessorConfig

        d = src_dict.copy()
        file_filter = FileFilter.from_dict(d.pop("file_filter"))

        preprocessor_config = PreprocessorConfig.from_dict(d.pop("preprocessor_config"))

        summarize_map_reduce = MapReduceConfigs.from_dict(d.pop("summarize_map_reduce"))

        llm_config = LLMConfigs.from_dict(d.pop("llm_config"))

        body_summarize_from_disk = cls(
            file_filter=file_filter,
            preprocessor_config=preprocessor_config,
            summarize_map_reduce=summarize_map_reduce,
            llm_config=llm_config,
        )

        body_summarize_from_disk.additional_properties = d
        return body_summarize_from_disk

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
