class Computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    speed=0
    def config(self):
        print("Config is ",self.cpu,self.ram)


com1=Computer("i5",16)
com2=Computer("i3",12)

print(type(com1))

com1.config()
com2.config()