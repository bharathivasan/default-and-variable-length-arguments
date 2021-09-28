   # overriding in class
# this is parent class
class parent:
    def __init__(self):
        print("parent contructor")

    def work(self):
        print("my parent is working for home town")

    def display(self):
        print("somthing picture dislaying")        

# this is child class
class child(parent):
    def __init__(self):
        super().__init__()    # ----> this key word is access for super class
        print("child contructor")

    def work(self):
        super().work()
        print("i am is business magnet")
     
    def test(self):
        print("test your knowledge") 
# create a object        
ch = child()

ch.work()
ch.test()
ch.display()
