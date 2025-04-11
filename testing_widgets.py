from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QRadioButton, QCheckBox, QSlider, QSpinBox, QProgressBar, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QListWidget, QMenuBar, QFileDialog, QToolButton, QDial, QDateEdit, QTimeEdit, QFontComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Widgets Showcase")
        self.setGeometry(100, 100, 800, 700)

        layout = QVBoxLayout()

        # QLabel
        label = QLabel("This is a QLabel")
        layout.addWidget(label)

        # QPushButton
        button = QPushButton("Click Me")
        layout.addWidget(button)

        # QLineEdit
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter text here")
        layout.addWidget(line_edit)

        # QTextEdit
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Write something here...")
        layout.addWidget(text_edit)

        # QComboBox
        combo = QComboBox()
        combo.addItem("Option 1")
        combo.addItem("Option 2")
        combo.addItem("Option 3")
        layout.addWidget(combo)

        # QRadioButton
        radio_button1 = QRadioButton("Radio Option 1")
        radio_button2 = QRadioButton("Radio Option 2")
        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)

        # QCheckBox
        checkbox = QCheckBox("Accept Terms")
        layout.addWidget(checkbox)

        # QSlider
        slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(slider)

        # QSpinBox
        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        layout.addWidget(spinbox)

        # QProgressBar
        progress = QProgressBar()
        progress.setRange(0, 100)
        layout.addWidget(progress)

        # Update ProgressBar
        for i in range(101):
            time.sleep(0.05)
            progress.setValue(i)

        # QTabWidget
        tab_widget = QTabWidget()
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("This is Tab 1"))
        tab1.setLayout(tab1_layout)
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("This is Tab 2"))
        tab2.setLayout(tab2_layout)
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        layout.addWidget(tab_widget)

        # QMenuBar
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        layout.setMenuBar(menu_bar)

        # QFileDialog
        def open_file_dialog():
            file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
            if file_name:
                print(f"File selected: {file_name}")
        button.clicked.connect(open_file_dialog)

        # QTableWidget
        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(2)
        table.setItem(0, 0, QTableWidgetItem("Row 1, Col 1"))
        table.setItem(0, 1, QTableWidgetItem("Row 1, Col 2"))
        table.setItem(1, 0, QTableWidgetItem("Row 2, Col 1"))
        table.setItem(1, 1, QTableWidgetItem("Row 2, Col 2"))
        table.setItem(2, 0, QTableWidgetItem("Row 3, Col 1"))
        table.setItem(2, 1, QTableWidgetItem("Row 3, Col 2"))
        layout.addWidget(table)

        # QListWidget
        list_widget = QListWidget()
        list_widget.addItem("Item 1")
        list_widget.addItem("Item 2")
        list_widget.addItem("Item 3")
        layout.addWidget(list_widget)

        # QToolButton
        tool_button = QToolButton()
        tool_button.setText("Tool Button")
        tool_button.setIcon(QIcon.fromTheme("edit-copy"))
        layout.addWidget(tool_button)

        # QDial
        dial = QDial()
        dial.setRange(0, 100)
        dial.setValue(50)
        layout.addWidget(dial)

        # QDateEdit
        date_edit = QDateEdit()
        layout.addWidget(date_edit)

        # QTimeEdit
        time_edit = QTimeEdit()
        layout.addWidget(time_edit)

        # QFontComboBox
        font_combo = QFontComboBox()
        layout.addWidget(font_combo)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
