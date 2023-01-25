class INDIA:
    def capital(self):
        print("delhi is the capital of india")
    def language(self):
        print("hindi is the more prefered language in india")
    def type(self):
        print("india is developing country")


class USA:
    def capital(self):
        print("washington dc is the capital city of USA")
    def language(self):
        print("english is the primary language is USA")
    def type(self):
        print("USA is well developed country")

india=INDIA()
usa=USA()
for country in (india,usa):
    country.capital()
    country.language()
    country.type()



    #polymorphism with inheritance

class ADD:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add (self):
        c=self.a+self.b
        return c

class SUB(ADD):
    def __init__(self,a,b):
        ADD.__init__(self,a,b)

    def sub(self):
        c=self.a-self.b
        return c



y=SUB(45,56)
x=ADD(23,543)
print(x.add())
print(y.sub())
print(y.add())




