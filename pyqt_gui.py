import sys
from PyQt6.QtWidgets import (QApplication, QLabel,
                              QWidget, QGridLayout,
                                QFormLayout, QLineEdit,
                                  QDialog, QHBoxLayout,
                                    QDialogButtonBox)

'''
app = QApplication([])
window = QWidget()
window.setWindowTitle("RaviHub")
window.setGeometry(100, 100, 500, 300)  
#helloMsg = QLabel("<h1>Welcome to RaviHub!<h1>", parent=window)
#helloMsg.move(100, 0)

mainLayout = QGridLayout()
entryLayout = QFormLayout()

entryLayout.addRow("Main goal", QLineEdit())
entryLayout.addRow("Secondary goal", QLineEdit())

mainLayout.addLayout(entryLayout, 2, 0)

window.setLayout(mainLayout)
'''

class EntryWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Entry Window")
        #self.setGeometry(100, 100, 500, 300) 
        dialogLayout = QHBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Main goal", QLineEdit())
        formLayout.addRow("Secondary goal", QLineEdit())
        
        #add buttons for extra goals
        dialogLayout.addLayout(formLayout)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = EntryWindow()
    window.show()
    sys.exit(app.exec())




#window.show()
#sys.exit(app.exec())