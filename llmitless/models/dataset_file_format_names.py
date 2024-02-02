from enum import Enum


class DatasetFileFormatNames(str, Enum):
    HTML_MESSAGE_HTML = "html-message.html"
    JSON_BODY_JSON = "json-body.json"
    RAW_SOURCE_TXT = "raw-source.txt"
    TEXT_MESSAGE_TXT = "text-message.txt"

    def __str__(self) -> str:
        return str(self.value)
