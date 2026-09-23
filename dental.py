# --------------------------------------------------------------------------
# ORGANIZACIÓN: Consultorio Odontológico Cajamarca
# SISTEMA: Gestión de Citas y Especialidades v1.0
# SECTOR: Servicios de Salud / Salud Bucal y Estética
# --------------------------------------------------------------------------

def registrar_atencion():
    print("================================================")
    print("        CONSULTORIO ODONTOLÓGICO CAJAMARCA      ")
    print("================================================")

    # Captura de datos del paciente
    nombre_paciente = input("Nombre completo del paciente: ")
    edad = int(input("Edad del paciente: "))

    print("\n--- Seleccione la Especialidad Requerida ---")
    print("1. Cirugía Odontológica")
    print("2. Odontología Estética")
    opcion = input("Ingrese el número de la opción (1-2): ")

    # Lógica de asignación de sector y especialidad
    if opcion == "1":
        especialidad = "Cirugía Odontológica"
        box_atencion = "Box A - Quirófano y Cirugía"
        indicaciones = "Paciente requiere evaluación pre-operatoria. Ayuno de 6 horas si aplica."
    elif opcion == "2":
        especialidad = "Odontología Estética"
        box_atencion = "Box B - Estética y Blanqueamiento"
        indicaciones = "Paciente requiere profilaxis previa al tratamiento estético."
    else:
        print("\n[ERROR] Opción no válida. Registro cancelado.")
        return

    # Mostrar ticket de ejecución / Caso de prueba exitoso
    print("\n================================================")
    print("           REGISTRO DE ATENCIÓN EXITOSO         ")
    print("================================================")
    print(f"Paciente: {nombre_paciente}")
    print(f"Edad: {edad} años")
    print(f"Especialidad: {especialidad}")
    print(f"Área Asignada: {box_atencion}")
    print(f"Indicaciones: {indicaciones}")
    print("================================================")

# Ejecución del caso de prueba
if __name__ == "__main__":
    registrar_atencion()