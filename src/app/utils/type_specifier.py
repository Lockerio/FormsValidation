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
