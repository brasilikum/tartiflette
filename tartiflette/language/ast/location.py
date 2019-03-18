from typing import Any, Optional


class Location:
    """
    TODO:
    """

    __slots__ = ("line", "column", "line_end", "column_end")

    def __init__(
        self,
        line: int,
        column: int,
        line_end: Optional[int] = None,
        column_end: Optional[int] = None,
    ) -> None:
        """
        TODO:
        :param line: TODO:
        :param column: TODO:
        :param line_end: TODO:
        :param column_end: TODO:
        :type line: int
        :type column: int
        :type line_end: Optional[int]
        :type column_end: Optional[int]
        """
        self.line = line
        self.column = column
        self.line_end = line_end
        self.column_end = column_end

    def __eq__(self, other: Any) -> bool:
        """
        TODO:
        :param other: TODO:
        :type other: Any
        :return: TODO:
        :rtype: bool
        """
        return self is other or (
            isinstance(other, Location)
            and (
                self.line == other.line
                and self.column == other.column
                and self.line_end == other.line_end
                and self.column_end == other.column_end
            )
        )

    def __repr__(self) -> str:
        """
        TODO:
        :return: TODO:
        :rtype: str
        """
        return "Location(line=%r, column=%r, line_end=%r, column_end=%r)" % (
            self.line,
            self.column,
            self.line_end,
            self.column_end,
        )