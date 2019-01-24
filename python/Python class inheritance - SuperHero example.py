class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print('{} is about {}'.format(name, self.height))


class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        self.breast = 90

    def about(self, name):  # method overwriting for about()
        print('{} is a hot girl, she is about {}, and her breast is {}'.
              format(name, self.height, self.breast))
        super(Girl, self).about(name)


class SuperHero(Person):   # SuperHero inherits from Person...
    def intro(self):       # but with a new method intro()
        '''Return an introduction.'''
        return 'Hello, I'm SuperHero {} and I'm {}.'.format(self.name, self.age)


if __name__ == '__main__':
    cang = Girl()
    cang.about("CangLaoShi")
