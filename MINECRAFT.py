import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, QMessageBox, QFrame
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from logic import *

class Symbol:
    def __init__(self, nombre, imagen, caracteristicas):
        self.nombre = nombre
        self.imagen = imagen
        self.caracteristicas = caracteristicas

class QuienEsQuienMinecraft:
    def __init__(self):
        self.bloques = [
            Symbol("Tierra", "imagenes/dirt.jpg", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False}),
            Symbol("Piedra", "imagenes/stone.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False}),
            Symbol("Cristal", "imagenes/glass.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": False}),
            Symbol("Antorcha", "imagenes/torch.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": True}),
            Symbol("Diamante", "imagenes/diamante.png", {"natural": False, "transparente": True, "crafteable": False, "resistente": True, "luminoso": False}),
            Symbol("Hoja", "imagenes/leaves.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False}),
            Symbol("Obsidiana", "imagenes/obsidian.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": True, "luminoso": False}),
            Symbol("Redstone", "imagenes/redstone_block.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": True}),
            Symbol("Agua", "imagenes/water.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False}),
            Symbol("Madera", "imagenes/wood.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
            Symbol("TNT", "imagenes/tnt.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
            Symbol("Calabaza", "imagenes/pumpkin.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
        ]
        #self.bloque_objetivo = random.choice(self.bloques)
        self.bloque_objetivo = random.choice(self.bloques)
        self.conocimiento = And()
        self.preguntas_hechas = 0

        print(f"El bloque objetivo es: {self.bloque_objetivo.nombre}")

    def hacer_pregunta(self, caracteristica):
        self.preguntas_hechas += 1
        respuesta = self.bloque_objetivo.caracteristicas[caracteristica]
        if respuesta:
            self.conocimiento.add(Symbol(f"{caracteristica}"))
        else:
            self.conocimiento.add(Not(Symbol(f"{caracteristica}")))
        return respuesta

    def adivinar(self, nombre):
        return nombre == self.bloque_objetivo.nombre

    def eliminar_bloques(self):
        bloques_eliminados = []
        for bloque in self.bloques:
            modelo = {caract: valor for caract, valor in bloque.caracteristicas.items()}
            if not self.conocimiento.evaluate(modelo):
                bloques_eliminados.append(bloque)
        for bloque in bloques_eliminados:
            self.bloques.remove(bloque)
        return bloques_eliminados

class VentanaJuego(QMainWindow):
    def __init__(self):
        super().__init__()
        self.juego = QuienEsQuienMinecraft()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minecraft: Quién es Quién')
        self.setGeometry(100, 100, 1200, 800)

        background = QImage("imagenes/minecraft_background.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        layout_principal = QHBoxLayout()

        panel_bloques = QFrame()
        panel_bloques.setStyleSheet("background-color: rgba(139, 69, 19, 150); border-radius: 10px;")
        layout_bloques = QGridLayout()
        for i, bloque in enumerate(self.juego.bloques):
            boton = QPushButton()
            boton.setIcon(QIcon(QPixmap(bloque.imagen)))
            boton.setIconSize(QSize(80, 80))
            boton.setFixedSize(100, 100)
            boton.setStyleSheet("""
                QPushButton {
                    background-color: #8B4513;
                    border: 2px solid #4A2511;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #A0522D;
                }
                QPushButton:pressed {
                    background-color: #6B4226;
                }
            """)
            boton.clicked.connect(lambda _, name=bloque.nombre: self.adivinar_bloque(name))
            boton.setToolTip(bloque.nombre)
            layout_bloques.addWidget(boton, i // 4, i % 4)
        panel_bloques.setLayout(layout_bloques)

        panel_preguntas = QFrame()
        panel_preguntas.setStyleSheet("background-color: rgba(60, 60, 60, 180); border-radius: 10px;")
        layout_preguntas = QVBoxLayout()
        
        self.label_resultado = QLabel("¡Adivina el bloque de Minecraft!")
        self.label_resultado.setStyleSheet("""
            background-color: rgba(255, 255, 255, 180);
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        """)
        layout_preguntas.addWidget(self.label_resultado)
        
        preguntas = ["¿Es un bloque natural?", "¿Es transparente?", "¿Se puede craftear?", "¿Es resistente?", "¿Emite luz?"]
        caracteristicas = ["natural", "transparente", "crafteable", "resistente", "luminoso"]
        for pregunta, caracteristica in zip(preguntas, caracteristicas):
            boton = QPushButton(pregunta)
            boton.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px;
                    border-radius: 8px;
                    font-size: 16px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:pressed {
                    background-color: #3e8e41;
                }
            """)
            boton.clicked.connect(lambda _, c=caracteristica: self.hacer_pregunta(c))
            layout_preguntas.addWidget(boton)
        
        self.label_preguntas = QLabel(f"Preguntas hechas: {self.juego.preguntas_hechas}")
        self.label_preguntas.setStyleSheet("""
            background-color: rgba(255, 255, 255, 180);
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        """)
        layout_preguntas.addWidget(self.label_preguntas)

        panel_preguntas.setLayout(layout_preguntas)

        layout_principal.addWidget(panel_bloques, 2)
        layout_principal.addWidget(panel_preguntas, 1)

        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def hacer_pregunta(self, caracteristica):
        respuesta = self.juego.hacer_pregunta(caracteristica)
        self.label_resultado.setText(f"{'Sí' if respuesta else 'No'}")
        eliminados = self.juego.eliminar_bloques()
        for bloque in eliminados:
            for i in range(self.centralWidget().layout().itemAt(0).widget().layout().count()):
                boton = self.centralWidget().layout().itemAt(0).widget().layout().itemAt(i).widget()
                if isinstance(boton, QPushButton) and boton.toolTip() == bloque.nombre:
                    boton.setEnabled(False)
                    boton.setStyleSheet("background-color: rgba(100, 100, 100, 150); border: 2px solid #333;")
                    break
        self.label_preguntas.setText(f"Preguntas hechas: {self.juego.preguntas_hechas}")

    def adivinar_bloque(self, nombre):
        if self.juego.adivinar(nombre):
            QMessageBox.information(self, "¡Felicidades!", f"¡Correcto! El bloque era {nombre}. Lo adivinaste en {self.juego.preguntas_hechas} preguntas.")
            self.close()
        else:
            QMessageBox.critical(self, "¡Perdiste!", f"Incorrecto. El bloque no era {nombre}. El bloque correcto era {self.juego.bloque_objetivo.nombre}.")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ventana = VentanaJuego()
    ventana.show()
    sys.exit(app.exec_())