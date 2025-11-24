from .operator import Operator
from .operator import OperatorType

class Initial(Operator):
    def operate(self, text: str, params: dict = None) -> str:
        if not text:
            return ""

        # Prefix: keep ONLY non-alphanumeric characters, NOT whitespace
        prefix = ""
        i = 0
        while i < len(text) and not text[i].isalnum():
            # only preserve non-alphanumeric non-whitespace
            if not text[i].isspace():
                prefix += text[i]
            i += 1

        # Remainder after prefix & whitespace
        remainder = text[i:].strip()

        # Split into meaningful chunks (names)
        parts = [p for p in remainder.split(" ") if p.strip()]

        # Initials for each word
        all_initials = [p[0].upper() + "." for p in parts]

        # If there was a symbol prefix, use only the first initial
        if prefix:
            return prefix + all_initials[0]

        # Otherwise use full initials
        return " ".join(all_initials)

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        pass
        