from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFormLayout, QLineEdit, QDialog
)
from PyQt6.QtCore import Qt, QSize  # Import QSize here
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QRadioButton, QCheckBox, QSlider, QSpinBox, QProgressBar, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QListWidget, QMenuBar, QFileDialog, QToolButton, QDial, QDateEdit, QTimeEdit, QFontComboBox
import eTraffic
from eTraffic import Router
from RawProcessing import Utils
import json

#Info before-hand

#The colors , font and stuff is chosen by AI , also the buttons structure also chosen by AI  :
#1) I suck at designing UIs to look cool
#2) Python UI
#3) I focused on the frame-work backend (eTraffic) more because that's the whole logic behind every button 







#Window for Routers #TODO
class RouterDashboard(QWidget):
    def __init__(self):
        super().__init__()
       
        with open("router_database.json","r") as data:
            find = json.load(data)
            d = find["user_routers"]
            routers_names = []
            for router in d:
                routers_names.append(router["router_name"])
           
            print(routers_names)







        self.setWindowTitle("Router Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        
        layout = QVBoxLayout()
        title = QLabel("Welcome,Andrew")
        title.setFont(QFont("Segoe UI", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        

    

        # Add your router specific widgets here (e.g., settings, controls, etc.)
        router_info_label = QLabel("The routers:")
        router_info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(router_info_label) 
        
        

        router_list = QComboBox()
        for item in routers_names:
            router_list.addItem(item)
        layout.addWidget(router_list)

        for btn in [router_list]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedSize(120, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    color: #dcdcdc;
                    border: 2px solid #3c3c3c;
                    border-radius: 8px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #3c3c3c;
                }
                QPushButton:checked {
                    background-color: #0078d7;
                    color: white;
                    border: 2px solid #0078d7;
                }
            """)
        


        self.setLayout(layout)

    def get_routers_info(self):
     with open("router_database.json","r") as data:
        reading = json.load(data)
        routers = reading["user_routers"]
        print(routers)


#Window for switches #TODO
class SwitchDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Switch Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        
        layout = QVBoxLayout()
        title = QLabel("Switch Dashboard")
        title.setFont(QFont("Segoe UI", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Add your switch specific widgets here (e.g., settings, controls, etc.)
        switch_info_label = QLabel("Switch settings go here...")
        layout.addWidget(switch_info_label)

        self.setLayout(layout)



#The window where you will change your settings #TODO
class SettingsDashBoard(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent, flags)
        self.setWindowTitle("Settings DashBoard")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")


#Main GUI Window
class ModernUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("eTraffic")
        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("background-color: #1e1e1e;")  # Dark background
        self.init_ui()


    def init_ui(self):
        #Info from user , take these from the auth database , etc later on...
        with open("userinfo.json","r") as user:
            data = json.load(user)
            username = data["username"]
            #TODO more here fetch data
 
  
   
        #The main choice , Routers,Switches,Servers
        self.router_button = QPushButton("Routers")
        self.switch_button = QPushButton("Switches")
        self.servers_pc_button = QPushButton("Servers")


        for btn in [self.router_button, self.switch_button,self.servers_pc_button]:
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedSize(120, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    color: #dcdcdc;
                    border: 2px solid #3c3c3c;
                    border-radius: 8px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #3c3c3c;
                }
                QPushButton:checked {
                    background-color: #0078d7;
                    color: white;
                    border: 2px solid #0078d7;
                }
            """)

        self.router_button.setChecked(True)  # Default selection

        # Connect toggle logic
        self.router_button.clicked.connect(self.open_router_dashboard)
        self.switch_button.clicked.connect(self.open_switch_dashboard)

        # === Layout for Router and Switch buttons ===
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        button_layout.addStretch()
        button_layout.addWidget(self.router_button)
        button_layout.addWidget(self.switch_button)
        button_layout.addWidget(self.servers_pc_button)
        button_layout.addStretch()

        #The buttons github,setting
        self.settings_button = QPushButton()
        self.github_button = QPushButton()
        self.settings_button.setIcon(QIcon("settings.png"))
        self.github_button.setIcon(QIcon("github.png"))
        self.github_button.clicked.connect(self.github_open)
        self.settings_button.clicked.connect(self.settings_open)
        self.settings_button.setIconSize(QSize(32, 32)) 
        self.github_button.setIconSize(QSize(32, 32))  

        # Style for icon buttons
        for btn in [self.settings_button, self.github_button]:
            btn.setFixedSize(50, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    border-radius: 25px;
                    border: 2px solid #3c3c3c;
                }
                QPushButton:hover {
                    background-color: #3c3c3c;
                }
            """)

        # === Layout for bottom-left buttons ===
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.settings_button)
        bottom_layout.addWidget(self.github_button)
        bottom_layout.addStretch()

        # === Main layout ===
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        main_layout.addLayout(bottom_layout)  # Add the bottom layout here

        self.setLayout(main_layout)

    def open_router_dashboard(self):
        self.router_dashboard = RouterDashboard()  # Create Router Dashboard
        self.router_dashboard.show()  # Show the Router Dashboard
        self.close()  # Close the main window after opening Router Dashboard

    def open_switch_dashboard(self):
        self.switch_dashboard = SwitchDashboard()  # Create Switch Dashboard
        self.switch_dashboard.show()  # Show the Switch Dashboard
        self.close()  # Close the main window after opening Switch Dashboard





    #Redirect to the site if you open the github button
    def github_open(self):
        import webbrowser
        webbrowser.open("https://github.com/BeepBoopesMore/eTrafficApp")
    #Open the dashboard if you click on the setting button
    def settings_open(self):
        self.settings_dashboard = SettingsDashBoard()
        self.settings_dashboard.show()












if __name__ == "__main__":
    app = QApplication([])
    window = ModernUI()
    window.show()
    app.exec()
