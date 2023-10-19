#iMPORTAR BIBLIOTECAS
from tkinter import *
from tkinter import ttk
import sys
from tkcalendar import Calendar, DateEntry
import time
from datetime import datetime
from datetime import timedelta
#from dateutil.relativedelta import relativedelta
from tkinter import messagebox
import sqlite3
import os 
from tkinter import filedialog
import csv
from tkinter.filedialog import asksaveasfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


global fecha_seleccionada; global TotalPartidasHoy; global hora; global horaFinal

global fecha_seleccionada_a; global fecha_seleccionada_b; global miFechaDesde; global miFechaHasta; global archivos

final = 0; fecha_seleccionada = ""; fecha_seleccionada_español = ""; miFechaDesde = ""; miFechaDesde = ""; horaFinal = 0
fecha_seleccionada_a = ""; fecha_seleccionada_b = ""

root=Tk()
root.title("Control de Partidas")
root.geometry("1300x700")
root.config(bg="#B3E5FC")

miId=StringVar()
miDia=StringVar()
miFecha=StringVar()
miHora=StringVar()
miPartidas=StringVar()
miTecnicos=StringVar()
misTotalPartidas=IntVar()
miFechaDesde=StringVar()
miFechaHasta=StringVar()
miBBDD=StringVar()
fecha_seleccionada=StringVar()
miMediaPartidas=IntVar()
misTotalPartidasHoy=IntVar()

def lista_tecnicos():

	global listado_tecnicos
	try:
		def combo_input():

			if combo_sala.get() != "":
				conexion = sqlite3.connect(combo_sala.get()+".db")
				cursor = conexion.cursor()
				cursor.execute('SELECT nombre FROM tecnicos')
				result=[]
				for row in cursor.fetchall():
					result.append(row[0])
				return result
		listado_tecnicos = combo_input()
		combo_tecnicos['value'] = listado_tecnicos

	except:
		messagebox.showinfo(title="Información", message="No existe la tabla técnicos.")

def correoBallena():

	valor=messagebox.askquestion("Salir","¿Desea enviar los datos?")

	if valor=="yes":
		
		try:	

			# Iniciamos los parámetros del script
			remitente = 'cristosoto@grupoac.es'
			destinatarios = ['cristosote@gmail.com','jesusalonso@grupoac.es']
			asunto = 'Partidas diarias Bingo La Ballena'
			cuerpo = 'Buenos días, se adjunta archivo de partidas.'
			ruta_adjunto = (r'C:\Partidas\La_Ballena.db')
			nombre_adjunto = 'La_Ballena.db'

			# Creamos el objeto mensaje
			mensaje = MIMEMultipart()
			 
			# Establecemos los atributos del mensaje
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			 
			# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			 
			# Abrimos el archivo que vamos a adjuntar
			archivo_adjunto = open(ruta_adjunto, 'rb')
			 
			# Creamos un objeto MIME base
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			# Y le cargamos el archivo adjunto
			adjunto_MIME.set_payload((archivo_adjunto).read())
			# Codificamos el objeto en BASE64
			encoders.encode_base64(adjunto_MIME)
			# Agregamos una cabecera al objeto
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			# Y finalmente lo agregamos al mensaje
			mensaje.attach(adjunto_MIME)
			 
			# Creamos la conexión con el servidor
			sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
			 
			# Ciframos la conexión
			sesion_smtp.starttls()

			# Iniciamos sesión en el servidor
			sesion_smtp.login('cristosoto@grupoac.es','BOnhm132')

			# Convertimos el objeto mensaje a texto
			texto = mensaje.as_string()

			# Enviamos el mensaje
			sesion_smtp.sendmail(remitente, destinatarios, texto)

			# Cerramos la conexión
			sesion_smtp.quit()

			messagebox.showinfo(title="Información", message="Datos enviados.")

			root.destroy()

		except:
			messagebox.showinfo(title="Información", message="No se ha podido enviar los datos.")

	else:
		root.destroy()
		
def correoMercantil():

	valor=messagebox.askquestion("Salir","¿Desea enviar los datos?")

	if valor=="yes":

		try:

			# Iniciamos los parámetros del script
			remitente = 'cristosoto@grupoac.es'
			destinatarios = ['cristosote@gmail.com','jesusalonso@grupoac.es']
			asunto = 'Partidas diarias Bingo Mercantil'
			cuerpo = 'Buenos días, se adjunta archivo de partidas.'

			ruta_adjunto = (r'C:\Partidas\Mercantil.db')
			nombre_adjunto = 'Mercantil.db'

			# Creamos el objeto mensaje
			mensaje = MIMEMultipart()
			 
			# Establecemos los atributos del mensaje
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			 
			# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			 
			# Abrimos el archivo que vamos a adjuntar
			archivo_adjunto = open(ruta_adjunto, 'rb')
			 
			# Creamos un objeto MIME base
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			# Y le cargamos el archivo adjunto
			adjunto_MIME.set_payload((archivo_adjunto).read())
			# Codificamos el objeto en BASE64
			encoders.encode_base64(adjunto_MIME)
			# Agregamos una cabecera al objeto
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			# Y finalmente lo agregamos al mensaje
			mensaje.attach(adjunto_MIME)
			 
			# Creamos la conexión con el servidor
			sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
			 
			# Ciframos la conexión
			sesion_smtp.starttls()

			# Iniciamos sesión en el servidor
			sesion_smtp.login('cristosoto@grupoac.es','BOnhm132')

			# Convertimos el objeto mensaje a texto
			texto = mensaje.as_string()

			# Enviamos el mensaje
			sesion_smtp.sendmail(remitente, destinatarios, texto)

			# Cerramos la conexión
			sesion_smtp.quit()

			messagebox.showinfo(title="Información", message="Datos enviados.")

			root.destroy()

		except:
			messagebox.showinfo(title="Información", message="No se ha podido enviar los datos.")

	else:
		root.destroy()
	
