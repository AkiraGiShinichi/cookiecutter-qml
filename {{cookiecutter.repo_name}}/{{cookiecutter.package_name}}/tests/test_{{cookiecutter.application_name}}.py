import pytest

import pkg_resources
try: # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMainWindow
    print("PySide2 was used")
except ImportError: # PyQt5
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
    from PyQt5.Qt import Qt
    from PyQt5.QtWidgets import QApplication, QMainWindow
    print("PyQt5 was used")
else:
    print('Qt for Python was not installed.')
    exit(1)
from PyQt5.QtWidgets import QDialog, QFileDialog

from {{ cookiecutter.package_name }} import {{ cookiecutter.application_name }}


@pytest.fixture
def window(qtbot):
    """Pass the application to the test functions via a pytest fixture."""
    new_window = {{cookiecutter.application_name }}.{{cookiecutter.application_title }}()
    qtbot.add_widget(new_window)
    new_window.show()
    return new_window


def test_window_title(window):
    """Check that the window title shows as declared."""
    assert window.windowTitle() == '{{ cookiecutter.application_title }}'


def test_window_geometry(window):
    """Check that the window width and height are set as declared."""
    assert window.width() == 1024
    assert window.height() == 768


def test_open_file(window, qtbot, mocker):
    """Test the Open File item of the File submenu.

    Qtbot clicks on the file sub menu and then navigates to the Open File item. Mock creates
    an object to be passed to the QFileDialog.
    """
    qtbot.mouseClick(window.file_sub_menu, Qt.LeftButton)
    qtbot.keyClick(window.file_sub_menu, Qt.Key_Down)
    mocker.patch.object(QFileDialog, 'getOpenFileName', return_value=('', ''))
    qtbot.keyClick(window.file_sub_menu, Qt.Key_Enter)


def test_about_dialog(window, qtbot, mocker):
    """Test the About item of the Help submenu.

    Qtbot clicks on the help sub menu and then navigates to the About item. Mock creates
    a QDialog object to be used for the test.
    """
    qtbot.mouseClick(window.help_sub_menu, Qt.LeftButton)
    qtbot.keyClick(window.help_sub_menu, Qt.Key_Down)
    mocker.patch.object(QDialog, 'exec_', return_value='accept')
    qtbot.keyClick(window.help_sub_menu, Qt.Key_Enter)
