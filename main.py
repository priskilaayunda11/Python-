import sys
 
# import module form pyqt5
from tkinter import QApplication, QLabel, QWidget
 
# create instance
app = QApplication(sys.argv)
window = QWidget()
 
# create title, and instance app
window.setWindowTitle('Simple App QT')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
window.move(60, 16)
 
# create simple message
hello = QLabel('<h1> Halo saya sedang belajar membuat aplikasi desktop</h1>', parent=window)
web = QLabel('<h2> pesonainformatika.com</h2>', parent=window)
web.move(60,60)
hello.move(60, 30)
 
# display app
window.show()
 
# run app
sys.exit(app.exec_())