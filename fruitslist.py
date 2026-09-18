
from pathlib import Path

#ACÁ LEO EL ARCHIVO TXT DONDE CONTENGO TODOS LOS NOMBRES DE LAS FRUTAS
file_path = Path(__file__).resolve().parent / "frutas.txt"
fruits = []

with open(file_path, "r", encoding="utf-8") as file:
    contents = file.read()
    fruitslist = list(contents.split())


print("Nombra tus frutas favoritas")

while True:
    print("Si no quieres siguir tipea 'listo'")

    user_input = input(": ").lower()
    print(user_input)

    if user_input == "listo":
        break
    elif user_input in fruits:
        print("Esta fruta ya la nombraste")
    elif user_input in fruitslist:
        fruits.append(user_input)
    else:
        print("La fruta que nombraste no existe...")

    print("Tu lista actual: ", fruits)