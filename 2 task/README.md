# Звіт до роботи
# Тема: Основи Python
# Мета роботи: Ознайомитись з основними конструкціями в Python

# Виконання роботи

## Я створив два файли на своєму ноутбуці, main.py та main.ipynb. В файл main.py я помістив код вказаний у завданні

```python
class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self): 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"


print("Let's Start!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")```

### 1 ця програма виводить у консоль цей текст
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001D0646429D0> 
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001D064642ED0>
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 4 names! ??? Why 4?

### 2. На жаль, у мене не було змоги відвідати лекцію, тому в цей файл я ввів свої приклади
```python
from main.py import MyName
names = ("Andriy", "Olena", None)
all_names = {name: MyName(name) for name in names}

# Вивід інформації про створені об'єкти
for name, me in all_names.items():
    print(f"""{">*<"*20}
    This is object: {me} 
    This is object attribute: {me.name} / {me.my_id}
    This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
    This is {type(me.create_email)} call: {me.create_email()}
    This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
    This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
    {"<*>"*20}""")

# Вивід кількості створених імен
print(f"We are done. We created {MyName.total_names} names!")
```

цей код видав мені такий результат
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <main.MyName object at 0x0000020D78F33A90> 
    This is object attribute: Bohdan / 5
    This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
    This is <class 'method'> call: Bohdan@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone! 
    This is class variable <class 'int'>: from class 8 / from object 8
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <main.MyName object at 0x0000020D78F32CD0> 
    This is object attribute: Marta / 6
    This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
    This is <class 'method'> call: Marta@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone! 
    This is class variable <class 'int'>: from class 8 / from object 8
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <main.MyName object at 0x0000020D78929A10> 
    This is object attribute: Anonymous / 8
    This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
    This is <class 'method'> call: Anonymous@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone! 
    This is class variable <class 'int'>: from class 8 / from object 8
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We created 8 names!


### 3 Я зрозумів за що відповідає кожний з рядків представленого коду
### 4 Я замінив рядок коду в файлі main.py, щоб вписати своє ім'я
```python
names = ("Bohdan", "Marta", "Andriy Balii", None)
```
### 
### 5 об'єкт Anonymus з'являється через ось цю строку коду
```python
self.name = name if name is not None else self.anonymous_user().name
```
Для зміни привітання на якесь інше потрібно створити кастомне привітання
```python
custom_greeting = MyName.say_hello("Hello, this is a customized greeting!")
```

для третього завдання потрібно дописати функцію 
```python
    def count_letters(self):
        """Метод для підрахунку кількості букв в імені"""
        return len(self.name)
        ```
    