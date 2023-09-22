# Код с абстракцией (Абстрактная фабрика)

from abc import ABC, abstractmethod

# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text_field(self):
        pass

# Конкретные продукты для Windows
class WindowsButton(Button):
    def render(self):
        print("Отрисовка кнопки для Windows")

class WindowsTextField(TextField):
    def render(self):
        print("Отрисовка текстового поля для Windows")

# Конкретные продукты для macOS
class MacOSButton(Button):
    def render(self):
        print("Отрисовка кнопки для macOS")

class MacOSTextField(TextField):
    def render(self):
        print("Отрисовка текстового поля для macOS")

# Конкретные фабрики для Windows и macOS
class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_field(self):
        return WindowsTextField()

class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_text_field(self):
        return MacOSTextField()

# Клиентский код
def create_gui(factory):
    button = factory.create_button()
    text_field = factory.create_text_field()
    button.render()
    text_field.render()

# Используем код
windows_factory = WindowsGUIFactory()
macos_factory = MacOSGUIFactory()

create_gui(windows_factory)  # Создает и отрисовывает компоненты для Windows
create_gui(macos_factory)    # Создает и отрисовывает компоненты для macOS