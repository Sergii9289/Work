
class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError(f'Age must be in range 1 - 120')
        self.__age = age

    def describe(self):
        print(f'I am {self._first_name} {self._last_name}, I am {self.__age} years old!')

if __name__ == '__main__':
    ivan = Person('Ivan', 'Ivanenko', 20)
    ivan.set_age(2)
    ivan.describe()