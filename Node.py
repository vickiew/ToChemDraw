class Node(object):
    """A simplified ChemDraw Node, which currently cannot contain other Fragments as subobjects.

    Attributes:
        id: A string, the unique identifier of an object, used when other objects refer to it.
        x: An double, the x-position of this node.
        y: An double, the y-position of this node.
        nodeType: An int, the type of node, which we will restrict to two options:
            1 = Element (A chemical element or one heavy element and attached hydrogens); in this
                case the text should be associated as an element property when exporting to cdmxl.
            0 = Unknown (All others; we will use this in for formulas, nicknames, and fragments);
                in this case the text should be associated as a Text object when exporting cdxml.
            Note that we will not support the ChemDraw's native Fragment, Formula, or Nickname
            types at the moment.
        implicit: A boolean that if true, indicates this node to have no label, i.e. it is a
            carbon with implicit hydrogens.
        text: A Text object that stores the label of this Node.
    """

    def __init__(self, id, x, y, nodeType, implicit, text):
        """Return a Node object with the given attributes."""
        self.id = id
        self.x = x
        self.y = y
        self.nodeType = nodeType
        self.implicit = implicit
        self.text = text

    def __str__(self):
        """Returns the cdxml string representation of this Node"""
        returnString = "<n\n"
        returnString += "id=\"" + self.id + "\"\n"
        returnString += "p=\"" + self.x + " " + self.y + "\"\n"
        if nodeType:
            returnString += "NodeType=\"1\"\n"
            returnString += "E"
""" Need to put the element number of the heavy atom in the label, maybe using somethign like:
re.sub(r"H\:.+?\, ", "", str(pt.formula("H2HfH3").hill.atoms)).split("{",1)[-1].split(":",1)[0]
"""
        returnString += "\/n>"
        return returnString
