# Interfaz Gráfica para el Sistema Experto
# Optimizada para Raspberry Pi 3 usando Tkinter

import sys
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from datetime import datetime

# Importar módulos locales
from base_conocimientos import obtener_accion, reglas
from procesador_lenguaje import procesar_entrada


class SistemaExpertoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto - Mantenimiento CPU e Impresoras")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Historial de consultas
        self.historial = []
        
        # Crear interfaz
        self.crear_widgets()
        
    def crear_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="🖥 Sistema Experto - Mantenimiento de CPU e Impresoras 🖨",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        titulo.pack(pady=10)
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="Optimizado para Raspberry Pi 3",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        subtitulo.pack()
        
        # Frame de entrada
        entrada_frame = tk.LabelFrame(
            main_frame,
            text="Describa su problema",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        entrada_frame.pack(fill=tk.X, pady=10)
        
        # Campo de texto para entrada
        self.entrada_texto = tk.Entry(
            entrada_frame,
            font=("Arial", 12),
            width=60
        )
        self.entrada_texto.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
        self.entrada_texto.bind("<Return>", lambda e: self.procesar_consulta())
        
        # Botón de consulta
        btn_consultar = tk.Button(
            entrada_frame,
            text="🔍 Consultar",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.procesar_consulta,
            cursor="hand2"
        )
        btn_consultar.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Frame de problemas comunes
        problemas_frame = tk.LabelFrame(
            main_frame,
            text="Problemas Comunes (clic para seleccionar)",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        problemas_frame.pack(fill=tk.X, pady=5)
        
        # Botones de problemas comunes
        problemas_comunes = [
            ("CPU no enciende", "Mi computadora no enciende"),
            ("CPU lenta", "Mi CPU está muy lenta"),
            ("CPU sobrecalienta", "La computadora se sobrecalienta"),
            ("Impresora no enciende", "La impresora no enciende"),
            ("Atasco de papel", "Hay papel atascado en la impresora"),
            ("No imprime", "La impresora no imprime")
        ]
        
        btn_frame = tk.Frame(problemas_frame, bg="#f0f0f0")
        btn_frame.pack(pady=5)
        
        for i, (nombre, consulta) in enumerate(problemas_comunes):
            btn = tk.Button(
                btn_frame,
                text=nombre,
                font=("Arial", 9),
                bg="#2196F3",
                fg="white",
                command=lambda c=consulta: self.consulta_rapida(c),
                cursor="hand2"
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=3, sticky="ew")
        
        # Frame de resultados
        resultados_frame = tk.LabelFrame(
            main_frame,
            text="Solución",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        resultados_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Área de texto para resultados
        self.resultado_texto = scrolledtext.ScrolledText(
            resultados_frame,
            font=("Consolas", 11),
            wrap=tk.WORD,
            bg="#ffffff",
            fg="#333",
            height=12
        )
        self.resultado_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame inferior con botones
        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill=tk.X, pady=5)
        
        # Botón limpiar
        btn_limpiar = tk.Button(
            botones_frame,
            text="🗑 Limpiar",
            font=("Arial", 10),
            bg="#FF9800",
            fg="white",
            command=self.limpiar,
            cursor="hand2"
        )
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Botón historial
        btn_historial = tk.Button(
            botones_frame,
            text="📋 Ver Historial",
            font=("Arial", 10),
            bg="#9C27B0",
            fg="white",
            command=self.ver_historial,
            cursor="hand2"
        )
        btn_historial.pack(side=tk.LEFT, padx=5)
        
        # Botón ver reglas
        btn_reglas = tk.Button(
            botones_frame,
            text="📖 Ver Base de Conocimientos",
            font=("Arial", 10),
            bg="#607D8B",
            fg="white",
            command=self.ver_reglas,
            cursor="hand2"
        )
        btn_reglas.pack(side=tk.LEFT, padx=5)
        
        # Botón salir
        btn_salir = tk.Button(
            botones_frame,
            text="❌ Salir",
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            command=self.root.quit,
            cursor="hand2"
        )
        btn_salir.pack(side=tk.RIGHT, padx=5)
        
        # Barra de estado
        self.estado = tk.Label(
            self.root,
            text="Listo para recibir consultas",
            font=("Arial", 9),
            bg="#333",
            fg="white",
            anchor=tk.W
        )
        self.estado.pack(fill=tk.X, side=tk.BOTTOM)
    
    def procesar_consulta(self):
        entrada = self.entrada_texto.get().strip()
        
        if not entrada:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una descripción del problema.")
            return
        
        # Procesar entrada
        self.estado.config(text="Procesando consulta...")
        self.root.update()
        
        palabras_clave = procesar_entrada(entrada)
        solucion = obtener_accion(palabras_clave)
        
        # Guardar en historial
        self.historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "consulta": entrada,
            "palabras_clave": palabras_clave,
            "solucion": solucion
        })
        
        # Mostrar resultado
        self.resultado_texto.delete(1.0, tk.END)
        self.resultado_texto.insert(tk.END, f"📝 Consulta: {entrada}\n\n")
        self.resultado_texto.insert(tk.END, f"🔑 Palabras clave detectadas: {palabras_clave}\n\n")
        self.resultado_texto.insert(tk.END, "=" * 50 + "\n\n")
        self.resultado_texto.insert(tk.END, solucion)
        
        self.estado.config(text=f"Consulta procesada - Palabras clave: {palabras_clave}")
        self.entrada_texto.delete(0, tk.END)
    
    def consulta_rapida(self, consulta):
        self.entrada_texto.delete(0, tk.END)
        self.entrada_texto.insert(0, consulta)
        self.procesar_consulta()
    
    def limpiar(self):
        self.entrada_texto.delete(0, tk.END)
        self.resultado_texto.delete(1.0, tk.END)
        self.estado.config(text="Listo para recibir consultas")
    
    def ver_historial(self):
        if not self.historial:
            messagebox.showinfo("Historial", "No hay consultas en el historial.")
            return
        
        # Crear ventana de historial
        ventana_historial = tk.Toplevel(self.root)
        ventana_historial.title("Historial de Consultas")
        ventana_historial.geometry("600x400")
        
        texto_historial = scrolledtext.ScrolledText(
            ventana_historial,
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        texto_historial.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i, item in enumerate(self.historial, 1):
            texto_historial.insert(tk.END, f"--- Consulta #{i} ---\n")
            texto_historial.insert(tk.END, f"Fecha: {item['fecha']}\n")
            texto_historial.insert(tk.END, f"Consulta: {item['consulta']}\n")
            texto_historial.insert(tk.END, f"Palabras clave: {item['palabras_clave']}\n\n")
    
    def ver_reglas(self):
        # Crear ventana de reglas
        ventana_reglas = tk.Toplevel(self.root)
        ventana_reglas.title("Base de Conocimientos")
        ventana_reglas.geometry("700x500")
        
        texto_reglas = scrolledtext.ScrolledText(
            ventana_reglas,
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        texto_reglas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        texto_reglas.insert(tk.END, "BASE DE CONOCIMIENTOS DEL SISTEMA EXPERTO\n")
        texto_reglas.insert(tk.END, "=" * 50 + "\n\n")
        
        for i, regla in enumerate(reglas, 1):
            texto_reglas.insert(tk.END, f"REGLA #{i}\n")
            texto_reglas.insert(tk.END, f"Palabras clave: {regla['palabras_clave']}\n")
            texto_reglas.insert(tk.END, f"Condición: {regla['condicion']}\n")
            texto_reglas.insert(tk.END, "-" * 40 + "\n\n")


def main():
    root = tk.Tk()
    app = SistemaExpertoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()