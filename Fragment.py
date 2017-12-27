class Fragment(object):

    def __init__(self,id,objectslist):
        self.objectslist = objectslist
        self.id = id

    def __add__(self,obj):
        self.idlist.append(obj)

    def __str__(self):
        """Returns the cdxml string representation of this Node."""
        returnString = "<fragment\n"
        returnString += "id=\"" + str(id) + "\"\n"
        for obj in self.objectlist:
            returnString += obj
        returnString += "</fragment>"

        return returnString
