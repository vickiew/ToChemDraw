class Bond(object):

    def __init__(self,id,begin,end,order,zorder,stereo=0):
        """Return a Bond object with the given attributes."""
        self.id = id
        self.begin = begin
        self.end = end
        self.order = order
        self.zorder = zorder
        self.stereo = stereo

    def __str__(self):
        """Returns the cdxml string representation of this Node."""
        returnString = "<b\n"
        returnString += "id=\"" + str(id) + "\"\n"
        returnString += "B=\"" + str(self.begin) + "\"\n"
        returnString += "E=\"" + str(self.end) + "\"\n"
        returnString += "Order=\"" + str(self.order) + "\"\n"
        returnString += "Z=\"" + str(self.zorder) + "\"\n"
        returnString += "Display=\"" + str(self.stereo) + "\"\n"
        returnString += "/>"
        return returnString

