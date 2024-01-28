from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileFilter")


@_attrs_define
class FileFilter:
    """
    Attributes:
        collection_digits (str): Usually a 3 digit number expressed as a string eg. "010"
        title_digits (List[str]): A list of usually 3 digit numbers expressed as a strings eg. ["001", "002", "009"]
    """

    collection_digits: str
    title_digits: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_digits = self.collection_digits

        title_digits = self.title_digits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_digits": collection_digits,
                "title_digits": title_digits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_digits = d.pop("collection_digits")

        title_digits = cast(List[str], d.pop("title_digits"))

        file_filter = cls(
            collection_digits=collection_digits,
            title_digits=title_digits,
        )

        file_filter.additional_properties = d
        return file_filter

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
