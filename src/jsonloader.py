from json import JSONEncoder, load, dump
# from os import sep


class CarteEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def exporter(data: dict, path: str = ""):
    """
    :param path: Chemin finissant par /
    :param carte:
    :return:
    """
    with open(f'{path if path == "" else path + "/"}data.json', 'w') as outfile:
        dump(data, outfile, cls=CarteEncoder)


def importer(chemin: str):
    """
    importe une Carte
    Produit une erreur si le fichier est inconnu ou n'est pas une carte
    :param chemin: Le chemin de la carte, fichier json inclus
    :return: Le premier objet carte du fichier chemin
    """
    with open(chemin, 'r') as infile:
        dico_data = load(infile)

    return dico_data


if __name__ == '__main__':
    pass
