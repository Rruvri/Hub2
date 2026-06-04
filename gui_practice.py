import saves



import sys
from PyQt6.QtWidgets import (QApplication, QLabel,
                             QWidget, QGridLayout,
                             QFormLayout, QLineEdit,
                             QDialog, QHBoxLayout,
                             QDialogButtonBox, QMainWindow,
                             QStackedLayout, QComboBox,
                             QCalendarWidget, QDateEdit,
                             QDateTimeEdit, QCheckBox,
                             QVBoxLayout, QListWidget, 
                             QPushButton, QTextEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hub2 Testing")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        h_l = QHBoxLayout()


        main_list = QListWidget()
        for item in saves.master_goals.goals_archive["Daily"]:
            main_list.addItem(str(item.start_dt))

        h_l.addWidget(main_list)
        central_widget.setLayout(h_l)

        display = QTextEdit()

        main_list.itemClicked.connect(self.display_item)

    
    def display_item(self)









if __name__ == "__main__":
    saves.load_initial_save()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()