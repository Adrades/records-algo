CONTEST = 'contest'


def aidez_moi(data):
    print(commandes.keys())


def ajout_contest(data: dict, nom: str, date: str):
    name = (nom + '§' + date).lower()
    data[name] = {}
    data[CONTEST].append(name)


def list_contest(data: dict):
    print(f"{'Noms':^20}{'Dates':^10}")
    for i in range(len(data[CONTEST])):
        print(i, '-', data[CONTEST][i].split('§'))


def add_exo(data, nom_concours, num_exo, res=0.0, *args):
    if '-n' in args:
        nom_concours = data[CONTEST][nom_concours]

    data[nom_concours][num_exo] = res
    print(f"L'exercice {num_exo} à été rajouté au coucours {nom_concours.split('§')[0]} avec un score de {res}")


commandes = {
    'help': aidez_moi,
    'add_contest': ajout_contest,
    'ac': ajout_contest,
    'liste_contest' : list_contest,
    'lc': list_contest,
    'add_exo': add_exo,
    'ae': add_exo
}
