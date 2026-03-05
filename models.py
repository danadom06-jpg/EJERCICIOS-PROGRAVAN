#Modulo de Personas (Herencia)
class Persona:
    def __init__(self,id_persona, nombre,email, telefono):
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        self.id_persona=id_persona

    def login(self):
        print(f"Hola {self.nombre} con id: {self.id_persona} ha iniciado sesión")

    def logout(self):
        print(f"Hola {self.nombre} con id: {self.id_persona} ha cerrado sesión")

    def actualizardatos(self,nuevo_id, nuevo_nombre, nuevo_email, nuevo_telefono): 
        self.nombre=nuevo_nombre
        self.email=nuevo_email
        self.telefono=nuevo_telefono
        self.id_persona=nuevo_id
        print(f"Tus datos se han actualizado correctamente, hola {self.nombre} ")

class Usuario(Persona):
    def __init__(self,id_persona, nombre, email, telefono):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntos_fidelidad = 0
        self.historial_reservas = []
    
    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        self.puntos_fidelidad += 100
        print("Reserva creada con éxito.")

    def consultar_promociones(self):
        print("Promociones disponibles: 2x1 los lunes y miercoles.")
    
    def cancelar_reserva(self, reserva):
        if reserva in self.historial_reservas:
            self.historial_reservas.remove(reserva)
            print("Reserva cancelada.")
        else:
            print("Reserva no encontrada, intentelo nuevamente.")

lista_peliculas = []
lista_funciones = []
lista_promociones = []
class Empleado(Persona):
    r_validos = ["admin", "taquillero", "limpieza"]
    
    def __init__(self, id_persona, nombre, email, telefono, id_empleado, rol,horario):
        super().__init__(id_persona, nombre, email, telefono)
        self.id_empleado = id_empleado
        self.horario = horario
        self.rol = rol
        rol = rol.lower()
        if rol not in Empleado.r_validos:
            raise ValueError("Rol no válido, (recuerda que solo hay: admin, taquillero, limpieza)")

    def marcar_entrada(self):
        print(self.nombre, self.rol,  "marcó entrada")

    def agregar_pelicula(self, pelicula):
        if self.rol == "admin":
            lista_peliculas.append(pelicula)
            print(f"Película agregada correctamente")
        else:
            print("No tienes permisos")

    def agregar_funcion(self, funcion):
        if self.rol == "admin":
            lista_funciones.append(funcion)
            print(f"Función agregada correctamente")
        else:
            print("No tienes permisos")

    def agregar_promocion(self, promocion):
        if self.rol == "admin":
            lista_promociones.append(promocion)
            print(f"Promoción {promocion} agregada correctamente")
        else:
            print("No tienes permisos")
    
    #Modulo de infraestructura
class Espacio:
    def __init__(self, id_espacio, nombre, ubicacion):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.disponible = True

    def verificar_disponibilidad(self):
        print(f"El espacio {self.nombre} fue verificado con éxito en la ubicación {self.ubicacion}.")
        return self.disponible

    def limpiar_espacio(self):
        print(f"El espacio {self.nombre} fue limpiado con éxito en la ubicación {self.ubicacion}.")
        self.disponible = True

class Sala(Espacio):
    t_validos = ["2D", "3d", "imax"]
    capacidad_maxima = 70
    def __init__(self, id_espacio, nombre, ubicacion, tipo, capacidad_total, VIP=False):
        super().__init__(id_espacio, nombre, ubicacion)

        tipo = tipo.lower()
        if tipo not in Sala.t_validos:
            print("Tipo no válido, (recuerda que solo hay: 2D, 3D, IMAX)")
        if capacidad_total > Sala.capacidad_maxima:
            print(f"Capacidad total no válida, (recuerda que la capacidad máxima es de {Sala.capacidad_maxima} personas)")
            capacidad_total = Sala.capacidad_maxima
        self.tipo = tipo
        self.capacidad_total = capacidad_total
        self.VIP = VIP
        self.aforo_actual =capacidad_total

    def ajustar_foro(self, nueva_capacidad):
        self.capacidad_total = nueva_capacidad
        self.aforo_actual = nueva_capacidad
        if nueva_capacidad > Sala.capacidad_maxima:
            print(f"La nueva capacidad {nueva_capacidad} excede la capacidad máxima de la sala {self.nombre}.")
        else:
            self.aforo_actual = nueva_capacidad
            print(f"La sala {self.nombre} fue ajustada con éxito a una capacidad de {nueva_capacidad}.")
    
    def obtener_tipo_sala(self):
        if self.VIP:
            return "VIP"
        else:
            return "Regular"

