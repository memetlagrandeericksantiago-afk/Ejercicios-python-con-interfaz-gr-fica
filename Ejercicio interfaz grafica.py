import tkinter as tk
from tkinter import messagebox, ttk

class AppParque:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal - Ejercicios de Programación")
        self.root.geometry("400x500")
        
        tk.Label(root, text="SELECCIONE UN EJERCICIO", font=("Arial", 14, "bold")).pack(pady=20)
        
        opciones = [
            ("1. Aumento de Sueldos", self.ejercicio_1),
            ("2. Parque de Diversiones", self.ejercicio_2),
            ("3. Descuentos por Mes", self.ejercicio_3),
            ("4. Validar Menor a 10", self.ejercicio_4),
            ("5, 6. Rango e Historial", self.ejercicio_5_6),
            ("7. Suma de N números", self.ejercicio_7),
            ("8. Suma Acumulativa (hasta 0)", self.ejercicio_8),
            ("9. Límite 100", self.ejercicio_9),
            ("10. Pago de Trabajadores", self.ejercicio_10)
        ]

        for texto, comando in opciones:
            tk.Button(root, text=texto, command=comando, width=30).pack(pady=3)

    def limpiar_ventana(self):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.geometry("400x500")
        return nueva_ventana

    def ejercicio_1(self):
        v = self.limpiar_ventana()
        v.title("Aumento de Sueldos")
        lista_trabajadores = []

        def calcular_aumento(sueldo):
            if sueldo < 4000: return sueldo * 0.15
            elif sueldo <= 7000: return sueldo * 0.10
            else: return sueldo * 0.08

        def registrar():
            try:
                nom = e_nom.get()
                s_base = float(e_sueldo.get())
                aum = calcular_aumento(s_base)
                n_sueldo = s_base + aum
                lista_trabajadores.append(f"{nom}: {n_sueldo} soles")
                txt.delete('1.0', tk.END)
                txt.insert(tk.END, "\n".join(lista_trabajadores))
            except: messagebox.showerror("Error", "Datos inválidos")

        tk.Label(v, text="Nombre:").pack()
        e_nom = tk.Entry(v); e_nom.pack()
        tk.Label(v, text="Sueldo Básico:").pack()
        e_sueldo = tk.Entry(v); e_sueldo.pack()
        tk.Button(v, text="Procesar", command=registrar).pack(pady=5)
        txt = tk.Text(v, height=10, width=40); txt.pack()

    def ejercicio_2(self):
        v = self.limpiar_ventana()
        historial = []
        
        def procesar():
            try:
                nom = e_nom.get()
                edad = int(e_edad.get())
                juegos = int(e_juegos.get())
                total = juegos * 50
                desc = 0
                if edad < 10: desc = 0.25
                elif edad <= 17: desc = 0.10
                pagar = total * (1 - desc)
                historial.append(pagar)
                lbl_res.config(text=f"A pagar: {pagar} soles\nTotal Parque: {sum(historial)}")
            except: messagebox.showerror("Error", "Revisar datos")

        tk.Label(v, text="Nombre:").pack(); e_nom = tk.Entry(v); e_nom.pack()
        tk.Label(v, text="Edad:").pack(); e_edad = tk.Entry(v); e_edad.pack()
        tk.Label(v, text="Juegos:").pack(); e_juegos = tk.Entry(v); e_juegos.pack()
        tk.Button(v, text="Calcular", command=procesar).pack(pady=10)
        lbl_res = tk.Label(v, text="Esperando..."); lbl_res.pack()

    def ejercicio_3(self):
        v = self.limpiar_ventana()
        compras = []
        meses = {"octubre": 0.15, "diciembre": 0.20, "julio": 0.10}

        def registrar():
            m = e_mes.get().lower()
            if m not in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]:
                messagebox.showerror("Error", "Mes inválido")
                return
            try:
                imp = float(e_imp.get())
                total = imp * (1 - meses.get(m, 0))
                compras.append(total)
                lbl.config(text=f"Total: {total}\nTotal Día: {sum(compras)}")
            except: pass

        tk.Label(v, text="Mes:").pack(); e_mes = tk.Entry(v); e_mes.pack()
        tk.Label(v, text="Importe:").pack(); e_imp = tk.Entry(v); e_imp.pack()
        tk.Button(v, text="Registrar", command=registrar).pack(); lbl = tk.Label(v, text=""); lbl.pack()

    def ejercicio_4(self):
        v = self.limpiar_ventana()
        self.cont = 0
        def validar():
            try:
                self.cont += 1
                n = int(e.get())
                if n < 10: lbl.config(text=f"Correcto: {n}\nIntentos: {self.cont}")
                else: messagebox.showerror("Error", "No es menor a 10")
            except: pass
        e = tk.Entry(v); e.pack(); tk.Button(v, text="Validar", command=validar).pack(); lbl = tk.Label(v, text=""); lbl.pack()

    def ejercicio_5_6(self):
        v = self.limpiar_ventana()
        self.nums = []
        def chequear():
            try:
                n = int(e.get())
                self.nums.append(n)
                if 0 <= n <= 20:
                    err = len([x for x in self.nums if not (0 <= x <= 20)])
                    lbl.config(text=f"Válido: {n}\nErróneos: {err}\nHistorial: {self.nums}")
                else: messagebox.showwarning("Fuera", "Rango 0-20")
            except: pass
        e = tk.Entry(v); e.pack(); tk.Button(v, text="Probar", command=chequear).pack(); lbl = tk.Label(v, text=""); lbl.pack()

    def ejercicio_7(self):
        v = self.limpiar_ventana()
        def calcular():
            try:
                n = int(e.get())
                if n > 0:
                    seq = list(range(1, n + 1))
                    lbl.config(text=f"Suma: {sum(seq)}\nSecuencia: {seq}")
                else: messagebox.showwarning("!", "Debe ser positivo")
            except: pass
        e = tk.Entry(v); e.pack(); tk.Button(v, text="Sumar", command=calcular).pack(); lbl = tk.Label(v, text="", wraplength=300); lbl.pack()

    def ejercicio_8(self):
        v = self.limpiar_ventana()
        self.lista8 = []
        def agregar():
            try:
                n = int(e.get())
                if n == 0:
                    lbl.config(text=f"Lista: {self.lista8}\nCant: {len(self.lista8)}\nTotal: {sum(self.lista8)}")
                    e.config(state="disabled")
                else:
                    self.lista8.append(n)
                    lbl.config(text=f"Suma acumulada: {sum(self.lista8)}")
                    e.delete(0, tk.END)
            except: pass
        e = tk.Entry(v); e.pack(); tk.Button(v, text="Ingresar (0 para fin)", command=agregar).pack(); lbl = tk.Label(v, text=""); lbl.pack()

    def ejercicio_9(self):
        v = self.limpiar_ventana()
        self.lista9 = []
        def flujo():
            try:
                n = int(e.get())
                self.lista9.append(n)
                s = sum(self.lista9)
                if s > 100:
                    lbl.config(text=f"Final: {s}\nCant: {len(self.lista9)}\nNúmeros: {self.lista9}")
                    e.config(state="disabled")
                else:
                    lbl.config(text=f"Suma parcial: {s}")
                    e.delete(0, tk.END)
            except: pass
        e = tk.Entry(v); e.pack(); tk.Button(v, text="Ingresar hasta >100", command=flujo).pack(); lbl = tk.Label(v, text=""); lbl.pack()

    def ejercicio_10(self):
        v = self.limpiar_ventana()
        reporte = []
        def calcular():
            try:
                h_norm = int(e_hn.get()); p_hora = float(e_ph.get())
                h_ext = int(e_he.get()); hijos = int(e_hijos.get())
                p_norm = h_norm * p_hora
                p_ext = h_ext * (p_hora * 1.5)
                bono = hijos * 0.5 # Asumiendo 0.5 unidades según el texto
                total = p_norm + p_ext + bono
                res = f"{e_nom.get()}: Total {total}"
                reporte.append(res)
                txt.delete('1.0', tk.END); txt.insert(tk.END, "\n".join(reporte))
            except: pass

        tk.Label(v, text="Nombre:").pack(); e_nom = tk.Entry(v); e_nom.pack()
        tk.Label(v, text="Horas Normales:").pack(); e_hn = tk.Entry(v); e_hn.pack()
        tk.Label(v, text="Pago x Hora:").pack(); e_ph = tk.Entry(v); e_ph.pack()
        tk.Label(v, text="Horas Extras:").pack(); e_he = tk.Entry(v); e_he.pack()
        tk.Label(v, text="Hijos:").pack(); e_hijos = tk.Entry(v); e_hijos.pack()
        tk.Button(v, text="Calcular Pago", command=calcular).pack()
        txt = tk.Text(v, height=8, width=40); txt.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppParque(root)
    root.mainloop()