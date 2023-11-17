from app.utils.validator import Validator


class TypeSpecifier:
    @staticmethod
    def define_input_type(line: str) -> str:
        if Validator.is_input_string_date(line):
            return "date"
        elif Validator.is_input_string_phone_number(line):
            return "phone_number"
        elif Validator.is_input_string_email(line):
            return "email"
        else:
            return "text"

    @staticmethod
    def is_input_type_correct(line: str) -> bool:
        if line in ["date", "phone_number", "email", "text"]:
            return True
        return False
