# Три человка у каждого три хобби(в массивее), потом отдельная характерисстика id и работа. Чтобы все заносилось в инпут
person = {'и1': {'Хобби': ['х11', 'x12', 'x13'], 'ID': '1', 'Работа': 'rab1'}, 'и2': {'Хобби': ['x21', 'x22', 'x23'], 'ID': '2', 'Работа': 'rab2'}, 'и3': {'Хобби': ['x31', 'x32', 'x33'], 'ID': '3', 'Работа': 'rab3'}}
print("Реестр людей")
# massiv=["Первый", "Второй", "Третий"]
# param=["Хобби", "id", "Работа"]
# for i in massiv:
#     username = input(f"Введите имя {i} человека: ")
#     userhobby = input("Введите 3 хобби: ")
#     massivhobby = userhobby.split(",")
#     userid = input("Введите id: ")
#     userwork = input("Введите название работы: ")
#     person[username] = {"Хобби": massivhobby, "ID": userid, "Работа": userwork}
# print(person)


for user in person:
    hobby = ""
    for el in person[user]["Хобби"]:
        hobby += f"{el},"
    hobby_new = hobby[:-1]
    print("Имя:", user)
    print("Хобби:", hobby_new)
    print("ID:", person[user]["ID"])
    print("Работа:", person[user]["Работа"])
    print("")
    