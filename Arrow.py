class Arrow(object):

    def __init__(self,id, ArrowheadHead="Full", Tail3D, Head3D):
        """Return a Bond object with the given attributes."""
        self.id = id
        self.arrowheadHead = ArrowheadHead
        self.tail3D = Tail3D  # set z coord to 0
        self.head3D = head3D  # set z coord to 0

    def __str__(self):
        """Returns the cdxml string representation of this Node."""
        returnString = "<arrow\n"
        returnString += "id=\"" + str(id) + "\"\n"
        returnString += "ArrowheadHead=\"" + str(self.arrowheadHead) + "\"\n"
        returnString += "Head3D=\"" + str(self.head3D) + "\"\n"
        returnString += "Tail3D=\"" + str(self.tail3D) + "\"\n"
        returnString += "/>"
        return returnString

