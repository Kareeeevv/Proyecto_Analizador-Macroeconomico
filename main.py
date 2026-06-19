import tkinter as tk
from tkinter import ttk
from dinero import Dinero
from juridico import marco_legal_dinero, procesar_pago
from modos_produccion import simular_evolucion
from comercio import BalanzaComercial
from constants import *

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulador Histórico y Económico de México")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.tab_dinero()
        self.tab_juridico()
        self.tab_historia()
        self.tab_comercio()

    def tab_dinero(self) -> None: #{
        def showResults() -> None:
            if startY_select.get() > endY_select.get():
                startY_select.current((int(endY_select.get()) - 1990) - 1)
            
            if endY_select.get() < startY_select.get():
                endY_select.current((int(startY_select.get()) - 1990) + 1)

            start_year.set(startY_select.get())
            end_year.set(endY_select.get())

            perdida.set(str(Dinero.inflacion_acumulada(start_year.get(), end_year.get())))
            valor_real = peso.deposito_de_valor(Dinero.historial_inflacion(start_year.get(), end_year.get()), [start_year.get(), end_year.get()])
            texto = (
                f"\n\nAnálisis de Billete de ${peso.valor_nominal}:\n\n"
                f"1. Inflación acumulada: {float(perdida.get()):.2f}% (tasa promedio: {Dinero.inflacion_promedio(start_year.get(), end_year.get()):.2f}%)\n"
                f"2. Valor real después del periodo establecido (depósito de valor): ${valor_real:.2f}\n"
            )
            tk.Label(main, name="results_label", text=texto, font=("Arial", 12), justify="left").grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        
        start_year = tk.StringVar(value='2015')
        end_year = tk.StringVar(value='2025')

        main = ttk.Frame(self.notebook)
        main.columnconfigure(0, weight=1)
        main.columnconfigure(3, weight=1)
        main.rowconfigure(1, weight=1)
        self.notebook.add(main, text="Dinero e Inflación")

        peso = Dinero(100.0, "billete", "Banxico")
        perdida = tk.StringVar(value=str(Dinero.inflacion_acumulada(start_year.get(), end_year.get())))
        valor_real = peso.deposito_de_valor(Dinero.historial_inflacion(start_year.get(), end_year.get()), [start_year.get(), end_year.get()])

        texto = (
            f"\n\nAnálisis de Billete de ${peso.valor_nominal}:\n\n"
            f"1. Inflación acumulada: {float(perdida.get()):.2f}% (tasa promedio: {Dinero.inflacion_promedio(start_year.get(), end_year.get()):.2f}%)\n"
            f"2. Valor real después del periodo establecido (depósito de valor): ${valor_real:.2f}\n"
        )
        tk.Label(main, name="results_label", text=texto, font=("Arial", 12), justify="left").grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        tk.Frame(main, name="startY_frame", relief="raised", borderwidth=5, width=200, height=100)\
            .grid(row=1, column=1, pady=15, padx=20)
        startY_select = ttk.Combobox(main.children['startY_frame'], state='readonly', font=('Arial', 13, 'bold'))
        startY_select['values'] = list(i for i in range(1990, 2026))
        startY_select.current(0)
        startY_select.pack(padx=10, pady=30)

        tk.Frame(main, name="endY_frame", relief="sunken", borderwidth=5, width=200, height=100)\
            .grid(row=1, column=2, pady=15, padx=20)
        endY_select = ttk.Combobox(main.children['endY_frame'], state='readonly', font=('Arial', 13, 'bold'))
        endY_select['values'] = list(i for i in range(1990, 2026))
        endY_select.current(0)
        endY_select.pack(padx=10, pady=30)

        tk.Button(main, text="Calcular", relief="ridge", borderwidth=5, font=('Cambria', 12, 'bold'),
                  command=showResults)\
            .grid(row=2, column=1, columnspan=2, padx=10)
    #}

    def tab_juridico(self) -> None:
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Marco Jurídico")

        marco = marco_legal_dinero()
        for ley, desc in marco.items():
            tk.Label(frame, text=f"{ley}:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(frame, text=desc, font=("Arial", 10)).pack(anchor="w", padx=40)

        ttk.Separator(frame, orient='horizontal').pack(fill='x', pady=20)

        # Demostración del decorador
        try:
            resultado_exito = procesar_pago(500.0)
            tk.Label(frame, text=f"Prueba Denominación Válida ($500): {resultado_exito}", fg="green").pack()
            procesar_pago(33.0) # Esto lanzará la excepción
        except ValueError as e:
            tk.Label(frame, text=f"Prueba Denominación Inválida ($33): {e}", fg="red").pack()

    def tab_historia(self) -> None:
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Modos de Producción")

        tk.Label(frame, text="Evolución Histórica y el Rol del Dinero", font=("Arial", 14, "bold")).pack(pady=10)
        
        evolucion = simular_evolucion()
        for etapa in evolucion:
            tk.Label(frame, text=etapa, font=("Arial", 11), justify="left").pack(anchor="w", padx=20, pady=5)

    def tab_comercio(self) -> None:
        tratado = tk.StringVar(value="T-MEC")
        mod = tk.StringVar(value="Exp")

        main = ttk.Frame(self.notebook)
        main.columnconfigure(0, weight=1)
        main.columnconfigure(3, weight=1)

        self.notebook.add(main, text="Comercio y Tratados")

        balanza = BalanzaComercial()
        
        tk.Label(main, text="Simulación de Balanza Comercial", font=("Arial", 16, "bold")).grid(row=0, columnspan=4, pady=10)

        tk.Frame(main, name="mod_frame", relief="ridge", borderwidth=3, height=100, width=200)\
            .grid(row=1, column=1, padx=10)
        mod_select = ttk.Combobox(main.children['mod_frame'], state='readonly')
        mod_select['values'] = ('Exportación', 'Importación')
        mod_select.current(0)
        mod_select.pack(padx=5, pady=5)
        mod_select.bind("<<ComboboxSelected>>", lambda e: mod.set(mod_select.get()[:3]))
        
        tk.Frame(main, name="tratado_frame", relief="groove", borderwidth=3, height=100, width=200)\
            .grid(row=1, column=2, padx=10)
        tratado_select = ttk.Combobox(main.children['tratado_frame'], state='readonly')
        tratado_select['values'] = tuple(TRATADOS.keys())
        tratado_select.current(0)
        tratado_select.pack(padx=5, pady=5)
        tratado_select.bind("<<ComboboxSelected>>", lambda e: tratado.set(tratado_select.get()))

        tk.Button(main, text="Generar Gráfica", command=lambda: balanza.simular(TRATADOS[tratado.get()], mod.get(), main)).grid(row=2, column=1, columnspan=2, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()