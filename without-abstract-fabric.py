# Код без абстракции

# Компоненты для Windows
class WindowsButton:
    def render(self):
        print("Отрисовка кнопки для Windows")

class WindowsTextField:
    def render(self):
        print("Отрисовка текстового поля для Windows")

# Компоненты для macOS
class MacOSButton:
    def render(self):
        print("Отрисовка кнопки для macOS")

class MacOSTextField:
    def render(self):
        print("Отрисовка текстового поля для macOS")

# Клиентский код
def create_gui_for_os(os_name):
    if os_name == "Windows":
        button = WindowsButton()
        text_field = WindowsTextField()
    elif os_name == "macOS":
        button = MacOSButton()
        text_field = MacOSTextField()
    else:
        raise ValueError("Неизвестная операционная система")

    button.render()
    text_field.render()

# Используем код
create_gui_for_os("Windows")
create_gui_for_os("macOS")