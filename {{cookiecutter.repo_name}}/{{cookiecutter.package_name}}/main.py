# This Python file uses the following encoding: utf-8
import sys
import os

from {{ cookiecutter.pyside_version }}.QtGui import QGuiApplication
from {{ cookiecutter.pyside_version }}.QtQml import QQmlApplicationEngine

from {{ cookiecutter.package_name }} import backend


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    main = backend.Backend()
    engine.rootContext().setContextProperty("backend", main)

    engine.load(os.path.join(os.path.dirname(__file__), "qml", "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())