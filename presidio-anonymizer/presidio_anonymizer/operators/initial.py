from .operator import Operator
from .operator import OperatorType

class Initial(Operator):
    def operate(self, text: str, params: dict = None) -> str:
        if not text:
            return ""

        # Split full name into words (first, last, etc.)
        parts = text.split()

        # Create initials and format like: "J. S."
        initials = [p[0].upper() + "." for p in parts]
        return " ".join(initials)

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        pass

