class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value
