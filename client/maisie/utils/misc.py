import ago
import dateutil.parser
from datetime import datetime, timezone
from colorama import Fore


class Transform:
    def api_response_to_terminaltables(self, obj: list, include: list = None) -> list:
        """Transforms a list of dictionaries into a list of lists.

        :param include: keys returned in the final list. 
        :returns: a TerminalTables-compatible data structure. 
        """
        result = []
        for index, entry in enumerate(obj):
            filtered_dict = {key: entry[key] for key in entry if key in include}
            if index == 0:
                result.append(filtered_dict.keys())
            values = filtered_dict.values()
            result.append(self.determine_values(values, filtered_dict.keys()))

        return result

    def colorise(self, obj: str, color: str = Fore.YELLOW):
        reset = Fore.RESET
        return color + obj + reset

    def determine_values(self, values: list, keys: list) -> list:
        obj = zip(keys, values)
        result = []
        for key, value in obj:
            result.append(self.determine_format(value, key))

        return result

    def determine_format(self, value, key=None):
        """Determines what can be done to each given value."""
        if isinstance(value, dict):
            if key and key == "user":
                return self.dict_to_username(value)
            else:
                return self.dict_to_multiline_string(value)
        if isinstance(value, str):
            if self.is_date(value):
                return self.timestamp_to_human_readable(value)
        return value

    def is_date(self, value: str) -> bool:
        """Checks whether the given string can be parsed as a datetime."""
        try:
            dateutil.parser.parse(value, fuzzy=False)
            return True

        except ValueError:
            return False

    def timestamp_to_human_readable(self, obj: str) -> str:
        """Transforms a timestamp into a human-readable delta of the time."""
        delta = datetime.now(timezone.utc) - dateutil.parser.parse(obj)

        return ago.human(delta, precision=2)

    def dict_to_multiline_string(self, obj: dict) -> str:
        """Transforms a dictionary into a string where each pair (key: value) 
        is followed by a newline.

        :param obj: a dictionary
        :returns: a dictionary formatted into manylines
        """
        result = []

        for key, value in obj.items():
            result.append(f"{key}: {value}")

        return "\n".join(result)

    def dict_to_username(self, obj: dict) -> str:
        username = obj["login"]
        if obj["full_name"]:
            username += f" ({obj['full_name']})"

        return username

    def apply_beautiful_colors(self, obj: str, schema: list = None) -> str:
        if schema != None:
            new_rows = []
            if obj:
                new_rows.append(obj[0])

            for row in obj[1:]:
                new_column = []
                for index, column in enumerate(row):
                    color = Fore.RESET
                    if schema[index] != None:
                        color = schema[index]

                    new_column.append(color + str(column) + Fore.RESET)
                new_rows.append(new_column)

            obj = new_rows
        return obj
