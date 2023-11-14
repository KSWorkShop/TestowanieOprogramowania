import sys
import os
import socket
import platform
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication
from Lista_2_Msz import MyTestApp

def test_get_ipv4_info_invalid_hostname():
    app = MyTestApp()
    with patch('socket.gethostname', return_value=None):
        app.get_ipv4_info()
        assert "Błąd: Nieprawidłowa nazwa hosta" in app.text_view.toPlainText()

def test_get_bios_version_file_not_found():
    app = MyTestApp()
    with patch('builtins.open', side_effect=FileNotFoundError):
        app.get_bios_version()
        assert "Błąd: Brak pliku z informacjami o wersji BIOS" in app.text_view.toPlainText()

def test_get_system_info_cpu_error():
    app = MyTestApp()
    with patch('psutil.cpu_count', side_effect=Exception):
        app.get_system_info()
        assert "Błąd: Nie można odczytać informacji o CPU" in app.text_view.toPlainText()

def test_get_proxy_info_error():
    app = MyTestApp()
    with patch.dict(os.environ, {'http_proxy': 'http://proxy.example.com'}), \
         patch('os.environ.get', side_effect=Exception):
        app.get_proxy_info()
        assert "Błąd: Nie można odczytać informacji o proxy" in app.text_view.toPlainText()

def test_main_window():
    app = QApplication(sys.argv)
    window = MyTestApp()
    window.show()
    assert window.isVisible()

if __name__ == '__main__':
    sys.exit(QApplication(sys.argv).exec_())
