# studentRegistration.py

from components import printError, printWarning, printSuccess

registeredStudents = set()

def registerStudent(studentsSet=None):
    if studentsSet is None:
        studentsSet = registeredStudents

    studentName = ""
    isAdding = True
    userChoice = ""

    print("\n--- REGISTRO DE ESTUDIANTES (SET) ---")
    while isAdding:
        try:
            studentName = input("Ingrese el nombre del estudiante a registrar: ").strip()
            if not studentName:
                printError("El nombre no puede estar vacío.")
                continue

            if studentName in studentsSet:
                printWarning(f"El estudiante '{studentName}' ya se encuentra registrado.")
            else:
                studentsSet.add(studentName)
                printSuccess(f"Estudiante '{studentName}' registrado exitosamente.")

            userChoice = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
            if userChoice != 's':
                isAdding = False
        except Exception as e:
            printError(f"Ocurrió un error inesperado: {e}")
            isAdding = False

    return studentsSet

def displayRegisteredStudents(studentsSet=None):
    if studentsSet is None:
        studentsSet = registeredStudents

    studentList = list(studentsSet)
    totalStudents = len(studentList)
    index = 0
    name = ""

    print("\n--- LISTA DE ESTUDIANTES REGISTRADOS ---")
    if totalStudents == 0:
        printWarning("No hay estudiantes registrados aún.")
    else:
        for index, name in enumerate(studentList, start=1):
            print(f"{index}. {name}")
    print("---------------------------------------")
