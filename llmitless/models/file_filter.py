from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_file_format_names import DatasetFileFormatNames
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileFilter")


@_attrs_define
class FileFilter:
    """
    Attributes:
        collection_digits (str): Usually a 3 digit number expressed as a string eg. "010"
        title_digits (Union[List[str], None, Unset]): A list of usually 3 digit numbers expressed as a strings eg.
            ["001", "002", "009"]
        file_format (Union[Unset, DatasetFileFormatNames]):  Default: DatasetFileFormatNames.HTML_MESSAGE_HTML.
    """

    collection_digits: str
    title_digits: Union[List[str], None, Unset] = UNSET
    file_format: Union[Unset, DatasetFileFormatNames] = DatasetFileFormatNames.HTML_MESSAGE_HTML
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_digits = self.collection_digits

        title_digits: Union[List[str], None, Unset]
        if isinstance(self.title_digits, Unset):
            title_digits = UNSET
        elif isinstance(self.title_digits, list):
            title_digits = self.title_digits

        else:
            title_digits = self.title_digits

        file_format: Union[Unset, str] = UNSET
        if not isinstance(self.file_format, Unset):
            file_format = self.file_format.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_digits": collection_digits,
            }
        )
        if title_digits is not UNSET:
            field_dict["title_digits"] = title_digits
        if file_format is not UNSET:
            field_dict["file_format"] = file_format

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_digits = d.pop("collection_digits")

        def _parse_title_digits(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                title_digits_type_0 = cast(List[str], data)

                return title_digits_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        title_digits = _parse_title_digits(d.pop("title_digits", UNSET))

        _file_format = d.pop("file_format", UNSET)
        file_format: Union[Unset, DatasetFileFormatNames]
        if isinstance(_file_format, Unset):
            file_format = UNSET
        else:
            file_format = DatasetFileFormatNames(_file_format)

        file_filter = cls(
            collection_digits=collection_digits,
            title_digits=title_digits,
            file_format=file_format,
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
