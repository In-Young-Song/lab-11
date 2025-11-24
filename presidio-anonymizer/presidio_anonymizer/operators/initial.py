from .operator import Operator
from .operator import OperatorType

class Initial(Operator):
    def operate(self, text: str, params: dict = None) -> str:
        if not text:
            return ""

        # Remove leading/trailing/multiple spaces between words
        # Split manually and discard empty segments
        parts = [p for p in text.split(" ") if p.strip()]

        # Create initials: "E. M. U."
        initials = [p[0].upper() + "." for p in parts]
        return " ".join(initials)

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        pass
