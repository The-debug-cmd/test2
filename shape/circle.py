class Circle:
    def __init__(self, pos, rad):
        self.center = pos
        self.radius = rad
    def __contains__(self, other):
        a=((list(self.center)[0]-list(other)[0])**2+(list(self.center)[1]-list(other)[1])**2)**0.5
        if a<self.radius:
            return True
        else:
            return False
