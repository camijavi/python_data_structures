# eventInfo.py

from components import printError, printWarning, printSuccess

eventsDict = {
    "Coding": [],
    "Quiz": [],
    "Gaming": []
}

def registerStudentToEvent(registeredStudents=None, currentEvents=None):
    if currentEvents is None:
        currentEvents = eventsDict
    if registeredStudents is None:
        registeredStudents = set()

    selectedEvent = ""
    studentName = ""
    newEvent = ""
    userChoice = ""
    choice = 0
    eventList = list(currentEvents.keys())
    isRegistering = True

    print("\n--- REGISTRO A EVENTOS (DICCIONARIO) ---")
    while isRegistering:
        try:
            eventList = list(currentEvents.keys())
            print("\nEventos disponibles:")
            for idx, eventName in enumerate(eventList, start=1):
                print(f"{idx}. {eventName}")
            print(f"{len(eventList) + 1}. Agregar nuevo evento")

            try:
                choice = int(input("Seleccione una opción de evento: "))
            except ValueError:
                printError("Debe ingresar un número entero.")
                continue

            if 1 <= choice <= len(eventList):
                selectedEvent = eventList[choice - 1]
            elif choice == len(eventList) + 1:
                newEvent = input("Ingrese el nombre del nuevo evento: ").strip()
                if not newEvent:
                    printError("El nombre del evento no puede estar vacío.")
                    continue
                if newEvent not in currentEvents:
                    currentEvents[newEvent] = []
                selectedEvent = newEvent
            else:
                printWarning("Opción fuera de rango.")
                continue

            studentName = input(f"Ingrese el nombre del estudiante para '{selectedEvent}': ").strip()
            if not studentName:
                printError("El nombre del estudiante no puede estar vacío.")
                continue

            if registeredStudents and studentName not in registeredStudents:
                printWarning(f"'{studentName}' no figuraba en estudiantes registrados generales.")

            if studentName in currentEvents[selectedEvent]:
                printWarning(f"El estudiante '{studentName}' ya está inscrito en '{selectedEvent}'.")
            else:
                currentEvents[selectedEvent].append(studentName)
                printSuccess(f"Estudiante '{studentName}' registrado exitosamente en el evento '{selectedEvent}'!")

            userChoice = input("\n¿Desea registrar otro estudiante en un evento? (s/n): ").strip().lower()
            if userChoice != 's':
                isRegistering = False
        except Exception as e:
            printError(f"Ocurrió un error inesperado: {e}")
            isRegistering = False

    return currentEvents

def displayEventInfo(currentEvents=None):
    if currentEvents is None:
        currentEvents = eventsDict

    eventName = ""
    studentsList = []

    print("\n--- INFORMACIÓN DE EVENTOS (DICCIONARIO) ---")
    if not currentEvents:
        printWarning("No hay eventos disponibles.")
    else:
        for eventName, studentsList in currentEvents.items():
            print(f"\nEvento: {eventName}")
            if studentsList:
                print(f"  Estudiantes inscritos: {', '.join(studentsList)}")
            else:
                print("  Estudiantes inscritos: Ninguno")
    print("--------------------------------------------")