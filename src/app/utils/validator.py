import calendar
from datetime import datetime
import re


class Validator:
    @staticmethod
    def is_input_string_date(input_string: str) -> bool:
        date_patterns = ["%d.%m.%Y", "%Y-%m-%d"]

        for date_pattern in date_patterns:
            try:
                dt = datetime.strptime(input_string, date_pattern)
                _, last_day = calendar.monthrange(dt.year, dt.month)
                if dt.day <= last_day:
                    return True
            except ValueError:
                pass
        return False

    @staticmethod
    def is_input_string_phone_number(input_string: str) -> bool:
        print(input_string)
        phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
        match = re.match(phone_pattern, input_string)
        print(bool(match))
        return bool(match)

    @staticmethod
    def is_input_string_email(input_string: str) -> bool:
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        match = re.match(email_pattern, input_string)
        return bool(match)
