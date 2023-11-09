animais = ["Cachorro", "Gato", "Elefante", "Girafa", "Leao", "Tigre", "Zebra", "Rinoceronte", "Hipopotamo", "Pinguim","Cobra", "Gorila", "Jacare", "Urubu", "Tubarao", "Camelo", "Urso", "Esquilo", "Hiena", "Carcara"]

animais.sort()

for i in animais:
    print(i)

with open("animais.csv", "w") as arquivo:
    for i in animais:
        arquivo.write(i + "\n")