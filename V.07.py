import sys
import platform
import socket
import psutil
import os
import cmd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QPushButton
from PyQt5.QtCore import Qt

class MyTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MyTest_43132.exe")
        self.setGeometry(100, 100, 400, 400)

        self.text_view = QTextBrowser(self)
        self.text_view.setOpenExternalLinks(True)

        layout = QVBoxLayout()
        layout.addWidget(self.text_view)

        self.button1 = QPushButton("Moje IPv4")
        self.button1.clicked.connect(self.get_ipv4_info)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Proxy")
        self.button2.clicked.connect(self.get_proxy_info)
        layout.addWidget(self.button2)

        self.button3 = QPushButton("System Info")
        self.button3.clicked.connect(self.get_system_info)
        layout.addWidget(self.button3)

        self.button4 = QPushButton("Bios Version")
        self.button4.clicked.connect(self.get_bios_version)
        layout.addWidget(self.button4)

        self.button5 = QPushButton("Host Name")
        self.button5.clicked.connect(self.get_host_name)
        layout.addWidget(self.button5)

        self.setLayout(layout)

#--------------------------Zmiana kolorystyki na ciemny
        dark_stylesheet = """
        QWidget {
            background-color: #333;
            color: #fff;
        }
        QTextEdit {
            background-color: #222;
            color: #fff;
        }
        QPushButton {
            background-color: #444;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #555;
        }
        """
        self.setStyleSheet(dark_stylesheet)
        
#--------------------------------------informacje o sprzęcie

    def get_ipv4_info(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.text_view.setPlainText(f"Host_name: {hostname}\nIPv4 Address: {ip_address}")

    def get_proxy_info(self):
        proxy_info = os.environ.get("http_proxy", None)
        if proxy_info:
            self.text_view.setPlainText(f"Proxy aktywne. Proxy Info: {proxy_info}")
        else:
            self.text_view.setPlainText("Proxy nieaktywne.")

    def get_system_info(self):
        system_info = platform.uname()
        cpu_info = f"CPUs: {psutil.cpu_count(logical=False)}, Cores: {psutil.cpu_count(logical=True)}"
        memory_info = f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        self.text_view.setPlainText(f"System: {system_info.system} {system_info.release}\n"
                                   f"CPU: {cpu_info}\nMemory: {memory_info}")

    def get_bios_version(self):
        try:
            with open('/sys/class/dmi/id/bios_version') as f:
                bios_version = f.read().strip()
                self.text_view.setPlainText(f"BIOS Version: {bios_version}")
        except FileNotFoundError:
            self.text_view.setPlainText("BIOS nie znaleziono.")

    def get_host_name(self):
        hostname = socket.gethostname()
        self.text_view.setPlainText(f"Host_Name: {hostname}")

class MyCmd(cmd.Cmd):
    prompt = "(っ◕‿◕)っ:"

    def __init__(self, app):
        super().__init__()
        self.app = app

    def do_ipv4(self, line):
        self.app.get_ipv4_info()

    def do_proxy(self, line):
        self.app.get_proxy_info()

    def do_sysinfo(self, line):
        self.app.get_system_info()

    def do_bios(self, line):
        self.app.get_bios_version()

    def do_hostname(self, line):
        self.app.get_host_name()

    def do_exit(self, line):
        return True

def main():
    app = QApplication(sys.argv)
    window = MyTestApp()
    window.show()

    my_cmd = MyCmd(window)
    my_cmd.cmdloop()

if __name__ == '__main__':
    main()
