
import saves
import goals


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
                             QPushButton, QTableWidget,
                             QTableWidgetItem)


goals_test = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RaviHUB")
        central_widget = QWidget()

        



        #tasks
        task_layout = QHBoxLayout()

        task_entry_form = QFormLayout()
        
        task_entry = QLineEdit()
        task_entry_form.addRow(QLabel("Enter Task"), task_entry)

        task_date_entry = QDateEdit()
        task_entry_form.addRow(QLabel("Enter Due Date"), task_date_entry)


        task_list_view = QListWidget()
        task_list_view.addItems([str(g.start_dt) for g in goals_test.goals_archive["Daily"]])
        task_list_view.itemClicked.connect(self.display_entry)

        self.snapshot_view = QTableWidget()

        

        task_layout.addLayout(task_entry_form)
        task_layout.addWidget(task_list_view)
        task_layout.addWidget(self.snapshot_view)

        central_widget.setLayout(task_layout)

        self.setCentralWidget(central_widget)
    
    def display_entry(self, dt):
        for item in goals_test.goals_archive["Daily"]:
            if str(item.start_dt) == dt.text():
                target = item
                self.snapshot_view.clear()
                self.snapshot_view.setRowCount(len(item.goals_dict.keys()))
                self.snapshot_view.setColumnCount(1)
                self.snapshot_view.setVerticalHeaderLabels(item.goals_dict.keys())
                row = 0
                for i in target.goals_dict.keys():
                    self.snapshot_view.setItem(row, 0, QTableWidgetItem(str(target.goals_dict[i])))
                    row +=1





if __name__ == "__main__":
    saves.load_initial_save()
    goals_test = saves.master_goals
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()