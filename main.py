"public(обычный)"

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_date(self):
#         print(f'{self.name, self.age}')
#
# idl = Person("Vasya", 18)
# idl.print_date()
# print(idl.name, idl.age)

"protected(защищёныые атрибуты)"

# class Person:
#     def __init__(self, name, age):
#         self._name = name #защищенные
#         self._age = age #защищенные
#
#     def print_date(self):
#         print(f'{self._name, self._age}')
#
# idl = Person("Vasya", 18)
# idl.print_date()
# print(idl._name, idl._age)

"Protected method(защищённые методы)"

# class Person:
#     def _vasya_cat_(self): #защищенный метод
#         print("Васин кот царапает диван")
#
#     def print_protected_method(self):
#         self._vasya_cat_()
#
# id1 = Person()
# id1.print_protected_method()
# id1._vasya_cat_()

"Private (приватные) атрибуты"

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
# id1 = BankAccount(10000)
# print(id1.get_balance())
# print(id1.__balance)

"Private (приватные) методы"

# class Person:
#     def __pin(self):
#         print("Пароль от почты")
#
#     def get_pin(self):
#         return self.__pin()
#
# id1 = Person()
# id1.get_pin()
################################################


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
# id1 = BankAccount(10000)
#
# print(id1.get_balance())
# print(id1.__dict__)
# print(id1._BankAccount__balance)

"Наследование protected"

# class Parent:
#     _x = 10
#     def parent_x(self):
#         print(self._x)
#
# class Child(Parent):
#     def child_x(self):
#         print(self._x)
#
# id1 = Child()
# id1.child_x()
# id1.parent_x()

"Наследование private"

# class Parent:
#     __x = 10
#     def parent_x(self):
#         print(self.__x)
#
# class Child(Parent):
#     def child_x(self):
#         print(self.__x)
#
# id2 = Parent()
# id2.parent_x()
#
# id1 = Child()
# id1.parent_x()

# id1.child_x()

"Можно ли вызвать приватные атрибуты созданные в родительском классе, через методы созданные в дочернем классе"

from accessify import private, protected
# class MyClass:
#     a = 2
#     b = 3
#
#     @private
#     def private_sum_ad(self):
#         print(f'{self.a + self.b}')
#
#     def public_sum_ad(self):
#         self.private_sum_ad()
#
#
# id1 = MyClass()
# id1.public_sum_ad()

# class MyClass:
#     @protected
#     def _protected(self):
#         print('это защищённый метод')
#
#     def _public(self):
#         self._protected()
#
# id1 = MyClass()
# id1._public()
# id1._protected()

"Декораторы property (getter, setter, deleter)"
"property - свойство"

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
# person = Person("вася")
# print(person.name)

"s"

class Person:
    def __init__(self, name):
        self.__name = name

    @property #getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


# person = Person("Vasya")
# print(person.name)
# person.name = "Vlad"
# print(person.name)
person = Person("John")
print(person.__dict__)
del person.name
print(person.__dict__)