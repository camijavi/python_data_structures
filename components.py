# components.py

import os

def clearConsole():
    commandName = 'cls' if os.name == 'nt' else 'clear'
    os.system(commandName)

def pauseConsole():
    promptMessage = "\nPresione Enter para continuar..."
    input(promptMessage)

def printError(message=""):
    formattedText = f"Error: {message}"
    print(formattedText)

def printWarning(message=""):
    formattedText = f"Advertencia: {message}"
    print(formattedText)

def printSuccess(message=""):
    formattedText = f"Éxito: {message}"
    print(formattedText)