def correoAuditorio():

	valor=messagebox.askquestion("Salir","¿Desea enviar los datos?")

	if valor=="yes":

		try:

			# Iniciamos los parámetros del script
			remitente = 'cristosoto@grupoac.es'
			destinatarios = ['cristosote@gmail.com','jesusalonso@grupoac.es']
			asunto = 'Partidas diarias Bingo Auditorio'
			cuerpo = 'Buenos días, se adjunta archivo de partidas.'

			ruta_adjunto = (r'C:\Partidas\Auditorio.db')
			nombre_adjunto = 'Auditorio.db'

			# Creamos el objeto mensaje
			mensaje = MIMEMultipart()
			 
			# Establecemos los atributos del mensaje
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			 
			# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			 
			# Abrimos el archivo que vamos a adjuntar
			archivo_adjunto = open(ruta_adjunto, 'rb')
			 
			# Creamos un objeto MIME base
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			# Y le cargamos el archivo adjunto
			adjunto_MIME.set_payload((archivo_adjunto).read())
			# Codificamos el objeto en BASE64
			encoders.encode_base64(adjunto_MIME)
			# Agregamos una cabecera al objeto
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			# Y finalmente lo agregamos al mensaje
			mensaje.attach(adjunto_MIME)
			 
			# Creamos la conexión con el servidor
			sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
			 
			# Ciframos la conexión
			sesion_smtp.starttls()

			# Iniciamos sesión en el servidor
			sesion_smtp.login('cristosoto@grupoac.es','BOnhm132')

			# Convertimos el objeto mensaje a texto
			texto = mensaje.as_string()

			# Enviamos el mensaje
			sesion_smtp.sendmail(remitente, destinatarios, texto)

			# Cerramos la conexión
			sesion_smtp.quit()

			messagebox.showinfo(title="Información", message="Datos enviados.")

			root.destroy()

		except:
			messagebox.showinfo(title="Información", message="No se ha podido enviar los datos.")

	else:
		root.destroy()

def correoImperial():

	valor=messagebox.askquestion("Salir","¿Desea enviar los datos?")

	if valor=="yes":

		try:

			# Iniciamos los parámetros del script
			remitente = 'cristosoto@grupoac.es'
			destinatarios = ['cristosote@gmail.com','jesusalonso@grupoac.es']
			asunto = 'Partidas diarias Bingo Imperial'
			cuerpo = 'Buenos días, se adjunta archivo de partidas.'

			ruta_adjunto = (r'C:\Partidas\Imperial.db')
			nombre_adjunto = 'Imperial.db'

			# Creamos el objeto mensaje
			mensaje = MIMEMultipart()
			 
			# Establecemos los atributos del mensaje
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			 
			# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			 
			# Abrimos el archivo que vamos a adjuntar
			archivo_adjunto = open(ruta_adjunto, 'rb')
			 
			# Creamos un objeto MIME base
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			# Y le cargamos el archivo adjunto
			adjunto_MIME.set_payload((archivo_adjunto).read())
			# Codificamos el objeto en BASE64
			encoders.encode_base64(adjunto_MIME)
			# Agregamos una cabecera al objeto
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			# Y finalmente lo agregamos al mensaje
			mensaje.attach(adjunto_MIME)
			 
			# Creamos la conexión con el servidor
			sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
			 
			# Ciframos la conexión
			sesion_smtp.starttls()

			# Iniciamos sesión en el servidor
			sesion_smtp.login('cristosoto@grupoac.es','BOnhm132')

			# Convertimos el objeto mensaje a texto
			texto = mensaje.as_string()

			# Enviamos el mensaje
			sesion_smtp.sendmail(remitente, destinatarios, texto)

			# Cerramos la conexión
			sesion_smtp.quit()

			messagebox.showinfo(title="Información", message="Datos enviados.")

			root.destroy()

		except:
			messagebox.showinfo(title="Información", message="No se ha podido enviar los datos.")

	else:
		root.destroy()

def correoMercurio():

	valor=messagebox.askquestion("Salir","¿Desea enviar los datos?")

	if valor=="yes":

		try:
		
			# Iniciamos los parámetros del script
			remitente = 'cristosoto@grupoac.es'
			destinatarios = ['cristosote@gmail.com','jesusalonso@grupoac.es']
			asunto = 'Partidas diarias Bingo Mercurio'
			cuerpo = 'Buenos días, se adjunta archivo de partidas.'

			ruta_adjunto = (r'C:\Partidas\Mercurio.db')
			nombre_adjunto = 'Mercurio.db'

			# Creamos el objeto mensaje
			mensaje = MIMEMultipart()
			 
			# Establecemos los atributos del mensaje
			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatarios)
			mensaje['Subject'] = asunto
			 
			# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			 
			# Abrimos el archivo que vamos a adjuntar
			archivo_adjunto = open(ruta_adjunto, 'rb')
			 
			# Creamos un objeto MIME base
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			# Y le cargamos el archivo adjunto
			adjunto_MIME.set_payload((archivo_adjunto).read())
			# Codificamos el objeto en BASE64
			encoders.encode_base64(adjunto_MIME)
			# Agregamos una cabecera al objeto
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			# Y finalmente lo agregamos al mensaje
			mensaje.attach(adjunto_MIME)
			 
			# Creamos la conexión con el servidor
			sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
			 
			# Ciframos la conexión
			sesion_smtp.starttls()

			# Iniciamos sesión en el servidor
			sesion_smtp.login('cristosoto@grupoac.es','BOnhm132')

			# Convertimos el objeto mensaje a texto
			texto = mensaje.as_string()

			# Enviamos el mensaje
			sesion_smtp.sendmail(remitente, destinatarios, texto)

			# Cerramos la conexión
			sesion_smtp.quit()

			messagebox.showinfo(title="Información", message="Datos enviados.")

			root.destroy()

		except:
			messagebox.showinfo(title="Información", message="No se ha podido enviar los datos.")

	else:
		root.destroy()

