from enum import Enum


class ResultStatus(str, Enum):
    FORBIDDEN_CONTENT = "FORBIDDEN_CONTENT"
    MODEL_ERROR = "MODEL_ERROR"
    SUCCESS = "SUCCESS"
    UNCLEAR_INSTRUCTIONS = "UNCLEAR_INSTRUCTIONS"

    def __str__(self) -> str:
        return str(self.value)
