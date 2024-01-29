import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def create_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('NFL Game')

    layout = QVBoxLayout()

    label = QLabel('Get Ready')
    layout.addWidget(label)

    button = QPushButton('Click Me!')
    layout.addWidget(button)

    def on_button_clicked():
        print("Button clicked!")

    button.clicked.connect(on_button_clicked) 

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_window()
