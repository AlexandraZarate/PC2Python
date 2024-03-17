def obtener_numero_mes(nombre_mes):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    return meses.get(nombre_mes, None)

def obtener_fecha():
    # Solicitar al usuario que ingrese la fecha
    fecha_input = input("Ingrese la fecha (en formato mes/día/año o nombre_mes día, año): ")

    # Dividir la fecha en sus componentes: mes, día y año
    if len(fecha_input.split()) == 3: 
        partes_fecha = fecha_input.split()
        nombre_mes = partes_fecha[0]
        dia = partes_fecha[1].rstrip(',')
        anio = partes_fecha[2]
        numero_mes = obtener_numero_mes(nombre_mes)
        fecha_formateada = f"{anio}-{numero_mes}-{dia.zfill(2)}" 
        if numero_mes is None:
            print("El nombre del mes ingresado no es válido.")
            return obtener_fecha()
    elif len(fecha_input.split()) == 1: 
        mes, dia, anio = fecha_input.split('/')
        # Formatear la fecha en el formato deseado
        fecha_formateada = f"{anio}-{mes.zfill(2)}-{dia.zfill(2)}"
        
    else:
        partes_fecha = fecha_input.split()
        print("Formato de fecha no válido. Intente de nuevo.")
    return fecha_formateada

# Obtener la fecha del usuario
fecha = obtener_fecha()

# Imprimir la fecha obtenida
print("Fecha ingresada:", fecha)