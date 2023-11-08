import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from Lista_2_43132 import MyTestApp

@pytest.fixture
def app(qtbot):
    app = MyTestApp()
    qtbot.addWidget(app)
    return app

def test_get_ipv4_info(app, qtbot):
    QTest.mouseClick(app.button1, Qt.LeftButton)
    
    assert "Host_name:" in app.text_view.toPlainText()
    assert "IPv4 Address:" in app.text_view.toPlainText()

def test_get_proxy_info(app, qtbot):
    QTest.mouseClick(app.button2, Qt.LeftButton)
    
    assert "Proxy aktywne" in app.text_view.toPlainText() or "Proxy nieaktywne" in app.text_view.toPlainText()

def test_get_system_info(app, qtbot):
    QTest.mouseClick(app.button3, Qt.LeftButton)
    
    assert "System:" in app.text_view.toPlainText()
    assert "CPU:" in app.text_view.toPlainText()
    assert "Memory:" in app.text_view.toPlainText()

def test_get_bios_version(app, qtbot):
    QTest.mouseClick(app.button4, Qt.LeftButton)
    
    assert "BIOS Version:" in app.text_view.toPlainText() or "BIOS nie znaleziono" in app.text_view.toPlainText()

def test_get_host_name(app, qtbot):
    QTest.mouseClick(app.button5, Qt.LeftButton)
    
    assert "Host_Name:" in app.text_view.toPlainText()

# Testy do komend w MyCmd
def test_my_cmd_ipv4(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_ipv4("") is None

def test_my_cmd_proxy(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_proxy("") is None

def test_my_cmd_sysinfo(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_sysinfo("") is None

def test_my_cmd_bios(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_bios("") is None

def test_my_cmd_hostname(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_hostname("") is None

def test_my_cmd_exit(app, qtbot):
    my_cmd = app.my_cmd
    assert my_cmd.do_exit("") is True
