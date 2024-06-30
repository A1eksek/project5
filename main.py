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


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

id1 = BankAccount(10000)

print(id1.get_balance())
print(id1.__dict__)
print(id1._BankAccount__balance)