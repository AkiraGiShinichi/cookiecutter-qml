from {{ cookiecutter.pyside_version }}.QtCore import QObject, Signal, Slot


class Backend(QObject):
    def __init__(self) -> None:
        super().__init__()

    def __del__(self):
        pass