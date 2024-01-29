from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document_contents_metadata_type_0 import DocumentContentsMetadataType0


T = TypeVar("T", bound="DocumentContents")


@_attrs_define
class DocumentContents:
    """Class for storing a piece of text and associated metadata.

    Attributes:
        page_content (str): Content to summarize
        metadata (Union['DocumentContentsMetadataType0', None]): Arbitrary metadata about the page content (e.g.,
            source, relationships to other documents, etc.).
    """

    page_content: str
    metadata: Union["DocumentContentsMetadataType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.document_contents_metadata_type_0 import DocumentContentsMetadataType0

        page_content = self.page_content

        metadata: Union[Dict[str, Any], None]
        if isinstance(self.metadata, DocumentContentsMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_content": page_content,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_contents_metadata_type_0 import DocumentContentsMetadataType0

        d = src_dict.copy()
        page_content = d.pop("page_content")

        def _parse_metadata(data: object) -> Union["DocumentContentsMetadataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DocumentContentsMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DocumentContentsMetadataType0", None], data)

        metadata = _parse_metadata(d.pop("metadata"))

        document_contents = cls(
            page_content=page_content,
            metadata=metadata,
        )

        document_contents.additional_properties = d
        return document_contents

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
