class Fragment(object):

    def __init__(self,id,objectsList):
        self.objectsList = objectsList
        self.id = id

    def __add__(self,obj):
        self.objectsList.append(obj)

    def __str__(self):
        """Returns the cdxml string representation of this Node."""
        returnString = "<fragment\n"
        returnString += "id=\"" + str(id) + "\"\n"
        for obj in self.objectsList:
            returnString += str(obj)
        returnString += "</fragment>"

        return returnString
