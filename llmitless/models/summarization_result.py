from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.result_status import ResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summarization_result_debug_type_0 import SummarizationResultDebugType0


T = TypeVar("T", bound="SummarizationResult")


@_attrs_define
class SummarizationResult:
    r"""
    Example:
        {'debug': {'key': 'value'}, 'result_status': 'SUCCESS', 'summary': 'Successful summarization output',
            'usage_report': 'Total Tokens: 3700\n\nPrompt Tokens: 3200\n\nCompletion Tokens: 500.\n\nTotal Cost (USD):
            $0.0351'}

    Attributes:
        result_status (ResultStatus):
        summary (Union[None, Unset, str]): The summarized text.
        usage_report (Union[None, Unset, str]): LLM cost and usage report, if available. This is enabled server-side,
            and if enabled, may vary by model. Example: 'Total Tokens: 3700

            Prompt Tokens: 3200

            Completion Tokens: 500.

            Total Cost (USD): $0.0351'
        debug (Union['SummarizationResultDebugType0', None, Unset]): Extra debug information, if available. Used in
            self-hosted dev environments.
    """

    result_status: ResultStatus
    summary: Union[None, Unset, str] = UNSET
    usage_report: Union[None, Unset, str] = UNSET
    debug: Union["SummarizationResultDebugType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.summarization_result_debug_type_0 import SummarizationResultDebugType0

        result_status = self.result_status.value

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        usage_report: Union[None, Unset, str]
        if isinstance(self.usage_report, Unset):
            usage_report = UNSET
        else:
            usage_report = self.usage_report

        debug: Union[Dict[str, Any], None, Unset]
        if isinstance(self.debug, Unset):
            debug = UNSET
        elif isinstance(self.debug, SummarizationResultDebugType0):
            debug = self.debug.to_dict()
        else:
            debug = self.debug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result_status": result_status,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if usage_report is not UNSET:
            field_dict["usage_report"] = usage_report
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summarization_result_debug_type_0 import SummarizationResultDebugType0

        d = src_dict.copy()
        result_status = ResultStatus(d.pop("result_status"))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_usage_report(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        usage_report = _parse_usage_report(d.pop("usage_report", UNSET))

        def _parse_debug(data: object) -> Union["SummarizationResultDebugType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_type_0 = SummarizationResultDebugType0.from_dict(data)

                return debug_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SummarizationResultDebugType0", None, Unset], data)

        debug = _parse_debug(d.pop("debug", UNSET))

        summarization_result = cls(
            result_status=result_status,
            summary=summary,
            usage_report=usage_report,
            debug=debug,
        )

        summarization_result.additional_properties = d
        return summarization_result

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
