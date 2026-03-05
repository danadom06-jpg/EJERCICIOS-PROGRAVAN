from models import *

per1=Persona(1, "Ana", "ana@email.com", 123999555)
per2=Persona(2, "Fernando", "fernando02@gmail.com", 5522998877)
per3=Persona(3, "Lucía", "lucia23@hotmail.com", 5541237788)
per4=Persona(4, "Carlos", "carlos.mtz@gmail.com", 5512345678)
per5=Persona(5, "María", "maria.lopez@yahoo.com", 5587654321)
per6=Persona(6, "Jorge", "jorge.ramirez@gmail.com", 5598765432)
per7=Persona(7, "Sofía", "sofia.garca@outlook.com", 5576543210)
per8=Persona(8, "Luis", "luis.perez@gmail.com", 5567890123)
per9=Persona(9, "Valeria", "valeria.hernandez@gmail.com", 5534567890)
per10=Persona(10, "Diego", "diego.santos@hotmail.com", 5523456789)

admin=Empleado(21, "Pedro", "pedro@cine.com", 5511223344, 101, "admin", "9-18")
taquillero=Empleado(22, "Laura", "laura@cine.com", 5522334455, 102, "taquillero", "10-19")
limpieza=Empleado(23, "Miguel", "miguel@cine.com", 5533445566, 103, "limpieza", "7-15")

#SE utilizo IA para dar el ejmplo de las peliculas

pel1 = Pelicula(1, "Dune: Part Two", 155, "Sci-Fi", "B")
pel2 = Pelicula(2, "Oppenheimer", 180, "Drama", "B")
pel3 = Pelicula(3, "Barbie", 120, "Comedia", "A")
pel4 = Pelicula(4, "Avatar: The Way of Water", 190, "Sci-Fi", "A")
pel5 = Pelicula(5, "Spider-Man: Across the Spider-Verse", 140, "Animacion", "A")
pel6 = Pelicula(6, "The Batman", 175, "Accion", "B")
pel7 = Pelicula(7, "Frozen II", 110, "Animacion", "A")
pel8 = Pelicula(8, "Interstellar", 169, "Sci-Fi", "B")
pel9 = Pelicula(9, "Titanic", 195, "Romance", "A")
pel10 = Pelicula(10, "Inception", 148, "Sci-Fi", "B")


print("----- PRUEBA PERSONAS -----") #los objetos estan en la parte superior
per1.login()
per1.actualizardatos(1,"Ana Lopez","ana2@mail.com",9999)
per1.logout()

per2.login()
per2.logout()
print("----- PRUEBA EMPLEADOS -----")

admin.marcar_entrada()
taquillero.marcar_entrada()

print("----- CREAR PELICULAS -----")

admin.agregar_pelicula(pel1)
admin.agregar_pelicula(pel2)

print(pel1.obtener_sinopsis())
print("¿Apta para todo público?",pel1.es_apta_para_todo_publico())

print("---- SALAS -----")
sala1=Sala(1,"Sala IMAX","Piso 1","IMAX",60,True)
sala2=Sala(2,"Sala 3D","Piso 2","3D",50)

sala1.verificar_disponibilidad()
sala1.limpiar_espacio()

sala1.ajustar_foro(65)

print("Tipo de sala:",sala1.obtener_tipo_sala())

print("---- FUNCIONES -----")

func1=Funcion(1,pel1,sala1,"19:00",120)
func2=Funcion(2,pel2,sala2,"21:00",100)

admin.agregar_funcion(func1)
admin.agregar_funcion(func2)

print(func1.obtener_detalles_funcion())

print("Asientos libres:",func1.calcular_asientos_libres())

print("----- PROMOCIONES -----")
promo1=Promocion("PROMO20","Descuento 20%",20,"2026")
admin.agregar_promocion(promo1)
precio=300
nuevo_precio=promo1.aplicar_descuento(precio)
print("Precio original:",precio)
print("Precio con descuento:",nuevo_precio)
print("---- USUARIO Y RESERVAS -----")
cliente=Usuario(50,"Carlos","cliente@mail.com",8888)
cliente.login()

cliente.consultar_promociones()

reserva1=Reserva(1,cliente,func1,["A1","A2"])

cliente.crear_reserva(reserva1)

print("Total de la reserva:",reserva1.monto_total)
reserva1.confirmar_pago()
reserva1.generar_ticket()
cliente.cancelar_reserva(reserva1)
cliente.logout()
print("---- ZONA DE COMIDA -----")
zona=ZonaComida(1,"Snacks","Planta baja")
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
palomitas=Producto("Palomitas",80)
refresco=Producto("Refresco",50)
zona.agregar_producto(palomitas,10)
zona.agregar_producto(refresco,8)
zona.vender_producto("Palomitas")
zona.vender_producto("Refresco")
zona.actualizar_inventario("Palomitas",20)
print("---- GRACIAS POR USAR ESTE PROGRAMA, QUE TENGA LINDO DIA :) -----")