class ZonaComida(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion):
        super().__init__(id_espacio, nombre, ubicacion)
        self.lista_productos = []   
        self.stock_actual = {} 
    def agregar_producto(self, producto, cantidad):
        if producto not in self.lista_productos:
            self.lista_productos.append(producto)
            self.stock_actual[producto.nombre] = cantidad
        print(f"El producto {producto.nombre} fue agregado a la zona de comida con una cantidad de {cantidad} unidades en stock.")

    def vender_producto(self, nombre_producto):
        if nombre_producto in self.stock_actual:
            if self.stock_actual[nombre_producto] > 0:
                self.stock_actual[nombre_producto] -= 1
                print(f"El producto {nombre_producto} fue vendido con éxito, stock restante: {self.stock_actual[nombre_producto]} unidades.")
            else:
                print("No hay stock disponible")
        else:
            print("El producto no existe")

    def actualizar_inventario(self, nombre_producto, nueva_cantidad):
        if nombre_producto in self.stock_actual:
            self.stock_actual[nombre_producto] = nueva_cantidad
            print("Inventario actualizado")
        else:
            print("El producto no existe")

#Logica de funciones y películas
class Pelicula:
    def __init__(self, id_pelicula, titulo, duracion, genero, clasificacion):
        self.id_pelicula=id_pelicula
        self.titulo=titulo
        self.duracion=duracion
        self.genero=genero
        self.clasificacion=clasificacion
    def obtener_sinopsis(self):
        return (f"{self.titulo} es una película del género {self.genero}")

    def es_apta_para_todo_publico(self):
        return self.clasificacion.upper()=="A"
   
#Funcion 
class Funcion:
    def __init__(self, id_funcion, pelicula, sala, horario_inicio, precio_base):
        self.id_funcion=id_funcion
        self.pelicula=pelicula
        self.sala=sala
        self.horario_inicio=horario_inicio
        self.precio_base=precio_base
        self.asientos_ocupados=[]

    def calcular_asientos_libres(self):
        return self.sala.capacidad_total - len(self.asientos_ocupados)

    def obtener_detalles_funcion(self):
        return f"La pelicula {self.pelicula.titulo} inicia a las {self.horario_inicio}"
    
#Gestion comercial
class Promocion:
    def __init__(self, codigo, descripcion, descuento, fecha_expiracion):
        self.codigo=codigo
        self.descripcion=descripcion
        self.descuento=descuento
        self.fecha_expiracion=fecha_expiracion
    def es_valida(self, fecha_actual):
        return fecha_actual <= self.fecha_expiracion

    def aplicar_descuento(self, monto):
        descuento = monto * (self.descuento / 100)
        return monto - descuento
    
class Reserva:
    estados_validos = ["pendiente", "confirmada", "cancelada"]
    def __init__(self, id_reserva, usuario, funcion, asientos):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = []
        self.monto_total = 0
        self.estado = "confirmada"
        for asiento in asientos:
            if asiento not in funcion.asientos_ocupados:
                self.asientos.append(asiento)
                funcion.asientos_ocupados.append(asiento)
            else:
                print("El asiento", asiento, "ya está ocupado")
        self.calcular_total()

    def calcular_total(self):
        self.monto_total = len(self.asientos) * self.funcion.precio_base

    def aplicar_promocion(self, promo):
        if promo.es_valida(fecha_actual):
            self.monto_total = promo.aplicar_descuento(self.monto_total)
            print("Promoción aplicada")

    def confirmar_pago(self):
        self.estado = "pagada"
        print("Pago confirmado")

    def generar_ticket(self):
        print("------ TICKET ------")
        print("Película:", self.funcion.pelicula.titulo)
        print("Asientos:", self.asientos)
        print("Total:", self.monto_total)
        print("Estado:", self.estado)