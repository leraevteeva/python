class StringUtils:
    """
    Класс со вспомогательными функциями для обработки строк.
    """

    def capitalize(self, string: str) -> str:
        """
        Делает первую букву заглавной.
        Примеры:
        "skypro" -> "Skypro"
        "" -> ""
        """
        if string is None:
            raise TypeError("string cannot be None")

        if not string:
            return string

        return string[0].upper() + string[1:]

    def trim(self, string: str) -> str:
        """
        Удаляет пробелы в начале и в конце строки.
        Примеры:
        "  skypro  " -> "skypro"
        "" -> ""
        """
        if string is None:
            raise TypeError("string cannot be None")
        return string.strip()

    def to_list(self, string: str, delimiter=",") -> list:
        """
        Превращает строку в список по разделителю.
        Примеры:
        "a,b,c" -> ["a", "b", "c"]
        "" -> []
        """
        if string is None:
            raise TypeError("string cannot be None")

        if string == "":
            return []

        return string.split(delimiter)

    def contains(self, string: str, substr: str) -> bool:
        """
        Проверяет, содержит ли строка подстроку.
        Примеры:
        "skypro", "pro" -> True
        "skypro", "xyz" -> False
        """
        if string is None or substr is None:
            raise TypeError("values cannot be None")

        return substr in string