def conexionBBDD():

	global fecha_seleccionada
	if combo_sala.get()=="":
		messagebox.showwarning("ADVERTENCIA","Debe seleccionar antes una Sala")

	else:

		def obtenerFecha():

			global fecha_seleccionada
			
			import tkinter as tk 
			from tkinter import ttk 
			from tkcalendar import Calendar, DateEntry

			def cal_done(): 
				top.withdraw() 
				root.quit()

			root = tk.Tk() 
			root.withdraw()
			root.title("Selecione día a registrar") 

			top = tk.Toplevel(root)

			cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1") 
			cal.pack(fill="both", expand=True)

			ttk.Button(top, text="ok", command=cal_done).pack() 

			selected_date = None 
			root.mainloop() 
			return cal.selection_get()

		fecha_seleccionada = obtenerFecha()
		fecha_seleccionada_español = fecha_seleccionada.strftime("%d/%m/%Y")

		etiqueta_fecha.config(text=fecha_seleccionada_español)
		try:
			conexion = sqlite3.connect(combo_sala.get() + ".db")
			cursor = conexion.cursor()

			try:
				cursor.execute('''CREATE TABLE IF NOT EXISTS datos
					(ID INTEGER PRIMARY KEY AUTOINCREMENT,
					DIA VARCHAR(10) NOT NULL,
					FECHA TEXT NOT NULL,
					HORA TEXT NOT NULL,
					PARTIDAS SMALLINT(2) NOT NULL,
					TECNICO VARCHAR(50) NOT NULL,
					BINGO VARCHAR(50))''')

				cursor.execute('''CREATE TABLE IF NOT EXISTS medias
					(TECNICO VARCHAR(50) PRIMARY KEY ,
					MEDIAS REAL(20))
					''')

			except:
				messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear la BBDD")
				pass
				
			conexion.commit()
			cursor.close()
			conexion.close()

		except:
			pass

		botonCrear['state'] = NORMAL
		
		if combo_sala.get() == "La_Ballena":

			botonCerrar.place_forget()
			botonCorreoImperial.place_forget()
			botonCorreoAuditorio.place_forget()
			botonCorreoMercantil.place_forget()
			botonCorreoMercurio.place_forget()
			botonCorreoBallena.place(x=1110, y=600)
	 
		elif combo_sala.get() == "Imperial":

			botonCerrar.place_forget()
			botonCorreoBallena.place_forget()
			botonCorreoAuditorio.place_forget()
			botonCorreoMercantil.place_forget()
			botonCorreoMercurio.place_forget()
			botonCorreoImperial.place(x=1110, y=600)

		elif combo_sala.get() == "Auditorio":

			botonCerrar.place_forget()
			botonCorreoBallena.place_forget()
			botonCorreoImperial.place_forget()
			botonCorreoMercantil.place_forget()
			botonCorreoMercurio.place_forget()
			botonCorreoAuditorio.place(x=1110, y=600)

		elif combo_sala.get() == "Mercantil":

			botonCerrar.place_forget()
			botonCorreoBallena.place_forget()
			botonCorreoImperial.place_forget()
			botonCorreoAuditorio.place_forget()
			botonCorreoMercurio.place_forget()
			botonCorreoMercantil.place(x=1110, y=600)

		elif combo_sala.get() == "Mercurio":

			botonCerrar.place_forget()
			botonCorreoBallena.place_forget()
			botonCorreoImperial.place_forget()
			botonCorreoAuditorio.place_forget()
			botonCorreoMercantil.place_forget()
			botonCorreoMercurio.place(x=1110, y=600)

	lista_tecnicos()
	sumar()
	mostrar()

#----------------------obtener fecha para la BBDD---------------------------
	
def calculoMedias():
	
	def medias():
		try:
			miConexion = sqlite3.connect(combo_sala.get()+".db")
			miCursor = miConexion.cursor()

			miCursor.execute("SELECT DISTINCT TECNICO FROM datos")
			persona=miCursor.fetchall()
			
			for i in persona:

				contadorRegistros=0
				sumaRegistro=0
				
				miCursor.execute("SELECT * FROM datos WHERE TECNICO=?", (i))

				for row in miCursor:
					contadorRegistros +=1
					sumaRegistro += row[4]
				tecnico = row[5]
				
				media=float(sumaRegistro/contadorRegistros)
				mediaRedondo=round(media, 2)
				mediaFinal=mediaRedondo
				datos= (tecnico, mediaFinal)
				
				miCursor.execute("DELETE FROM medias WHERE TECNICO=?", (i))
				miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))
				
			miConexion.commit()
			miCursor.close()
			miConexion.close()

		except:
			pass

	
	def mostrarRanking():

		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		registros=treeRanking.get_children()

		for elemento in registros:
			treeRanking.delete(elemento)

		miCursor.execute("SELECT * FROM medias ORDER BY MEDIAS")
		for row in miCursor:

			treeRanking.insert("",0,text=row[0],values=(row[1]))

		miConexion.commit()
		miCursor.close()
		miConexion.close()
	
	medias()
	mostrarRanking()
	
