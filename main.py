# main.py

import sys
from components import clearConsole, pauseConsole, printError, printWarning, printSuccess
from studentRegistration import registerStudent, displayRegisteredStudents, registeredStudents
from teamFormation import createTeam, displayTeams, teamsList
from eventInfo import registerStudentToEvent, displayEventInfo, eventsDict

def main():
    menuChoice = ""
    isRunning = True

    localRegisteredStudents = registeredStudents
    localTeams = teamsList
    localEvents = eventsDict

    while isRunning:
        try:
            clearConsole()
            print("==================================================")
            print("   Sistema de Registro del Fest Universitario    ")
            print("==================================================")
            print("1. Registrar estudiante (Set)")
            print("2. Mostrar estudiantes registrados")
            print("3. Formar equipo para competencia (Tupla)")
            print("4. Mostrar equipos formados")
            print("5. Registrar estudiante a evento (Diccionario)")
            print("6. Mostrar información de eventos")
            print("7. Salir")
            print("==================================================")

            menuChoice = input("Seleccione una opción (1-7): ").strip()

            match menuChoice:
                case "1":
                    clearConsole()
                    registerStudent(localRegisteredStudents)
                    pauseConsole()
                case "2":
                    clearConsole()
                    displayRegisteredStudents(localRegisteredStudents)
                    pauseConsole()
                case "3":
                    clearConsole()
                    createTeam(localRegisteredStudents, localTeams)
                    pauseConsole()
                case "4":
                    clearConsole()
                    displayTeams(localTeams)
                    pauseConsole()
                case "5":
                    clearConsole()
                    registerStudentToEvent(localRegisteredStudents, localEvents)
                    pauseConsole()
                case "6":
                    clearConsole()
                    displayEventInfo(localEvents)
                    pauseConsole()
                case "7":
                    printSuccess("¡Saliendo del programa! Gracias por usar el Sistema de Registro del Fest Universitario.")
                    isRunning = False
                case _:
                    printWarning("Opción no válida. Por favor, intente de nuevo.")
                    pauseConsole()
        except Exception as e:
            printError(f"Ocurrió un error en el menú principal: {e}")
            pauseConsole()

if __name__ == "__main__":
    main()
