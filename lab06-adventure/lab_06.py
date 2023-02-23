class Room:
    """A room"""
    def __init__(self, descripcion, norte, sur, este, oeste):
        """El constructor"""
        self.description = descripcion
        self.north = norte
        self.east = este
        self.west = oeste
        self.south = sur

def main():
    room_list = []
    # Room 0
    room = Room("Te despiertas en un dormitorio desconocido.\nHay puertas al norte y al este",
                norte = 5, sur = None, este = 1, oeste = None)
    room_list.append(room)
    # Room 1
    room = Room("Estas en un pasillo.\nTe encuentras una puerta al norte, el pasillo continua hacia el este",
                norte = 6, sur = None, este = 2, oeste = 0)
    room_list.append(room)
    # Room 2
    room = Room("Estas en un pasillo.\nTe encuentras una puerta al norte, el pasillo continua hacia el este o puedes volver al oeste",
                norte = 7, sur = None, este = 3, oeste = 1)
    room_list.append(room)
    # Room 3
    room = Room("Estas en un pasillo\nTe encuentras una puerta al norte, el pasillo continua hacia el este o puedes volver al oeste",
                norte = 8, sur = None, este = 4, oeste = 2)
    room_list.append(room)
    # Room 4
    room = Room("Estas en un pasillo\nEl pasillo se ha acabado y ves una ventana que da al exterior.\nHay una puerta con marcas verdes al norte o puedes volver por el pasillo al este",
                norte = 9, sur = None, este = None, oeste = 3)
    room_list.append(room)
    # Room 5
    room = Room("Has entrado a un baño\nDespués de rebuscar encuentras un pasaje hacia el oeste detrás del espejo\nPuedes ir por el pasaje o volver al dormitorio en el sur",
                norte = None, sur = 0, este = None, oeste = 11)
    room_list.append(room)
    # Room 6
    room = Room("Has entrado en un dormitorio lleno de peluches, es como si fuese el dormitorio de una princesa de cuentos\nNo hay nigún camnio más que volver al pasillo del sur",
                norte = None, sur = 1, este = None, oeste = None)
    room_list.append(room)
    # Room 7
    room = Room("En construcción\nVuelve al pasillo del sur o continua a otro sitio en construcción al este",
                norte = None, sur = 2, este = 8, oeste = None)
    room_list.append(room)
    # Room 8
    room = Room("En construcción\nVuelve al pasillo del sur o continua a otro sitio en construcción al oeste",
                norte = None, sur = 3, este = None, oeste = 7)
    room_list.append(room)
    # Room 9
    room = Room("Has entrado en un extraño laboratorio lleno de frascos con líquido verde\nHay una puerta roja con una señal de peligro al lado hacia el norte, también puedes volver por el pasillo al sur",
                norte = 10, sur = 4, este = None, oeste = None)
    room_list.append(room)
    # Room 10
    room = Room("Has entrado en una habitación completamente vacía\nLa puerta a ala habitación anterior está al sur",
                norte = None, sur = 9, este = None, oeste = None)
    room_list.append(room)
    # Room 11 (exit)
    room = Room("Has conseguido salir del edificio",
                norte = None, sur = None, este = 5, oeste = None)
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        next = input("¿Hacia donde quieres ir? ")
        # Norte
        if next.lower() in ("n", "norte"):
            next_room = room_list[current_room].north
            if next_room is None:
                print("No hay ningún camino en esta dirrección")
            else:
                current_room = next_room
        # Sur
        elif next.lower() in ("s", "sur"):
            next_room = room_list[current_room].south
            if next_room is None:
                print("No hay ningún camino en esta dirrección")
            else:
                current_room = next_room
        # Este
        elif next.lower() in ("e", "este"):
            next_room = room_list[current_room].east
            if next_room is None:
                print("No hay ningún camino en esta dirrección")
            else:
                current_room = next_room
        # Oeste
        elif next.lower() in ("o", "oeste"):
            next_room = room_list[current_room].west
            if next_room is None:
                print("No hay ningún camino en esta dirrección")
            else:
                current_room = next_room
        # Error
        else:
            print("Por favor introduce una dirección válida (inicial o nombre completo de: norte, sur, este, oeste)")

        if room_list[next_room] == room_list[11]:
            print()
            print(room_list[current_room].description)
            done = True

main()