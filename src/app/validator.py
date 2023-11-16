from datetime import datetime


class Validator:
    @staticmethod
    def is_input_string_date(input_string: str) -> bool:
        date_pattern_1 = "%d.%m.%Y"
        date_pattern_2 = "%Y-%m-%d"

        try:
            datetime.strptime(input_string, date_pattern_1)
            return True
        except ValueError:
            pass

        try:
            datetime.strptime(input_string, date_pattern_2)
            return True
        except ValueError:
            pass

        return False

    @staticmethod
    def is_input_string_phone_number(input_string: str) -> bool:
        pass

    @staticmethod
    def is_input_string_email(input_string: str) -> bool:
        pass
