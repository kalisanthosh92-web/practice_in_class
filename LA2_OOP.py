class Phone:
    def __init__(self,brand, model):
        self.Brand = brand
        self.Model = model


    def describePhone(self):
        return '{}-{}.'.format(self.Brand, self.Model)


#class Android(Phone):
 #   def __init__(self, brand, model):
  #      super().__init__(brand, model)


And1 = Android('oppo','Reno 13')
print(Android.describePhone(And1))


Ph1= Phone('samsung,'Galaxy-z)
print(Phone.describePhone(Ph1))
