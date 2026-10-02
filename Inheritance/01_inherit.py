class GrandFather:
    def __init__(self):
        self.property="house"
class Father(GrandFather):
    def __init__(self):
        self.car="bmw"
        super().__init__()
class child(Father):
    def __init__(self):
        self.bike="ktm"
        super().__init__()
c=child()
print(c.property)
print(c.car)
print(c.bike)
