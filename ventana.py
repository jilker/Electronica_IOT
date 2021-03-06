from ventana_ui import *
from peliculas import Peliculas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from video_class import *
import urllib.request
import json
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.peliculas = Peliculas()
        self.video = Video()
        self.video.start()
        self.fill_table()
        self.Generos_lista.itemDoubleClicked.connect(self.allow_genre)
        self.year_spin.valueChanged.connect(self.update_year)
        self.Buscar_button.clicked.connect(self.search)
        self.Siguiente_button.clicked.connect(self.show_info)
        self.Aceptar_button.clicked.connect(self.selecionar_button)
        self.Siguiente_button.setEnabled(False)
        self.Aceptar_button.setEnabled(False)
        self.status = [1,0]
        self.genre_selected = []
    def search(self):
        self.Siguiente_button.setEnabled(True)
        self.Aceptar_button.setEnabled(True)
        self.res = self.peliculas.search("1")
        self.res = self.res['results']
        self.status = [1,0]
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
        it = self.status[1]
        url = 'https://image.tmdb.org/t/p/w500' + self.res[it]['poster_path']
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self.Pictures.setPixmap(QtGui.QPixmap(image))
        self.textBrowser.setText(self.res[it]['original_title'])
        self.textBrowser.append(self.res[it]['overview'])
        self.status[1] += 1
        if self.res.__len__()==self.status[1]:
            self.next_page()
    def next_page(self):
        self.status[1] = 0
        self.status[0] += 1
        self.res = self.peliculas.search(str(self.status[0]))
        self.res = self.res['results']
    def selecionar_button(self):
        print('Coger prediccion')
        self.prediction = [sentimiento/sum(self.video.prediction) for sentimiento in self.video.prediction]

        it = self.status[1]
        print('Coger generos')
        self.genre_selected = self.peliculas.genre_ids2names(self.res[it-1]['genre_ids'])
        print('Abrir JSON')
        with open('save.json') as f:
            self.load=json.load(f)
        for genre in self.genre_selected:
            self.load[genre] = [x + y for x, y in zip(self.load[genre], self.prediction)]
        print('Escribir JSON')
        with open('save.json','w') as json_file:
            json.dump(self.load,json_file)
        QMessageBox.about(self, "Fin","Gracias por utilizar la aplicación")
        print(self.genre_selected)
        #self.video.terminate()
        self.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()