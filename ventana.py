from ventana_ui import *
from peliculas import Peliculas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.peliculas = Peliculas()
        self.fill_table()
        self.Generos_lista.itemDoubleClicked.connect(self.allow_genre)
        self.year_spin.valueChanged.connect(self.update_year)
        self.Buscar_button.clicked.connect(self.search)
    def search(self):
        self.res = self.peliculas.search()
        self.res = self.res['results']
        self.show_info()
    def update_year(self, item):
        form = '-01-01' #Respetar el formato
        self.peliculas.year=str(item)+form
    def fill_table(self):
        names_list = [x['name'] for x in self.peliculas.genre_list]
        self.Generos_lista.addItems(names_list)
    def allow_genre(self,item):
        genre = next((genre for genre in self.peliculas.genre_list if genre["name"] == item.text()), None)
        if genre['Allow'] == 1:
            item.setBackground(QColor('#ff2d00'))
            genre['Allow']  = 0
        else:
            item.setBackground(QColor('#ffffff'))
            genre['Allow']  = 1
    def show_info(self):
        while 1:
            if self.Siguiente_button.clic():
                print('hola')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()