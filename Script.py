import os
from pathlib import Path

def directory():
    print(os.getcwd())

def changeDirectory():
    pass

def createFolder():
    pass

def moveFolder():
    pass

def deleteFolder():
    pass

def renameFolder():
    pass

def searchDirectory():
    pass

def printHelp():
    pass

def main():
    printHelp()
    command = input("Enter a command: ")
    while command != "exit":
        if command == "dir":
            directory()
        elif command == "cd":
            changeDirectory()
        elif command == "mkdir":
            createFolder()
        elif command == "move":
            moveFolder()
        elif command == "rmdir":
            deleteFolder()
        elif command == "rename":
            renameFolder()
        elif command == "search":
            searchDirectory()
        elif command == "help":
            printHelp()
        else:
            print("Invalid command. Type 'help' for a list of commands.")
        
        command = input("Enter a command: ")
    print("Exiting...")