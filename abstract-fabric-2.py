from math import pi
from abc import ABC, abstractmethod

# Абстрактная фабрика для создания фигур
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

# Конкретная фабрика для создания кругов
class CircleFactory(ShapeFactory):
    def create_shape(self, radius):
        return Circle(radius)

# Конкретная фабрика для создания прямоугольников
class RectangleFactory(ShapeFactory):
    def create_shape(self, width, height):
        return Rectangle(width, height)

# Конкретная фабрика для создания треугольников
class TriangleFactory(ShapeFactory):
    def create_shape(self, base, height):
        return Triangle(base, height)

# Пример использования абстрактной фабрики
circle_factory = CircleFactory()
circle = circle_factory.create_shape(5)
print(f"Площадь круга: {circle.area()}")

rectangle_factory = RectangleFactory()
rectangle = rectangle_factory.create_shape(4, 6)
print(f"Площадь прямоугольника: {rectangle.area()}")

triangle_factory = TriangleFactory()
triangle = triangle_factory.create_shape(3, 4)
print(f"Площадь треугольника: {triangle.area()}")