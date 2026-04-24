import customtkinter as ctk
from tkinter import messagebox
import csv # Uso esta librería para manejar los datos de mi archivo CSV

# Configuro el estilo visual de mi aplicación
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MiAplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Defino el tamaño de mi ventana y el título
        self.title("Sistema de Análisis de Estudiantes")
        self.geometry("950x600")

        # Primero mando llamar a mi pantalla de login
        self.mostrar_login()

    def mostrar_login(self):
        # Yo creo este frame para que sea lo primero que vea el usuario
        self.frame_acceso = ctk.CTkFrame(self)
        self.frame_acceso.pack(pady=60, padx=60, fill="both", expand=True)

        self.lbl_bienvenido = ctk.CTkLabel(self.frame_acceso, text="Control de Usuarios", font=("Arial", 22, "bold"))
        self.lbl_bienvenido.pack(pady=20)

        # Entradas para que yo pueda capturar los datos
        self.user_input = ctk.CTkEntry(self.frame_acceso, placeholder_text="Usuario", width=200)
        self.user_input.pack(pady=10)

        self.pass_input = ctk.CTkEntry(self.frame_acceso, placeholder_text="Contraseña", show="*", width=200)
        self.pass_input.pack(pady=10)

        self.btn_entrar = ctk.CTkButton(self.frame_acceso, text="Iniciar Sesión", command=self.validar_desde_archivo)
        self.btn_entrar.pack(pady=20)

    def validar_desde_archivo(self):
        # Yo tomo los datos que el usuario escribió
        u = self.user_input.get()
        p = self.pass_input.get()

        acceso = False
        try:
            # Aquí yo abro el archivo .txt para leer línea por línea
            with open("usuarios.txt", "r") as f:
                for linea in f:
                    # Separo por coma y valido que no haya espacios extra
                    datos = linea.strip().split(",")
                    if len(datos) == 2:
                        if datos[0] == u and datos[1] == p:
                            acceso = True
                            break

            if acceso:
                # Si los datos son correctos, destruyo el login y abro el sistema
                self.frame_acceso.destroy()
                self.crear_interfaz_principal()
            else:
                messagebox.showerror("Error", "Usuario o clave no coinciden")
        except:
            messagebox.showerror("Error", "No encontré mi archivo 'usuarios.txt'")

    def crear_interfaz_principal(self):
        # Yo uso un frame contenedor para organizar mis dos secciones
        self.contenedor = ctk.CTkFrame(self)
        self.contenedor.pack(fill="both", expand=True)

        # Sección 1: El menú lateral con mis 10 consultas
        self.menu_botones = ctk.CTkScrollableFrame(self.contenedor, width=280, label_text="Panel de Consultas")
        self.menu_botones.pack(side="left", fill="y", padx=10, pady=10)

        # Sección 2: El "otro frame" donde se muestran los resultados
        self.frame_resultados = ctk.CTkFrame(self.contenedor)
        self.frame_resultados.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.titulo_visor = ctk.CTkLabel(self.frame_resultados, text="Visor de Datos", font=("Arial", 16, "bold"))
        self.titulo_visor.pack(pady=10)

        # Yo uso un Textbox para que la información se vea clara y profesional
        self.caja_datos = ctk.CTkTextbox(self.frame_resultados, font=("Consolas", 12))
        self.caja_datos.pack(fill="both", expand=True, padx=15, pady=15)

        # Defino mi lista de 10 consultas complejas sobre el CSV
        mis_consultas = [
            "Promedio General Matemáticas", "Mujeres con curso completo",
            "Hombres con curso completo", "Promedio Math por Nivel Padres",
            "Top 5 Puntajes Reading", "Promedio Reading por Género",
            "Alumnos con Almuerzo Standard", "Puntajes 100 en Writing",
            "Promedio Writing por Etnia", "Conteo total por Etnia"
        ]

        # Yo genero los botones automáticamente para ahorrar líneas de código
        for i, texto in enumerate(mis_consultas):
            btn = ctk.CTkButton(self.menu_botones, text=texto, 
                               command=lambda n=i+1: self.ejecutar_analisis(n))
            btn.pack(pady=5, fill="x")

    def ejecutar_analisis(self, id_con):
        # Yo abro mi base de datos para cada consulta
        try:
            with open('StudentsPerformance.csv', mode='r', encoding='utf-8') as file:
                lector = csv.DictReader(file)
                lista = list(lector)

            res = ""
            # Yo programé estas 10 lógicas para filtrar y calcular los datos
            if id_con == 1:
                suma = sum(int(f['math score']) for f in lista)
                res = f"REPORTE 01:\nEl promedio de matemáticas es: {suma/len(lista):.2f}"
            elif id_con == 2:
                c = sum(1 for f in lista if f['gender'] == 'female' and f['test preparation course'] == 'completed')
                res = f"REPORTE 02:\n{c} mujeres completaron su preparación."
            elif id_con == 3:
                c = sum(1 for f in lista if f['gender'] == 'male' and f['test preparation course'] == 'completed')
                res = f"REPORTE 03:\n{c} hombres completaron su preparación."
            elif id_con == 4:
                res = "REPORTE 04 (Promedio Math / Educación Padres):\n"
                grupos = {}
                for f in lista:
                    p = f['parental level of education']
                    s = int(f['math score'])
                    if p not in grupos: grupos[p] = []
                    grupos[p].append(s)
                for k, v in grupos.items():
                    res += f"- {k}: {sum(v)/len(v):.2f}\n"
            elif id_con == 5:
                top = sorted(lista, key=lambda x: int(x['reading score']), reverse=True)[:5]
                res = "REPORTE 05 (TOP 5 READING):\n"
                for p in top:
                    res += f"- Género: {p['gender']} | Score: {p['reading score']}\n"
            elif id_con == 6:
                m = [int(f['reading score']) for f in lista if f['gender'] == 'male']
                f = [int(f['reading score']) for f in lista if f['gender'] == 'female']
                res = f"REPORTE 06:\nPromedio Hombres: {sum(m)/len(m):.2f}\nPromedio Mujeres: {sum(f)/len(f):.2f}"
            elif id_con == 7:
                c = sum(1 for f in lista if f['lunch'] == 'standard')
                res = f"REPORTE 07:\n{c} alumnos tienen almuerzo estándar."
            elif id_con == 8:
                c = sum(1 for f in lista if f['writing score'] == '100')
                res = f"REPORTE 08:\nEncontré {c} alumnos con calificación perfecta (100)."
            elif id_con == 9:
                res = "REPORTE 09 (Writing por Etnia):\n"
                etn = {}
                for f in lista:
                    g = f['race/ethnicity']
                    sc = int(f['writing score'])
                    if g not in etn: etn[g] = []
                    etn[g].append(sc)
                for k, v in etn.items():
                    res += f"- {k}: {sum(v)/len(v):.2f}\n"
            elif id_con == 10:
                res = "REPORTE 10 (Total por Etnia):\n"
                tot = {}
                for f in lista:
                    g = f['race/ethnicity']
                    tot[g] = tot.get(g, 0) + 1
                for k, v in tot.items():
                    res += f"- {k}: {v} alumnos\n"

            # Yo limpio la caja de texto y pongo el nuevo resultado
            self.caja_datos.delete("0.0", "end")
            self.caja_datos.insert("0.0", res)

        except Exception as err:
            messagebox.showerror("Error de Datos", f"Yo no pude procesar el CSV: {err}")

if __name__ == "__main__":
    # Yo arranco mi programa aquí
    app = MiAplicacion()
    app.mainloop()
