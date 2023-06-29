class Man:
    def __init__(self,name):
        self.name = name
        print("Init")
    def hello(self):
        print("Hello " + self.name+" !")
    def goodbye(self):
        print("Goodbye "+self.name+" !") 

m = Man("李彬")
m.hello()
m.goodbye()