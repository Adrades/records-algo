from commandes import commandes, CONTEST
from jsonloader import importer, exporter
import os

if os.path.isfile("./data.json"):
    data = importer("./data.json")
else:
    data = {CONTEST: []}

if not CONTEST in data.keys():
    data[CONTEST] = []


continu = True
while continu:

    com, *rest= input('> ').lower().split()

    try:
        if com in commandes:
            commandes[com](data, *rest)
        else:
            print("Mauvaise commande")
            commandes['help'](data)
    except TypeError as e:
        print(e)


    if (input("\nVoulez vous continuer? [O/n] ").lower() + ' ')[0] == 'n':
        continu = False

exporter(data, '.')
