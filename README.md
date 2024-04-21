# Звіт з лабораторної роботи №4. Відмова від спадку. Альтернативні класи з різними інтерфейсами.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
### Мета: Рефакторінг коду коли підклас використовує лише малу частину успадкованих методів і властивостей суперкласа.

### Завдання 1: Наданий код
    
    class Animal:
        def speak(self):
            pass

        def move(self):
            pass

    class Dog(Animal):
        pass

    # Приклад використання класів
    dog = Dog()
    dog.speak()
    dog.move()

### Рішення

     class Animal:
        def speak(self):
          pass

        def move(self):
          pass

    class Dog:
        def __init__(self):
            self.animal = Animal()

        def speak(self):
            self.animal.speak()

        def move(self):
            self.animal.move()

    dog = Dog()
    dog.speak()
    dog.move()

Клас Dog вже не успадковується від класу Animal. 
Замість цього, він створює екземпляр класу Animal у своєму конструкторі і використовує цей екземпляр для делегування викликів методів базового класу. Таким чином, замінено успадкування делегуванням.

### Завдання 2: Наданий код 

    class Square:
        def area_square(self, side):
            return side ** 2

    class Circle:
        def area_circle(self, radius):
            return 3.14 * radius ** 2

    # Приклад використання класів
    square = Square()
    print("Area of square:", square.area_square(5))

    circle = Circle()
    print("Area of circle:", circle.area_circle(3))

### Рішення

    class Shape:
    def area(self):
        pass

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    # Приклад використання класів
    square = Square(5)
    print("Area of square:", square.area())
    circle = Circle(3)
    print("Area of circle:", circle.area())

Отже, був створений новий базовий клас Shape, який містить метод area(). Цей клас визначає загальний інтерфейс для обчислення площі будь-якої фігури.
Обидва класи Square і Circle тепер успадковуються від базового класу Shape. Це дозволяє їм успадкувати метод area() та реалізовувати його.
Конструктори класів Square і Circle були модифіковані, щоб вони приймали вхідні параметри, необхідні для обчислення площі фігури, тобто довжину сторони для квадрата, і радіус для кола.
В обох класах Square і Circle було реалізовано метод area(), який обчислює площу відповідно до формул для квадрата і кола.
При використанні класів, тепер викликаються методи area() безпосередньо, без додавання префіксів area_square або area_circle, як це було у попередньому коді.
