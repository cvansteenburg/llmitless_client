from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_filter import FileFilter
    from ..models.preprocessor import Preprocessor
    from ..models.summarize_map_reduce import SummarizeMapReduce
    from ..models.user_llm_config import UserLLMConfig


T = TypeVar("T", bound="BodySummarizeFromDiskSummarizeFromDiskPost")


@_attrs_define
class BodySummarizeFromDiskSummarizeFromDiskPost:
    """
    Attributes:
        file_filter (FileFilter):
        preprocessor (Preprocessor):
        summarize_map_reduce (SummarizeMapReduce):
        llm_config (UserLLMConfig):
    """

    file_filter: "FileFilter"
    preprocessor: "Preprocessor"
    summarize_map_reduce: "SummarizeMapReduce"
    llm_config: "UserLLMConfig"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_filter = self.file_filter.to_dict()

        preprocessor = self.preprocessor.to_dict()

        summarize_map_reduce = self.summarize_map_reduce.to_dict()

        llm_config = self.llm_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_filter": file_filter,
                "preprocessor": preprocessor,
                "summarize_map_reduce": summarize_map_reduce,
                "llm_config": llm_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_filter import FileFilter
        from ..models.preprocessor import Preprocessor
        from ..models.summarize_map_reduce import SummarizeMapReduce
        from ..models.user_llm_config import UserLLMConfig

        d = src_dict.copy()
        file_filter = FileFilter.from_dict(d.pop("file_filter"))

        preprocessor = Preprocessor.from_dict(d.pop("preprocessor"))

        summarize_map_reduce = SummarizeMapReduce.from_dict(d.pop("summarize_map_reduce"))

        llm_config = UserLLMConfig.from_dict(d.pop("llm_config"))

        body_summarize_from_disk_summarize_from_disk_post = cls(
            file_filter=file_filter,
            preprocessor=preprocessor,
            summarize_map_reduce=summarize_map_reduce,
            llm_config=llm_config,
        )

        body_summarize_from_disk_summarize_from_disk_post.additional_properties = d
        return body_summarize_from_disk_summarize_from_disk_post

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
