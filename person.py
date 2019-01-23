
#
#
#
class Person:
    count = 0
    people = []
    def __init__(self, name):
        self.name = name
        Person.count += 1
        Person.people.append(name)
        self.pos = Pos(0,0,0)
        self.count=0
        self.speed = 0
        print(name)

    def walk(self, _speed, _time):
        self.speed = _speed
        self.pos.x += _speed * _time
        self.pos.y += _speed * _time

    def run(self, _speed, _time):
        self.speed = _speed
        self.pos.x += _speed * _time
        self.pos.y += _speed * _time

    def where(self):
        print("({}\'s location (x,y,z) is :({},{},{})".format(self.name, self.pos.x, self.pos.y,self.pos.z))


class Pos:
    count = 0
#    def __init__(self):
#        self._x = 0
#        self._y = 0
#        self._z = 0
#        Pos.count += 1
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z
        Pos.count += 1

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z
    @x.setter
    def x(self,val):
        self._x = val
    @y.setter
    def y(self,val):
        self._y = val
    @z.setter
    def z(self,val):
        self._z = val
    @x.deleter
    def x(self):
        del self._x
    @y.deleter
    def y(self):
        del self._y
    @z.deleter
    def z(self):
        del self._z