def sumar():

	miTotalPartidas = 0
	miContadorPartidas = 0
	#miMediaPartidas = 0
	try:
		# Obtengo la lista de items e itero con ella. La variable item almacenará el id del item que actualmente estamos visitando.
		for item in tree.get_children():
		    # Obtengo el valor de la "celda" cuyo item es item y cuya columna es "#4"
		    # Como me devuelve el valor en forma de cadena, lo convierto al tipo que deseo. En este ejemplo va a ser un entero.
		    celda = int(tree.set(item, "#4"))

		    miContadorPartidas += 1
		    # Sumo el valor obtenido a la variable total
		    miTotalPartidas += celda

		misTotalPartidas.set(miTotalPartidas)

		media = float(miTotalPartidas/miContadorPartidas)
		miNumeroRedondeado = round(media, 2)
		miMediaPartidas.set(float(miNumeroRedondeado))

	except:
		pass

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿No ha introducido datos, está seguro que desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	combo_dia.set("")
	combo_hora.set("")
	combo_partidas.set("")
	combo_tecnicos.set("")
	#combo_sala.set("")
	misTotalPartidas.set("")
	misTotalPartidasHoy.set("")
	
def mensaje():
	acerca='''
	Aplicación Partidas
	Versión 1.0
	Cristo Soto
	cristosoto@grupoac.es
	'''

	messagebox.showinfo(title="Información", message=acerca)

#-------------------------------Métodos CRUD---------------------------------------

def crear():

	global fecha_seleccionada

	if combo_tecnicos.get() == "":
		messagebox.showinfo(title="Información", message="Debe seleccionar a un TÉCNICO")

	if combo_dia.get() == "":
		messagebox.showinfo(title="Información", message="Debe seleccionar a un DÍA de la semana")

	if combo_hora.get() == "":
		messagebox.showinfo(title="Información", message="Debe seleccionar a una HORA")

	if combo_partidas.get() == "":
		messagebox.showinfo(title="Información", message="Debe seleccionar a número de PARTIDAS")

	if combo_tecnicos.get() != "" and combo_dia.get() != "" and combo_hora.get() != "" and combo_partidas.get() != "":
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		try:
			datos=combo_dia.get(),fecha_seleccionada, combo_hora.get(), combo_partidas.get(), combo_tecnicos.get(), combo_sala.get()
			miCursor.execute("INSERT INTO datos VALUES(NULL,?,?,?,?,?,?)", (datos))
			miConexion.commit()
		except:
			messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
			pass

		if combo_hora.get() == '03:00':
			horaCadena = "2000-01-01 "+ combo_hora.get()
			ahora = datetime.strptime(horaCadena,'%Y-%m-%d %H:%M')# 
			dentro_de_1_hora = ahora + timedelta(hours = 1)
			dentro_de_1_hora_sin_segundos = dentro_de_1_hora.strftime('%H:%M')
			combo_hora.set(dentro_de_1_hora_sin_segundos)
			messagebox.showwarning("ADVERTENCIA","El próximo registro estará fuera de horario")
		
		else:
			horaCadena = "2000-01-01 "+ combo_hora.get()
			ahora = datetime.strptime(horaCadena,'%Y-%m-%d %H:%M')# 
			dentro_de_1_hora = ahora + timedelta(hours = 1)
			dentro_de_1_hora_sin_segundos = dentro_de_1_hora.strftime('%H:%M')
			combo_hora.set(dentro_de_1_hora_sin_segundos)
		
		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")
		
		mostrar()
		sumar()
		#sumar_dia()
		calculoMedias()

#-----------------------------Imprimir-----------------------------
def convertirTXT():

	file = open('Consulta.txt', 'r')
	read_file = file.readlines()
	file.close()

	a = []

	for i in range(len(read_file)):
		a.append(read_file[i].rstrip().split('  '))

	print(a)

#------------------------------Consultas--------------------------

def consultaPorFechas():

	global fecha_seleccionada_a; global fecha_seleccionada_b

	def aaaa():
	
		import tkinter as tk 
		from tkinter import ttk 
		from tkcalendar import Calendar, DateEntry

		def cal_done(): 
			top.withdraw() 
			root.quit()

		root = tk.Tk() 
		root.withdraw() 

		top = tk.Toplevel(root)
		top.title("Selección día inicial")


		cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1") 
		cal.pack(fill="both", expand=True)

		ttk.Button(top, text="ok", command=cal_done).pack() 

		selected_date = None 
		root.mainloop() 
		return cal.selection_get()

	fecha_seleccionada_a = aaaa()
	fecha_seleccionada_a_español = fecha_seleccionada_a.strftime("%d/%m/%Y")

	def bbbb():
	
		import tkinter as tk 
		from tkinter import ttk 
		from tkcalendar import Calendar, DateEntry

		def cal_done(): 
			top.withdraw() 
			root.quit()

		root = tk.Tk() 
		root.withdraw() 

		top = tk.Toplevel(root)
		top.title("Selección día Final")


		cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1") 
		cal.pack(fill="both", expand=True)

		ttk.Button(top, text="ok", command=cal_done).pack() 

		selected_date = None 
		root.mainloop() 
		return cal.selection_get()

	fecha_seleccionada_b = bbbb()
	fecha_seleccionada_b_español = fecha_seleccionada_b.strftime("%d/%m/%Y")

	miFechaDesde.set("Desde: " + str(fecha_seleccionada_a_español))
	miFechaHasta.set("Hasta: " + str(fecha_seleccionada_b_español))
	
