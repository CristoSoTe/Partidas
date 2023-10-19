
	def mediaGuillermoCabrera():

		contadorRegistros=0
		sumaRegistro=0

		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()


		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Cabrera Castellano, Guillermo'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)
			print(datos)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Cabrera Castellano, Guillermo'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))

		except:

			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()
	
	def mediaTania():

		contadorRegistros=0
		sumaRegistro=0

		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='García Santana, Tania'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='García Santana, Tania'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla2")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()
	
	def mediaBegoña():

		contadorRegistros=0
		sumaRegistro=0

		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Santiago López, Begoña'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Santiago López, Begoña'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()
	
	def mediaSergioFarias():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Farías García, Sergio Felipe'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Farías García, Sergio Felipe'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaFranciscoSantana():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Santana Santana, Francisco'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Santana Santana, Francisco'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaJuanAntonioCabrera():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Cabrera Castellano, Juan Antonio'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Cabrera Castellano, Juan Antonio'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaLuisArencibia():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Arencibia Navarro, Luis Carmelo'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Arencibia Navarro, Luis Carmelo'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaSonsolesLlavata():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Llavata Conde, Sonsoles'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Llavata Conde, Sonsoles'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaLucía():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Cabello Suárez, Lucía'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Cabello Suárez, Lucía'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaManuelToledo():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Toledo Fontes, Francisco'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Toledo Fontes, Francisco'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaAntonio():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Navarro Luján, Antonio Jesús'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Navarro Luján, Antonio Jesús'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaMonicaRamirez():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Ramírez Quintana, Mónica Esther'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Ramírez Quintana, Mónica Esther'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaDiego():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Fernández Pereira, Diego'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Fernández Pereira, Diego'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaPedroPorteiro():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='González Porteiro, Pedro Manuel'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='González Porteiro, Pedro Manuel'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaAdil():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Arteaga Rodríguez, Adil'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Arteaga Rodríguez, Adil'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaCarloMujica():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Mujíca García, Carlos'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Mujíca García, Carlos'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaAbenchara():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Cabrera Santana, M. Abenchara'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Cabrera Santana, M. Abenchara'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaTitoGimeno():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Gimeno Suárez, Salvador'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Gimeno Suárez, Salvador'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla3")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()

	def mediaAuxiliar():

		contadorRegistros=0
		sumaRegistro=0


		miConexion = sqlite3.connect(combo_sala.get()+".db")
		miCursor = miConexion.cursor()
		
		miCursor.execute("SELECT * FROM datos WHERE TECNICO='Auxiliar'")

		try:
			for row in miCursor:
				contadorRegistros +=1
				sumaRegistro += row[4]
			tecnico = row[5]
			
			media=float(sumaRegistro/contadorRegistros)
			mediaRedondo=round(media, 2)
			mediaFinal=mediaRedondo
			datos= (tecnico, mediaFinal)

		except:

			pass

		try:
			miCursor.execute("DELETE FROM medias WHERE TECNICO='Auxiliar'")
			miCursor.execute("INSERT INTO medias VALUES (?,?)", (datos))


		except:
			#messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con la tabla")
			pass

		miConexion.commit()
		miCursor.close()
		miConexion.close()
	