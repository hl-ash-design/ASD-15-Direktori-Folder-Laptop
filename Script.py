import os
from pathlib import Path

def directory():
    print("Current directory:", os.getcwd())
    print("Contents:")
    for item in os.listdir():
        print(f"  {item}")

def changeDirectory():
    path = input("Enter the path to change to: ")
    try:
        os.chdir(path)
        print("Changed directory to:", os.getcwd())
    except FileNotFoundError:
        print("Directory not found.")
    except NotADirectoryError:
        print("Not a directory.")
    except PermissionError:
        print("Permission denied.")

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
