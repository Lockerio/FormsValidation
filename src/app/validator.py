import calendar
from datetime import datetime
import re


class Validator:
    @staticmethod
    def is_input_string_date(input_string: str) -> bool:
        date_pattern_1 = "%d.%m.%Y"
        date_pattern_2 = "%Y-%m-%d"

        try:
            dt = datetime.strptime(input_string, date_pattern_1)
        except ValueError:
            try:
                dt = datetime.strptime(input_string, date_pattern_2)
            except ValueError:
                return False

        _, last_day = calendar.monthrange(dt.year, dt.month)
        if dt.day <= last_day:
            return False
        return True

    @staticmethod
    def is_input_string_phone_number(input_string: str) -> bool:
        phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
        match = re.match(phone_pattern, input_string)
        return bool(match)

    @staticmethod
    def is_input_string_email(input_string: str) -> bool:
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        match = re.match(email_pattern, input_string)
        return bool(match)
