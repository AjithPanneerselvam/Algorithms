"""
String Combination
"""

class Combination(object):

    def __init__(self,String):
        self.String = String
        self.output = str()
        self.set = set()
        temp = list(self.String)

        for i in temp:
            self.set.add(i)

    def combination(self):
        pass

obj = Combination("aabc")