def consultaGeneral(): 
	global hora
	import tkinter as tk 
	from tkinter import ttk 
	from tkcalendar import Calendar, DateEntry
	
	def cccc():

		global dia; global hora; global hora2; global partidas; global tecnicos; global sala; global fecha_seleccionada_a; global fecha_seleccionada_b


		def hecho(): 
				top.withdraw() 
				root.quit()

		root = tk.Tk()
		root.withdraw() 
		
		top = tk.Toplevel(root)
		top.title("Consulta")
		top.geometry("250x400")

		botonConsultaFecha = Button(top, text="   Fecha   ", font=("times",13,"bold"), command=consultaPorFechas)
		botonConsultaFecha.pack(pady=10)

		Label(top, text="TÉCNICO").pack(pady=7)

		combo_tecnicos = ttk.Combobox(top, state = "readonly", width=30)
		combo_tecnicos['value'] = listado_tecnicos
		combo_tecnicos.pack()

		Label(top, text="DIA").pack(pady=7)

		combo_dia = ttk.Combobox(top, state = "readonly", value = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
		combo_dia.pack()

		Label(top, text="HORA INICIAL").pack(pady=7)
		combo_hora = ttk.Combobox(top, state = "readonly", value = ["00:00","01:00","02:00","03:00","04:00","16:00","17:00",
			"18:00","19:00","20:00","21:00","22:00","23:00"])
		combo_hora.pack()
		

		Label(top, text="HORA FINAL").pack(pady=7)
		combo_hora2 = ttk.Combobox(top, state = "readonly", value = ["00:00","01:00","02:00","03:00","04:00","16:00","17:00",
			"18:00","19:00","20:00","21:00","22:00","23:00"])
		combo_hora2.pack()

		Label(top, text="PARTIDAS").pack(pady=7)
		combo_partidas = ttk.Combobox(top, state = "readonly", value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
		combo_partidas.pack()
		"""
		Label(top, text="SALA").pack(pady=7)

		combo_sala = ttk.Combobox(top, state = "readonly", value = ["La Ballena","Auditorio","Mercantil","Imperial","Mercurio"])
		combo_sala.pack()		
		"""
		botonAceptar=Button(top, text="  Aceptar  ", font=("times",13,"bold"), command=hecho)
		botonAceptar.pack(pady=15) 

		root.mainloop()
		
		misTotalPartidasHoy.set(0)
		
		dia = combo_dia.get()
		hora = combo_hora.get()
		hora2 = combo_hora2.get()
		partidas = combo_partidas.get()
		tecnicos = combo_tecnicos.get()
		sala = combo_sala.get()

	seleccion = cccc()

	if dia !="" and hora != "" and partidas != "" and tecnicos != "":# and sala != "" 1

		global fecha_seleccionada_a; global fecha_seleccionada_b; global archivos

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora<= '23:00') and (hora2>='00:00' and hora2<='03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND PARTIDAS=? AND TECNICO=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA" ,(hora, horaFinal, dia, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b, ))
				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND PARTIDAS=? AND TECNICO=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA" ,(hora, horaFinal, dia, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b, ))
				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND PARTIDAS=? AND TECNICO=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA" ,(hora, hora2, dia, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b, ))
				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
				Imprimir.close()

			
		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")

	if dia =="" and hora == "" and partidas == "" and tecnicos == "":# and sala == "" 2

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)

			miCursor.execute("SELECT * FROM datos WHERE FECHA BETWEEN ? AND ? ORDER BY FECHA" ,(fecha_seleccionada_a, fecha_seleccionada_b, ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")

	if dia !="" and hora != "" and partidas == "" and tecnicos == "":#  and sala != "" 3

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora<= '23:00') and (hora2>='00:00' and hora2<='03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, dia, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					 
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, dia, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					 
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND BINGO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, dia, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					 
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
		
	if dia !="" and hora != "" and partidas == "" and tecnicos != "":# and sala == "" 4

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora>='16:00' and hora<= '23:00') and (hora2>='00:00' and hora2<='03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, dia, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, dia, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND DIA=? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, dia, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()



		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")
		
	elif dia == "" and hora != "" and partidas != "" and tecnicos != "":# and sala != "" 5

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora<= '23:00') and (hora2>='00:00' and hora2<='03:00'):

				horaFinal = '23:00'				
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2				
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")

	elif dia == "" and hora == "" and partidas != "" and tecnicos != "":# and sala != "" 6
		
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE PARTIDAS = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")

	elif dia == "" and hora == "" and partidas == "" and tecnicos != "":# and sala != "" 7
		
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")
	
	elif hora == "" and dia != "" and partidas != "" and tecnicos != "":# and sala != "" 10

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND PARTIDAS = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, partidas, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")

	elif hora == "" and partidas == "" and dia != "" and tecnicos !="":# and sala != "" 11

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")

	elif hora == "" and partidas == "" and tecnicos =="" and dia!= "":# and sala !="" 12

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
	
	elif partidas == "" and dia =="" and hora != "" and tecnicos != "":# and sala!="" 15
		#global horaFinal

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		
		try:
			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00' 
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ?  AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))

				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
					
				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2 
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ?  AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))

				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
					
				Imprimir.close()

			else:
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ?  AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))

				for row in miCursor:

					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)
					
				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="green")
		
	elif partidas == "" and dia =="" and tecnicos =="" and hora !="":# and sala != "" 16

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
	
	elif tecnicos == "" and partidas != "" and dia !="" and hora != "":# and sala !="" 18

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, hora2, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")

	elif tecnicos == "" and partidas != "" and dia =="" and hora != "":# and sala !="" 19

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")

	elif tecnicos == "" and dia == "" and hora =="" and partidas !="":# and sala != "" 20

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE PARTIDAS = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(partidas, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass


		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
	

	elif dia!="" and hora=="" and partidas!="" and tecnicos=="":#sala=="" and 31

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND PARTIDAS = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, partidas, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")
	sumar()

def mostrar():

	global fecha_seleccionada
	try:
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()
		for elemento in registros:
			tree.delete(elemento)

		try:
			miCursor.execute("SELECT * FROM datos WHERE FECHA BETWEEN ? AND ?",(fecha_seleccionada, fecha_seleccionada))
			for row in miCursor:
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")

		sumar()
		calculoMedias()

	except:
		messagebox.showwarning("ADVERTENCIA","Debe seleccionar antes una Sala")

		pass

#------------------------------Tabla------------------------------------------------

tree=ttk.Treeview(root,height=15, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=380,y=230)
tree.column('#0',width=50)
tree.heading('#0', text="ID", anchor=CENTER)
tree.column('#1', width=100)
tree.heading('#1', text="DÍA", anchor=CENTER)
tree.column('#2', width=100)
tree.heading('#2', text="FECHA", anchor=CENTER)
tree.column('#3', width=50)
tree.heading('#3', text="HORA", anchor=CENTER)
tree.column('#4', width=70)
tree.heading('#4', text="PARTIDAS", anchor=CENTER)
tree.column('#5', width=200)
tree.heading('#5', text="TÉCNICO", anchor=CENTER)
tree.column('#6', width=80)
tree.heading('#6', text="SALA", anchor=CENTER)

treeRanking=ttk.Treeview(root,height=10, columns=('#0'))
treeRanking.place(x=70,y=320)
treeRanking.column('#0',width=200)
treeRanking.heading('#0', text="TÉCNICO", anchor=CENTER)
treeRanking.column('#1', width=50)
treeRanking.heading('#1', text="MEDIA", anchor=CENTER)

ejscrollbar= ttk.Scrollbar(root,orient=VERTICAL,command=tree.yview)
ejscrollbar.pack(side='right',fill='y')
tree.configure(yscrollcommand=ejscrollbar.set)

style = ttk.Style()
style.theme_use("clam")
style.map("Treeview")

def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	combo_dia.set(tree.item(item,"values")[0])
	combo_hora.set(tree.item(item,"values")[2])
	combo_partidas.set(tree.item(item,"values")[3])
	combo_tecnicos.set(tree.item(item,"values")[4])
	combo_sala.set(tree.item(item,"values")[5])

tree.bind("<Double-1>", seleccionarUsandoClick)

def actualizar():

	try:
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		try:
			datos=combo_dia.get(),fecha_seleccionada, combo_hora.get(), combo_partidas.get(), combo_tecnicos.get(), combo_sala.get()
			miCursor.execute("UPDATE datos SET DIA=?, FECHA=?, HORA=?, PARTIDAS=?, TECNICO=?, BINGO=? WHERE ID=" + miId.get(), (datos))
			miConexion.commit()
		except:
			messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
			pass

		mostrar()
		sumar()
		calculoMedias()

	except:
		#messagebox.showwarning("ADVERTENCIA","Debe seleccionar antes una Sala")
		pass

def borrar():

	try:
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		try:
			if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
				miCursor.execute("DELETE FROM datos WHERE ID=" + miId.get())
				miConexion.commit()
		except:
			messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
			pass
		limpiarCampos()
		mostrar()
		calculoMedias()

	except:
		#messagebox.showwarning("ADVERTENCIA","Debe seleccionar antes una Sala")
		pass

#-----------------------------Creando los Menus-----------------------------------

menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
#menubasedat.add_command(label="Guardar", command=limpiar)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

menuconsulta=Menu(menubar,tearoff=0)
menuconsulta.add_command(label="Consulta", command=consultaGeneral)
menubar.add_cascade(label="Consultas", menu=menuconsulta)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Acerca", menu=ayudamenu)

#-------------------------Creando etiquetas y cajas de texto-------------------

etiqueta_titulo = Label(root, text = "PARTIDAS POR HORA",bg="#B3E5FC", font=("times",25,"bold"))
etiqueta_titulo.place(x=150, y=10)

etiqueta_titulo = Label(root, text = "FECHA:",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_titulo.place(x=1000, y=20)

etiqueta_fecha = Label(root, text = fecha_seleccionada_español,bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_fecha.place(x=1100, y=20)

etiqueta_dia = Label(root, text = "DÍA: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_dia.place(x=445, y=130)

combo_dia = ttk.Combobox(root, state = "readonly", value = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
combo_dia.place(x=500, y=133)

etiqueta_hora = Label(root, text = "HORA: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_hora.place(x=800, y=70)

combo_hora = ttk.Combobox(root, state = "readonly", value =  ["00:00","01:00","02:00","03:00","04:00","16:00","17:00",
	"18:00","19:00","20:00","21:00","22:00","23:00"])
combo_hora.place(x=880, y=73)

etiqueta_partidas = Label(root, text = "PARTIDAS: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_partidas.place(x=760, y=130)		

combo_partidas = ttk.Combobox(root, state = "readonly", value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]) 
combo_partidas.place(x=880, y=133)

etiqueta_tecnicos = Label(root, text = "TÉCNICO: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_tecnicos.place(x=390, y=70)

combo_tecnicos = ttk.Combobox(root, state = "readonly", width=30)
combo_tecnicos.place(x=500, y=73)
#combo_tecnicos['value'] = combo_input()

etiqueta_sala = Label(root, text = "SALA DE BINGO: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_sala.place(x=50, y=100)

combo_sala = ttk.Combobox(root, state = "readonly", value = ["La_Ballena","Auditorio","Mercantil","Imperial","Mercurio"])
combo_sala.place(x=220, y=103)

#etiqueta_total_hoy = Label(root, text = "TOTAL HOY: ",bg="#B3E5FC", font=("times",15,"bold"))
#etiqueta_total_hoy.place(x=613, y= 565)

#entrada_total_hoy = ttk.Entry(root,justify= RIGHT,textvariable=misTotalPartidasHoy, state="readonly")
#entrada_total_hoy.place(x=750, y=568)

etiqueta_total = Label(root, text = "TOTAL: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_total.place(x=660, y= 580)

entrada_total = ttk.Entry(root,justify= RIGHT,textvariable=misTotalPartidas, state="readonly")
entrada_total.place(x=750, y=583)

etiqueta_media = Label(root, text = "MEDIA POR HORA: ",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_media.place(x=553, y= 625)

entrada_media = ttk.Entry(root,justify= RIGHT,textvariable=miMediaPartidas, state="readonly")
entrada_media.place(x=750, y=628)

etiqueta_filtro = Label(root, text = "FLITROS",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_filtro.place(x=1120, y=270)

etiqueta_aplicados = Label(root, text = "APLICADOS:",bg="#B3E5FC", font=("times",15,"bold"))
etiqueta_aplicados.place(x=1100, y=300)

etiqueta_dia_filtro = Label(root, text = "DÍA",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_dia_filtro.place(x=1145, y=335)

etiqueta_hora_filtro = Label(root, text = "HORA INICIAL:",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_hora_filtro.place(x=1100, y=365)

etiqueta_hora2_filtro = Label(root, text = "HORA FINAL:",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_hora2_filtro.place(x=1108, y=395)

etiqueta_partidas_filtro = Label(root, text = "PARTIDAS",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_partidas_filtro.place(x=1117, y=425)

etiqueta_tecnico_filtro = Label(root, text = "TÉCNICO",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_tecnico_filtro.place(x=1122, y=455)

#etiqueta_sala_filtro = Label(root, text = "SALA",bg="#B3E5FC", font=("times",12,"bold"))
#etiqueta_sala_filtro.place(x=1138, y=455)

etiqueta_fecha_filtro_desde = Label(root, textvariable= miFechaDesde,bg="#B3E5FC",fore ="green", font=("times",12,"bold"))
etiqueta_fecha_filtro_desde.place(x=1100, y=500)

etiqueta_fecha_filtro_hasta = Label(root, textvariable= miFechaHasta,bg="#B3E5FC",fore ="green", font=("times",12,"bold"))
etiqueta_fecha_filtro_hasta.place(x=1100, y=520)

etiqueta_medias_individual = Label(root, text = "MEDIAS",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_medias_individual.place(x=165, y=260)

etiqueta_tecnicos_individual = Label(root, text = "INDIVIDUALES",bg="#B3E5FC", font=("times",12,"bold"))
etiqueta_tecnicos_individual.place(x=138, y=280)

combo_hora.set("16:00")
combo_partidas.set(12)

#-----------------------------Creando botones---------------------------------

botonCrear=Button(root, text="Grabar", font=("times",15,"bold"),bg="Green", command=crear, padx=15)
botonCrear.place(x=770, y=170)
botonCrear['state'] = DISABLED
botonActualizar=Button(root, text="Modificar", font=("times",15,"bold"), command=actualizar)
botonActualizar.place(x=400, y=600)
botonMostrar=Button(root, text=" Mostrar ", font=("times",15,"bold"), command=mostrar)
botonMostrar.place(x=550, y=170)
botonBorrar=Button(root, text=" Eliminar ", font=("times",15,"bold"),bg="red", command=borrar)
botonBorrar.place(x=920, y=600)
botonCerrar=Button(root, text="Salir", font=("times",15,"bold"), command=salirAplicacion, padx=25)
botonCerrar.place(x=1110, y=600)
botonConexionBBDD=Button(root, text="Conectar BBDD", command=conexionBBDD, font=("times",12,"bold"))
botonConexionBBDD.place(x=228, y=130)

botonCorreoBallena=Button(root, text="Salir", command=correoBallena, font=("times",15,"bold"), padx=25)
botonCorreoImperial=Button(root, text="Salir", command=correoImperial, font=("times",15,"bold"), padx=25)
botonCorreoAuditorio=Button(root, text="Salir", command=correoAuditorio, font=("times",15,"bold"), padx=25)
botonCorreoMercantil=Button(root, text="Salir", command=correoMercantil, font=("times",15,"bold"), padx=25)
botonCorreoMercurio=Button(root, text="Salir", command=correoMercurio, font=("times",15,"bold"), padx=25)

root.config(menu=menubar)

root.mainloop()

"""
def sumar_dia():

	global fecha_seleccionada; global TotalPartidasHoy

	sumaRegistro=0
	
	miConexion = sqlite3.connect(combo_sala.get()+".db")
	miCursor = miConexion.cursor()
	
	miCursor.execute("SELECT * FROM datos WHERE FECHA BETWEEN ? AND ?" ,( fecha_seleccionada, fecha_seleccionada, ))

	try:
		for row in miCursor:
			
			sumaRegistro += row[4]
		
		misTotalPartidasHoy.set(sumaRegistro)
		
	except:

		pass

	miConexion.commit()
	miCursor.close()
	miConexion.close()

	
	elif dia != "" and hora == "" and partidas != "" and tecnicos == "":# and sala == "" 8
		
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND PARTIDAS = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, partidas, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")
		
	elif dia == "" and hora == "" and partidas == "" and tecnicos == "":# and sala != "" 9
		
		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
		
	
	elif hora == "" and partidas == "" and tecnicos =="" and dia != "":# and sala =="" 13

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")
		
	elif partidas == "" and dia != "" and hora != "" and tecnicos != "":# and sala != "" 14

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora >= '16:00' and hora <= '23:00') and (hora2 >= '00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND TECNICO = ? AND BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, hora2, tecnicos, sala, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		
	
	elif partidas == "" and dia =="" and hora == "" and tecnicos =="":# and sala != "" 17

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
			
	
	elif tecnicos == "" and dia =="" and hora =="" and partidas == "":# and sala != "" 21

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE BINGO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(sala, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="green")
		
	elif tecnicos != "" and dia == "" and hora !="" and partidas =="":# and sala == "" 22

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()				

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif tecnicos != "" and dia != "" and hora =="" and partidas =="":# and sala == "" 23

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE DIA=? AND TECNICO=? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia,tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif tecnicos != "" and dia !="" and hora !="" and partidas !="" :#sala == "" and 24

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA BETWEEN ? AND ? AND HORA = ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA BETWEEN ? AND ? AND HORA = ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA BETWEEN ? AND ? AND HORA = ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, hora2, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif dia =="" and hora != "" and partidas !="" and tecnicos != "" :#sala == "" and 25

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:

				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif dia =="" and hora =="" and partidas != "" and tecnicos != "" :#sala == "" and 26

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE PARTIDAS = ? AND TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(partidas, tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif dia =="" and hora =="" and partidas != "" and tecnicos == "" :#sala == "" and 27

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE PARTIDAS = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(partidas, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="green")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")

	elif dia =="" and hora !="" and partidas == "" and tecnicos == "" :#sala == "" and 28

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, horaFinal, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(hora, hora2, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")
		
	elif dia=="" and hora=="" and partidas=="" and tecnicos!="":#sala=="" and 29

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:

			Imprimir=open("Consulta.csv", "w")
			print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
			miCursor.execute("SELECT * FROM datos WHERE TECNICO = ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(tecnicos, fecha_seleccionada_a, fecha_seleccionada_b ))
			
			for row in miCursor:
				
				tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
				print(row, file=Imprimir)

			Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="black")
		etiqueta_hora_filtro.config(text="HORA INICIAL: ",fore ="black")
		etiqueta_hora_filtro.config(text="HORA FINAL: ",fore ="black")
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="green")
		#etiqueta_sala_filtro.config(fore ="black")

	elif dia !="" and hora !="" and partidas == "" and tecnicos == "" :#sala == "" and 30

		miConexion=sqlite3.connect(combo_sala.get()+".db")
		miCursor=miConexion.cursor()
		registros=tree.get_children()

		for elemento in registros:
			tree.delete(elemento)

		try:
			if (hora>='16:00' and hora <='23:00') and (hora2>='00:00' and hora2 <= '03:00'):

				horaFinal = '23:00'
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

				hora = '00:00'
				horaFinal = hora2
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, horaFinal, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

			else:
				Imprimir=open("Consulta.csv", "w")
				print(["","DIA", "FECHA", "HORA","PARTIDAS","TECNICO","SALA"], file=Imprimir)
				miCursor.execute("SELECT * FROM datos WHERE DIA = ? AND HORA BETWEEN ? AND ? AND FECHA BETWEEN ? AND ? ORDER BY FECHA",(dia, hora, hora2, fecha_seleccionada_a, fecha_seleccionada_b ))
				
				for row in miCursor:
					
					tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					print(row, file=Imprimir)

				Imprimir.close()

		except:
			pass

		etiqueta_dia_filtro.config(fore ="green")
		etiqueta_hora_filtro.config(text="HORA INICIAL: "+ str(hora), fore ="green")
		etiqueta_hora_filtro.place(x=1077, y=365)
		etiqueta_hora2_filtro.config(text="HORA FINAL: "+ str(hora2), fore ="green")
		etiqueta_hora2_filtro.place(x=1084, y=395)
		etiqueta_partidas_filtro.config(fore ="black")
		etiqueta_tecnico_filtro.config(fore ="black")
		#etiqueta_sala_filtro.config(fore ="black")		
		"""