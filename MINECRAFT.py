import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from logic import *

class simbolos:
    def __init__(self, nombre, imagen, caracteristicas):
        self.nombre = nombre
        self.imagen = imagen
        self.caracteristicas = caracteristicas

class QuienEsQuienMinecraft:
    def __init__(self):
        self.bloques = [
            simbolos("Tierra", "imagenes/dirt.jpg", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False}),
            simbolos("Piedra", "imagenes/stone.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False}),
            simbolos("Cristal", "imagenes/glass.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": False}),
            simbolos("Antorcha", "imagenes/torch.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": True}),
            simbolos("Bloque de Diamante", "imagenes/diamante.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False}),
            simbolos("Hoja", "imagenes/leaves.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False}),
            simbolos("Obsidiana", "imagenes/obsidian.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": True, "luminoso": False}),
            simbolos("Redstone", "imagenes/redstone_block.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": True}),
            simbolos("Agua", "imagenes/water.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False}),
            simbolos("Madera", "imagenes/wood.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
            simbolos("TNT", "imagenes/tnt.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
            simbolos("Calabaza", "imagenes/pumpkin.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False}),
        ]
        #self.bloque_objetivo = next(bloque for bloque in self.bloques if bloque.nombre == "Bloque de Diamante")
        self.bloque_objetivo = random.choice(self.bloques)
        self.conocimiento = And()  # Base inicial vacía
        self.preguntas_hechas = 0
        print(f"El bloque objetivo es: {self.bloque_objetivo.nombre}")

    def hacer_pregunta(self, caracteristica):
        self.preguntas_hechas += 1
        respuesta = self.bloque_objetivo.caracteristicas[caracteristica]

        if respuesta:
            self.conocimiento = And(self.conocimiento, Symbol(caracteristica))
            print(f"La característica '{caracteristica}' es verdadera.")
        else:
            self.conocimiento = And(self.conocimiento, Not(Symbol(caracteristica)))
            print(f"La característica '{caracteristica}' es falsa.")

        # Ejemplo de lógica adicional
        if caracteristica == "natural" and not respuesta:
            self.conocimiento = And(self.conocimiento, Not(Symbol("transparente")))
            print("Como no es natural, también es cierto que no es transparente.")

        if caracteristica == "luminoso" and respuesta:
            self.conocimiento = And(self.conocimiento, Symbol("crafteable"))
            print("Como es luminoso, también se supone que es crafteable.")

        print(f"Conocimiento actual: {self.conocimiento}")
        return respuesta

    def generar_conocimiento(self):
        # Generar conocimiento basado en las características
        caracteristicas = ["natural", "transparente", "crafteable", "resistente", "luminoso"]

        for caracteristica in caracteristicas:
            self.hacer_pregunta(caracteristica)

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
        self.historial_preguntas = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minecraft: Quién es Quién')
        self.setGeometry(100, 100, 1200, 800)

        # Establecer fondo
        background = QImage("imagenes/minecraft_background.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        layout_principal = QHBoxLayout()

        # Panel de bloques (sin cambios)
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

        # Panel de preguntas (modificado)
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
            boton.clicked.connect(lambda _, c=caracteristica, p=pregunta: self.hacer_pregunta(c, p))
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

        # Área de historial de preguntas
        self.historial_widget = QWidget()
        self.historial_layout = QVBoxLayout()
        self.historial_widget.setLayout(self.historial_layout)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.historial_widget)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgba(255, 255, 255, 120);
                border-radius: 10px;
            }
        """)
        
        layout_preguntas.addWidget(scroll_area)

        panel_preguntas.setLayout(layout_preguntas)

        layout_principal.addWidget(panel_bloques, 2)
        layout_principal.addWidget(panel_preguntas, 1)

        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def hacer_pregunta(self, caracteristica, pregunta):
        respuesta = self.juego.hacer_pregunta(caracteristica)
        self.label_resultado.setText(f"{'Sí' if respuesta else 'No'}")
        
        # Añadir la pregunta y respuesta al historial
        respuesta_texto = "Sí" if respuesta else "No"
        nueva_pregunta = QLabel(f"{pregunta} {respuesta_texto}")
        nueva_pregunta.setStyleSheet("""
            background-color: rgba(255, 255, 255, 150);
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
            color: #333;
            margin-bottom: 5px;
        """)
        self.historial_layout.addWidget(nueva_pregunta)
        self.historial_preguntas.append(nueva_pregunta)
        
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