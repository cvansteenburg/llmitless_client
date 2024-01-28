from enum import Enum


class InputDocFormat(str, Enum):
    HTML = "html"
    MARKDOWN = "markdown"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
