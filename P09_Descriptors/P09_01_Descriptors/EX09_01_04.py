class MyDescriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called with instance={instance}, owner={owner}")
        if instance is None:
            return self
        return instance.__dict__.get('value', 'default')

    def __set__(self, instance, value):
        print(f"__set__ called with instance={instance}, value={value}")
        instance.__dict__['value'] = value

    def __delete__(self, instance):
        print(f"__delete__ called with instance={instance}")
        del instance.__dict__['value']

class MyClass:
    attribute = MyDescriptor()

# Создание экземпляра класса
obj = MyClass()

# Установка значения атрибута через дескриптор
obj.attribute = 42
# __set__ called with instance=<__main__.MyClass object at 0x...>, value=42

# Чтение значения атрибута через дескриптор
print(obj.attribute)
# __get__ called with instance=<__main__.MyClass object at 0x...>, owner=<class '__main__.MyClass'>
# 42

# Чтение атрибута через сам класс
print(MyClass.attribute)
# __get__ called with instance=None, owner=<class '__main__.MyClass'>
# <__main__.MyDescriptor object at 0x...>

