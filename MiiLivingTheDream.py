class Philippines():
    def capital(self):
        print("BRO THEY ARE CORRUPT")
    def languange(self):
        print("Kamusta, panget mo daw sabi ni hangin")
    def type(self):
        print("Philippines is a corrupt country")

class USA():
    def capital(self):
        print("Trump lowkey be drinking diet coke while his country goes to inflation")
    def languange(self):
        print("English, they try to be special by saying they r 1% mexican")
    def type(self):
        print("Goofy ahh government")

obj_Phil = Philippines()
obj_usa = USA()

for country in(obj_Phil,obj_usa):
    country.capital()
    country.languange()
    country.type()