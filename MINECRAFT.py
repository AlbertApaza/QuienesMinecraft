import sys
import random
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from logic import *
from colorama import Fore, Style, init

init()

class simbolos:
    def __init__(self, nombre, imagen, caracteristicas):
        self.nombre = nombre
        self.imagen = imagen
        self.caracteristicas = caracteristicas

class QuienEsQuienMinecraft:
    def __init__(self):
        self.bloques = [
            simbolos("Tierra", "imagenes/dirt.jpg", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Piedra", "imagenes/stone.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Cristal", "imagenes/glass.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Antorcha", "imagenes/torch.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": True, "gravedad": False, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
            simbolos("Bloque de Diamante", "imagenes/diamante.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Hoja", "imagenes/leaves.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": True, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Obsidiana", "imagenes/obsidian.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Redstone", "imagenes/redstone_block.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": True, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Agua", "imagenes/water.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": True, "interactivo": False, "creativo": False}),
            simbolos("Madera", "imagenes/wood.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("TNT", "imagenes/tnt.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
            simbolos("Calabaza", "imagenes/pumpkin.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
            
            simbolos("Grava", "imagenes/grava.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": True, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Arena", "imagenes/sand.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": True, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Arcilla", "imagenes/clay.png", {"natural": True, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Lava", "imagenes/lava.png", {"natural": True, "transparente": True, "crafteable": False, "resistente": False, "luminoso": True, "gravedad": False, "comer": False, "fluido": True, "interactivo": False, "creativo": False}),
            simbolos("Hierro", "imagenes/iron.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Esmeralda", "imagenes/emerald.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Oro", "imagenes/gold.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Roca Madre", "imagenes/bedrock.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": True, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": True}),
            simbolos("Esponja", "imagenes/sponge.png", {"natural": True, "transparente": False, "crafteable": False, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": False, "creativo": False}),
            simbolos("Bloque de Slime", "imagenes/slime.png", {"natural": False, "transparente": True, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
            simbolos("Tarta", "imagenes/cake.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": True, "fluido": False, "interactivo": True, "creativo": False}),
            simbolos("Cofre", "imagenes/chest.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": False, "luminoso": False, "gravedad": False, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
            simbolos("Yunque", "imagenes/anvil.png", {"natural": False, "transparente": False, "crafteable": True, "resistente": True, "luminoso": False, "gravedad": True, "comer": False, "fluido": False, "interactivo": True, "creativo": False}),
        ]
        self.bloque_objetivo = random.choice(self.bloques)
        self.conocimiento = And()
        self.preguntas_hechas = 0
        print(f"El bloque objetivo es: {self.bloque_objetivo.nombre}")
        self.print_possible_blocks()

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
        self.print_possible_blocks()
        return bloques_eliminados

    def print_possible_blocks(self):
        # Limpia la consola
        os.system('cls' if os.name == 'nt' else 'clear')

        # Imprime los bloques posibles
        print("\nBloques posibles:")
        for bloque in self.bloques:
            print(f"{Fore.GREEN}{bloque.nombre}{Style.RESET_ALL}")


class VentanaJuego(QMainWindow):
    def __init__(self):
        super().__init__()
        self.juego = QuienEsQuienMinecraft()
        self.historial_preguntas = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minecraft: Quién es Quién')
        self.setGeometry(100, 100, 1300, 800)

        # Establecer fondo
        background = QImage("imagenes/minecraft_background.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        layout_principal = QHBoxLayout()

        # Panel de bloques
        panel_bloques = QFrame()
        panel_bloques.setStyleSheet("""
            background-color: rgba(139, 69, 19, 180);
            border-radius: 15px;
            border: 2px solid #8B4513;
        """)
        layout_bloques = QGridLayout()
        for i, bloque in enumerate(self.juego.bloques):
            boton = QPushButton()
            boton.setIcon(QIcon(QPixmap(bloque.imagen)))
            boton.setIconSize(QSize(90, 90))
            boton.setFixedSize(110, 110)
            boton.setStyleSheet("""
                QPushButton {
                    background-color: #A0522D;
                    border: 3px solid #4A2511;
                    border-radius: 12px;
                }
                QPushButton:hover {
                    background-color: #CD853F;
                    border: 3px solid #8B4513;
                }
                QPushButton:pressed {
                    background-color: #8B4513;
                    border: 3px solid #4A2511;
                }
            """)
            boton.clicked.connect(lambda _, name=bloque.nombre: self.adivinar_bloque(name))
            boton.setToolTip(bloque.nombre)
            layout_bloques.addWidget(boton, i // 4, i % 4)
        panel_bloques.setLayout(layout_bloques)

        # Panel de preguntas
        panel_preguntas = QFrame()
        panel_preguntas.setStyleSheet("""
            background-color: rgba(60, 60, 60, 200);
            border-radius: 15px;
            border: 2px solid #333;
        """)
        layout_preguntas = QVBoxLayout()
        
        self.label_resultado = QLabel("¡Adivina el bloque de Minecraft!")
        self.label_resultado.setStyleSheet("""
            background-color: rgba(255, 255, 255, 200);
            padding: 20px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            color: #333;
            border: 2px solid #555;
        """)
        layout_preguntas.addWidget(self.label_resultado)
        
        preguntas = [
            "¿Es un bloque natural?",
            "¿Es transparente?",
            "¿Se puede craftear?",
            "¿Es resistente?",
            "¿Emite luz?",
            "¿Tiene gravedad?",
            "¿Se puede comer?",
            "¿Es un fluido?",
            "¿Es interactivo?",
            "¿Es creativo?"
        ]

        caracteristicas = [
            "natural", "transparente", "crafteable", "resistente", "luminoso",
            "gravedad", "comer", "fluido", "interactivo", "creativo"
        ]
        
        preguntas_layout = QGridLayout()
        for i, (pregunta, caracteristica) in enumerate(zip(preguntas, caracteristicas)):
            boton = QPushButton(pregunta)
            boton.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 12px;
                    border-radius: 10px;
                    font-size: 14px;
                    font-weight: bold;
                    border: 2px solid #45a049;
                }
                QPushButton:hover {
                    background-color: #45a049;
                    border: 2px solid #4CAF50;
                }
                QPushButton:pressed {
                    background-color: #3e8e41;
                    border: 2px solid #2e6d31;
                }
            """)
            boton.clicked.connect(lambda _, c=caracteristica, p=pregunta: self.hacer_pregunta(c, p))
            preguntas_layout.addWidget(boton, i // 2, i % 2)
        
        layout_preguntas.addLayout(preguntas_layout)
        
        self.label_preguntas = QLabel(f"Preguntas hechas: {self.juego.preguntas_hechas}")
        self.label_preguntas.setStyleSheet("""
            background-color: rgba(255, 255, 255, 200);
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
            border: 2px solid #555;
            margin-top: 10px;
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
                background-color: rgba(255, 255, 255, 150);
                border-radius: 12px;
                border: 2px solid #555;
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
        
        respuesta_texto = "Sí" if respuesta else "No"
        nueva_pregunta = QLabel(f"{pregunta} {respuesta_texto}")
        nueva_pregunta.setStyleSheet("""
            background-color: rgba(255, 255, 255, 180);
            padding: 12px;
            border-radius: 8px;
            font-size: 14px;
            color: #333;
            margin-bottom: 8px;
            border: 1px solid #999;
        """)
        self.historial_layout.addWidget(nueva_pregunta)
        self.historial_preguntas.append(nueva_pregunta)
        
        eliminados = self.juego.eliminar_bloques()
        for bloque in eliminados:
            for i in range(self.centralWidget().layout().itemAt(0).widget().layout().count()):
                boton = self.centralWidget().layout().itemAt(0).widget().layout().itemAt(i).widget()
                if isinstance(boton, QPushButton) and boton.toolTip() == bloque.nombre:
                    boton.setEnabled(False)
                    boton.setStyleSheet("""
                        background-color: rgba(100, 100, 100, 180);
                        border: 3px solid #555;
                        border-radius: 12px;
                    """)
                    break
        self.label_preguntas.setText(f"Preguntas hechas: {self.juego.preguntas_hechas}")

    def adivinar_bloque(self, nombre):
        if self.juego.adivinar(nombre):
            QMessageBox.information(self, "¡Felicidades!", f"¡Correcto! El bloque era {nombre}.\nLo adivinaste en {self.juego.preguntas_hechas} preguntas.", QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.critical(self, "¡Perdiste!", f"Incorrecto. El bloque no era {nombre}.\nEl bloque correcto era {self.juego.bloque_objetivo.nombre}.", QMessageBox.Ok)
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Configurar fuente global
    font = QFont("Minecraft", 10)
    app.setFont(font)
    
    ventana = VentanaJuego()
    ventana.show()
    sys.exit(app.exec_())