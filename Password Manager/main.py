from main_window import MainWindow, QApplication
import sys
import mysql.connector
from my_socket import localhost

if __name__ == '__main__':
        try:
                cnx = mysql.connector.connect(
                        user="root",
                        password="root",
                        host=localhost,
                        database="passwords"
                )

                cursor = cnx.cursor()
                print("Database connection successful!")
        except Exception as _ex:
                print(f"Database connect error: {_ex}")
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        w = MainWindow()
        w.show()
        app.exec_()
