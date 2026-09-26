# teamFormation.py

from components import printError, printWarning, printSuccess

teamsList = []

def createTeam(registeredStudents=None, currentTeams=None):
    if currentTeams is None:
        currentTeams = teamsList
    if registeredStudents is None:
        registeredStudents = set()

    teamName = ""
    memberCount = 0
    membersList = []
    membersTuple = ()
    teamData = ()
    memberName = ""
    userChoice = ""
    isCreating = True

    print("\n--- CREACIÓN DE EQUIPO PARA COMPETENCIA (TUPLA) ---")
    while isCreating:
        try:
            teamName = input("Ingrese el nombre del equipo: ").strip()
            if not teamName:
                printError("El nombre del equipo no puede estar vacío.")
                continue

            try:
                memberCount = int(input("Ingrese la cantidad de integrantes del equipo: "))
                if memberCount <= 0:
                    printError("La cantidad de integrantes debe ser mayor a 0.")
                    continue
            except ValueError:
                printError("Ingrese un número entero válido.")
                continue

            membersList = []
            for i in range(1, memberCount + 1):
                while True:
                    memberName = input(f"Ingrese el nombre del integrante #{i}: ").strip()
                    if not memberName:
                        printError("El nombre del integrante no puede estar vacío.")
                        continue
                    if registeredStudents and memberName not in registeredStudents:
                        printWarning(f"'{memberName}' no figuraba en estudiantes registrados, pero será agregado al equipo.")
                    membersList.append(memberName)
                    break

            membersTuple = tuple(membersList)
            teamData = (teamName, membersTuple)
            currentTeams.append(teamData)
            printSuccess(f"¡Equipo '{teamName}' creado exitosamente!")
            print(f"Integrantes almacenados en Tupla: {membersTuple}")

            userChoice = input("\n¿Desea crear otro equipo? (s/n): ").strip().lower()
            if userChoice != 's':
                isCreating = False
        except Exception as e:
            printError(f"Ocurrió un error inesperado: {e}")
            isCreating = False

    return currentTeams

def displayTeams(currentTeams=None):
    if currentTeams is None:
        currentTeams = teamsList

    index = 0
    teamName = ""
    membersTuple = ()

    print("\n--- EQUIPOS REGISTRADOS ---")
    if not currentTeams:
        printWarning("No hay equipos registrados aún.")
    else:
        for index, teamData in enumerate(currentTeams, start=1):
            teamName, membersTuple = teamData
            print(f"{index}. Equipo: {teamName}")
            print(f"   Integrantes (Tupla): {membersTuple}")
    print("---------------------------")