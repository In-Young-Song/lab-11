from .operator import Operator
from .operator import OperatorType

class Initial(Operator):
    def operate(self, text: str, params: dict = None) -> str:
        if not text:
            return ""
        return text[0]

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        # No parameters required — always valid
        pass
