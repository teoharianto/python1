class MyClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def penjumlahan(self):
        return self.x + self.y

    def pengurangan(self):
        return self.x - self.y

class MyClassChild(MyClass):
   super
