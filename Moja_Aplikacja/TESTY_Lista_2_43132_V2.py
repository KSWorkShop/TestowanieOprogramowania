import pytest
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from Lista_2_43132 import MyTestApp

@pytest.fixture
def app():
    app = QApplication([])
    yield app
    app.exit()


@pytest.fixture
def window(app):
    window = MyTestApp()
    window.show()
    yield window
    window.close()


def test_dark_stylesheet(window):
    assert window.styleSheet() is not None
    assert "background-color: #333;" in window.styleSheet()
    assert "color: #fff;" in window.styleSheet()
