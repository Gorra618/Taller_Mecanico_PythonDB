import os, mysql.connector, time

os.system("cls" if os.name == "nt" else "clear")


class TallerDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="NikoStasyszyn",
                database="Taller_Mecanico",
            )

            if self.connection.is_connected():
                print("> Conexion exitosa")
                self.cursor = self.connection.cursor()
        except Exception as ex:
            print("> Error de conexion:", ex)
            exit()

    # Limpiar la pantalla
    def clean(self):
        os.system("cls" if os.name == "nt" else "clear")

    # -----MENUS-----
    def menu(self):
        self.clean()
        print("1. Clientes")
        print("2. Vehiculos")
        print("3. Mecanicos")
        print("4. Ficha Tecnica")
        print("5. Facturacion")
        print("6. Salir")

    # Clientes
    def menu_clientes(self):
        print("1. Ver clientes")
        print("2. Ingresar clientes")
        print("3. Ver cliente especifico")
        print("4. Eliminar cliente")
        print("5. Volver ")

    # Vehiculos
    def menu_vehiculos(self):
        print("1. Ver vehiculos")
        print("2. Ingresar vehiculo")
        print("3. Ver vehiculo especifico")
        print("4. Eliminar vehiculo")
        print("5. Volver")

    # Mecanicos
    def menu_mecanicos(self):
        print("1. Ver mecanicos")
        print("2. Ingresar mecanico")
        print("3. Ver mecanico especifico")
        print("4. Eliminar mecanico")
        print("5. Volver")

    # Ficha Tecnica
    def menu_ficha_tecnica(self):
        print("1. Crear Ficha Tecnica")
        print("2. Consultar Ficha Tecnica")
        print("3. Modificar Ficha Tecnica")
        print("4. Volver")

    # Facturacion
    def menu_facturacion(self):
        print("1. Crear Facturacion")
        print("2. Anular Facturacion")
        print("3. Consultar Facturacion")
        print("4. Volver")

    # -----Funciones-----
    # Clientes
    def Clientes(self):
        query = "SELECT * FROM Clientes"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)
        option = input("Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

    def Crear_Cliente(self):
        insert_query = "INSERT INTO Clientes (DNI, Nombre, Apellido, Direccion, Telefono) VALUES (%s, %s, %s, %s, %s)"
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        direccion = input("Ingrese Direccion: ")
        telefono = input("Ingrese Telefono: ")

        data = (dni, nombre, apellido, direccion, telefono)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        print("> Cliente creado exitosamente.")
        print("> Volviendo al menu principal...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

    def Cliente_especifico(self):
        query = "SELECT DNI, Nombre, Apellido, Telefono FROM Clientes WHERE DNI=%s"
        dni = int(input("Ingrese DNI: "))
        data = (dni,)
        self.cursor.execute(query, data)
        fila = self.cursor.fetchone()
        if fila is not None:
            dni, nombre, apellido, telefono = fila
            print(
                "> DNI:",
                dni,
                "|",
                "Nombre:",
                nombre,
                "|",
                "Apellido:",
                apellido,
                "|",
                "Telefono:",
                telefono,
            )
        option = input("Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            self.clean()
        else:
            print("> No se encontraron resultados")

    def Eliminar_cliente(self):
        query = "DELETE FROM Clientes WHERE DNI = %s"
        dni = int(input("Ingresar DNI: "))
        data = (dni,)
        self.cursor.execute(query, data)
        print("> Eliminando...")
        time.sleep(1)
        print("> Volviendo al menu principal...")
        time.sleep(1)
        self.clean()
        self.connection.commit()

    # Vehiculos
    def Vehiculos(self):
        query = "SELECT * FROM Vehiculos"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)
        option = input("Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            self.clean()

    def Crear_Vehiculo(self):
        insert_query = "INSERT INTO Vehiculos (Patente,DNI, Marca, Modelo, Color) VALUES (%s,%s,%s,%s,%s)"

        patente = input("Ingrese patente: ")
        dni = input("Ingrese DNI del dueño: ")
        marca = input("Ingrese marca: ")
        modelo = input("Ingrese modelo: ")
        color = input("Ingrese color: ")

        data = (patente, dni, marca, modelo, color)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        print("> El vehiculo ha sido creado exitosamente.")
        print("> Volviendo al menu principal...")
        time.sleep(1)
        self.clean()

    def Vehiculo_especifico(self):
        query = "SELECT Patente, Marca, Modelo FROM Vehiculos WHERE Patente=%s"
        patente = input("Ingrese Patente del vehiculo: ")
        data = (patente,)
        self.cursor.execute(query, data)
        fila = self.cursor.fetchone()
        if fila is not None:
            patente, marca, modelo = fila
            print(
                "> Patente: ",
                patente,
                "|",
                "Marca: ",
                marca,
                "|",
                "Modelo: ",
                modelo,
            )
        option = input("Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            self.clean()

        else:
            print("> No se encontraron resultados")

    def Eliminar_vehiculo(self):
        query = "DELETE FROM Vehiculos WHERE Patente = %s"
        patente = input("Ingresar Patente: ")
        data = (patente,)
        self.cursor.execute(query, data)
        print("> Eliminando...")
        time.sleep(1)
        print(">Volviendo al menu principal...")
        time.sleep(1)
        self.clean()

        self.connection.commit()

    # Mecanicos
    def Mecanicos(self):
        query = "SELECT * FROM Mecanicos"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)
        option = input("> Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            self.clean()

    def Crear_Mecanico(self):
        insert_query = "INSERT INTO Mecanicos (Legajo, Nombre, Apellido, Rol, Estado) VALUES (%s, %s, %s, %s, %s)"
        legajo = input("Ingrese Legajo: ")
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        rol = input("Ingrese Rol: ")
        estado = input("Ingrese Estado (- / +): ")
        while estado not in ["-", "+"]:
            print("Estado invalido, debe ser '-' o '+'")
            estado = input("Ingrese Estado (- / +): ")

        data = (legajo, nombre, apellido, rol, estado)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        print("> Mecanico creado exitosamente.")
        print("> Volviendo al menu principal...")
        time.sleep(1)
        self.clean()

    def Mecanico_especifico(self):
        query = "SELECT Legajo, Nombre, Apellido, Rol, Estado FROM Mecanicos WHERE Legajo=%s"
        legajo = input("Ingrese Legajo del mecanico: ")
        data = (legajo,)
        self.cursor.execute(query, data)
        fila = self.cursor.fetchone()
        if fila is not None:
            legajo, nombre, apellido, rol, estado = fila
            print(
                "> Legajo:",
                legajo,
                "|",
                "Nombre:",
                nombre,
                "|",
                "Apellido:",
                apellido,
                "|",
                "Rol:",
                rol,
                "|",
                "Estado:",
                estado,
            )
        option = input("Volver al menu principal? (s): ")
        if option.lower() == "s":
            print("> Volviendo al menu principal...")
            time.sleep(1)
            self.clean()

        else:
            print("No se encontraron resultados")

    def Eliminar_mecanico(self):
        query = "DELETE FROM Mecanicos WHERE Legajo = %s"
        legajo = input("Ingresar Legajo: ")
        data = (legajo,)
        self.cursor.execute(query, data)
        print("> Eliminando...")
        time.sleep(1)
        print("> Volviendo al menu principal...")
        time.sleep(1)
        self.clean()
        self.connection.commit()

    # Ficha Tecnica
    def Crear_FichaTecnica(self):
        self.clean()
        insert_query = "INSERT INTO Ficha_tecnica (id_ficha, dni_cliente, marca, modelo, patente, motivo_ingreso, fecha_ingreso) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        id_ficha = input("Ingrese numero de ficha: ")
        dni = input("Ingrese DNI del cliente: ")
        marca = input("Ingrese marca del vehiculo: ")
        modelo = input("Ingrese modelo del vehiculo: ")
        patente = input("Ingrese patente del vehiculo: ")
        motivo_ingreso = input("Ingrese motivo de ingreso: ")
        fecha_ingreso = input("Ingrese fecha de ingreso (YYYY-MM-DD): ")

        data = (id_ficha, dni, marca, modelo, patente, motivo_ingreso, fecha_ingreso)
        try:
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            print("> Ficha técnica creada exitosamente.")
        except Exception as e:
            print("> Error al crear ficha técnica:", e)
        print("> Volviendo al menu principal...")
        time.sleep(1)
        self.clean()

    def Modificar_FichaTecnica(self):
        self.clean()
        print("Modificar Ficha Tecnica")
        id_ficha = input("Ingrese el ID de la ficha tecnica a modificar: ")
        query = "SELECT * FROM Ficha_tecnica WHERE id_ficha = %s"
        self.cursor.execute(query, (id_ficha,))
        ficha = self.cursor.fetchone()
        if not ficha:
            print("> No se encontró la ficha tecnica con ese ID.")
            time.sleep(2)
            return

        print("¿Qué desea modificar?")
        opciones = {
            1: ("Datos del Vehículo", ["marca", "modelo", "patente"]),
            2: ("Datos del Cliente", ["dni_cliente"]),
        }
        for k, v in opciones.items():
            print(f"{k}. {v[0]}")
        print("3. Cancelar")

        try:
            op = int(input("Opción: "))
            if op == 3:
                print("> Modificación cancelada.")
                return
            if op not in opciones:
                print("> Opción inválida.")
                return
            campos = opciones[op][1]
            for idx, campo in enumerate(campos, 1):
                print(f"{idx}. {campo}")
            campo_idx = int(input("Seleccione el campo a modificar: ")) - 1
            if campo_idx < 0 or campo_idx >= len(campos):
                print("> Opción inválida.")
                return
            campo_modificar = campos[campo_idx]
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo_modificar}: ")
            update_query = (
                f"UPDATE Ficha_tecnica SET {campo_modificar} = %s WHERE id_ficha = %s"
            )
            self.cursor.execute(update_query, (nuevo_valor, id_ficha))
            self.connection.commit()
            print("> Ficha tecnica modificada exitosamente.")
            time.sleep(2)
        except Exception as e:
            print("> Error al modificar la ficha tecnica:", e)
            time.sleep(2)

    def Consultar_FichaTecnica(self):
        self.clean()
        print("Consultar Ficha Tecnica")
        id_ficha = input(
            "Ingrese el ID de la ficha tecnica a consultar (deje vacío para ver todas): "
        )
        try:
            if id_ficha.strip() == "":
                query = "SELECT * FROM Ficha_tecnica"
                self.cursor.execute(query)
                fichas = self.cursor.fetchall()
                if not fichas:
                    print("> No hay fichas técnicas registradas.")
                else:
                    for ficha in fichas:
                        print(ficha)
            else:
                query = "SELECT * FROM Ficha_tecnica WHERE id_ficha = %s"
                self.cursor.execute(query, (id_ficha,))
                ficha = self.cursor.fetchone()
                if ficha:
                    print(ficha)
                else:
                    print("> No se encontró la ficha tecnica con ese ID.")
        except Exception as e:
            print("> Error al consultar ficha técnica:", e)
        input("Presione Enter para volver al menú")
        self.clean()

    # Facturacion
    def Crear_Facturacion(self):
        self.clean()
        print("Crear Facturación")
        dni = input("Ingrese DNI del cliente: ")
        fecha = input("Ingrese fecha de la factura (YYYY-MM-DD): ")
        monto = input("Ingrese monto: ")
        estado = "Emitida"
        insert_query = "INSERT INTO Facturacion (DNI_Cliente, Fecha_Factura, Monto, Estado) VALUES (%s, %s, %s, %s)"
        data = (dni, fecha, monto, estado)
        try:
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            print("> Factura creada exitosamente.")
        except Exception as e:
            print("> Error al crear la factura:", e)
        input("Presione Enter para volver al menú")
        self.clean()

    def Anular_Facturacion(self):
        self.clean()
        print("Anular Facturación")
        id_factura = input("Ingrese el ID de la factura a anular: ")
        update_query = "UPDATE Facturacion SET Estado = 'Anulada' WHERE id_factura = %s"
        try:
            self.cursor.execute(update_query, (id_factura,))
            if self.cursor.rowcount == 0:
                print("> No se encontró la factura con ese ID.")
            else:
                self.connection.commit()
                print("> Factura anulada exitosamente.")
        except Exception as e:
            print("> Error al anular la factura:", e)
        input("Presione Enter para volver al menú")
        self.clean()

    def Consultar_Facturacion(self):
        self.clean()
        print("Consultar Facturación")
        id_factura = input("Ingrese el ID de la factura a consultar (deje vacío para ver todas): ")
        try:
            if id_factura.strip() == "":
                query = "SELECT * FROM Facturacion"
                self.cursor.execute(query)
                facturas = self.cursor.fetchall()
                if not facturas:
                    print("> No hay facturas registradas.")
                else:
                    for factura in facturas:
                        print(factura)
            else:
                query = "SELECT * FROM Facturacion WHERE id_factura = %s"
                self.cursor.execute(query, (id_factura,))
                factura = self.cursor.fetchone()
                if factura:
                    print(factura)
                else:
                    print("> No se encontró la factura con ese ID.")
        except Exception as e:
            print("> Error al consultar facturación:", e)
        input("Presione Enter para volver al menú")
        self.clean()

    # Salir
    def salir(self):
        print("> Saliendo del programa...")
        time.sleep(1)
        self.cursor.close()
        self.connection.close()
        exit()


# -----Menu Manager-----

while True:
    conexion = TallerDB()
    conexion.menu()
    try:
        option = int(input("Seleccione una opcion: \n"))
    except ValueError:
        print("> Por favor, ingrese un número válido.\n")
        continue
    if option == 1:
        conexion.clean()

        conexion.menu_clientes()
        option2 = int(input("Seleccione una opcion: "))
        if option2 == 1:
            conexion.Clientes()
        elif option2 == 2:
            conexion.Crear_Cliente()
        elif option2 == 3:
            conexion.Cliente_especifico()
        elif option2 == 4:
            conexion.Eliminar_cliente()
        elif option2 == 5:
            print("> Volviendo al menu principal...")
            time.sleep(1)
            conexion.clean()
        else:
            print("> Opcion no valida, intente nuevamente.")

    elif option == 2:
        conexion.clean()
        conexion.menu_vehiculos()
        option2 = int(input("Seleccione una opcion: "))
        if option2 == 1:
            conexion.Vehiculos()
        elif option2 == 2:
            conexion.Crear_Vehiculo()
        elif option2 == 3:
            conexion.Vehiculo_especifico()
        elif option2 == 4:
            conexion.Eliminar_vehiculo()
        elif option2 == 5:
            print("> Volviendo al menu principal...")
            time.sleep(1)
            conexion.clean()

        else:
            print("> pcion no valida, intente nuevamente.")

    elif option == 3:
        conexion.clean()
        conexion.menu_mecanicos()
        option2 = int(input("Seleccione una opcion: "))
        if option2 == 1:
            conexion.Mecanicos()
        elif option2 == 2:
            conexion.Crear_Mecanico()
        elif option2 == 3:
            conexion.Mecanico_especifico()
        elif option2 == 4:
            conexion.Eliminar_mecanico()
        elif option2 == 5:
            print("> Volviendo al menu principal...")
            time.sleep(1)
            conexion.clean()
        else:
            print("> Opcion no valida, intente nuevamente.")

    elif option == 4:
        conexion.clean()
        conexion.menu_ficha_tecnica()
        option2 = int(input("Seleccione una opcion: "))
        if option2 == 1:
            conexion.Crear_FichaTecnica()
        elif option2 == 2:
            conexion.Consultar_FichaTecnica()
        elif option2 == 3:
            conexion.Modificar_FichaTecnica()
        elif option2 == 4:
            print("> Volviendo al menu principal...")
            time.sleep(1)
            conexion.clean()
        else:
            print("> Opcion no valida, intente nuevamente.")

    elif option == 5:
        conexion.clean()
        conexion.menu_facturacion()
        option2 = int(input("Seleccione una opcion: "))
        if option2 == 1:
            conexion.Crear_Facturacion()
        elif option2 == 2:
            conexion.Anular_Facturacion()
        elif option2 == 3:
            conexion.Consultar_Facturacion()
        elif option2 == 4:
            print("> Volviendo al menu principal...")
            time.sleep(1)
            conexion.clean()
        else:
            print("> Opcion no valida, intente nuevamente.")

    elif option == 6:
        conexion.salir()
    else:
        print("> Opcion no valida, intente nuevamente.")
