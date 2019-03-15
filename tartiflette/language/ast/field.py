from typing import List, Optional

from tartiflette.language.ast.base import SelectionNode


class FieldNode(SelectionNode):
    """
    TODO:
    """

    __slots__ = (
        "alias",
        "name",
        "arguments",
        "directives",
        "selection_set",
        "location",
    )

    def __init__(
        self,
        name: "NameNode",
        alias: Optional["NameNode"] = None,
        arguments: Optional[List["ArgumentNode"]] = None,
        directives: Optional[List["DirectiveNode"]] = None,
        selection_set: Optional["SelectionSetNode"] = None,
        location: Optional["Location"] = None,
    ) -> None:
        """
        TODO:
        :param name: TODO:
        :param alias: TODO:
        :param arguments: TODO:
        :param directives: TODO:
        :param selection_set: TODO:
        :param location: TODO:
        :type name: TODO:
        :type alias: TODO:
        :type arguments: TODO:
        :type directives: TODO:
        :type selection_set: TODO:
        :type location: TODO:
        """
        self.name = name
        self.alias = alias
        self.arguments = arguments
        self.directives = directives
        self.selection_set = selection_set
        self.location = location

    def __eq__(self, other):
        """
        TODO:
        :param other: TODO:
        :type other: TODO:
        :return: TODO:
        :rtype: TODO:
        """
        return self is other or (
            isinstance(other, FieldNode)
            and (
                self.alias == other.alias
                and self.name == other.name
                and self.arguments == other.arguments
                and self.directives == other.directives
                and self.selection_set == other.selection_set
                and self.location == other.location
            )
        )

    def __repr__(self) -> str:
        """
        TODO:
        :return: TODO:
        :rtype: TODO:
        """
        return (
            "FieldNode(alias=%r, name=%r, arguments=%r, directives=%r, selection_set=%r, location=%r)"
            % (
                self.alias,
                self.name,
                self.arguments,
                self.directives,
                self.selection_set,
                self.location,
            )
        )
