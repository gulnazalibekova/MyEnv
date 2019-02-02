class Pet():
   def __init__(self, name, types):
      self.name = name
      self.types = types

   def getInfo(self):
       print("This is a " + self.types + ".")
        print(self.name + " is the" + self.types + "'s name.")


