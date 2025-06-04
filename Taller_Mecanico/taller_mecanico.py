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
        print("1. Clientes")
        print("2. Vehiculos")
        print("3. Mecanicos")
        print("4. Salir")

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
        conexion.salir()
    else:
        print("> Opcion no valida, intente nuevamente.")
