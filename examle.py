class First:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def disp(self):
        return self.a, self.b

    def new(self):
        return self.a.upper()

    def __repr__(self):
        return f'names: {self.a} {self.b}'


f = First('serg', 'naumov')
print(f)


class Second(First):
    def __init__(self, a, b, c=None):
        super().__init__(a, b)
        self.c = c




s = Second('vasili', 'slinin')
print(s)
s.new()
print(s.a)
