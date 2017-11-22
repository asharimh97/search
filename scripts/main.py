"""
author rochanaph
October 23 2017

edited by ashari
November 18 2017
"""

import lib1, lib2, lib3, os

def main():
    path = './text files'
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = lib1.prepro_base(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = lib2.bow(list_token)   # membuat bow
        list_of_bow.append(dic)    # append bow ke list kosong yg di atas

    # membuat matrix
    matrix_akhir = lib2.matrix(list_of_bow) # jalankan fungsi matrix ke list_of_bow

    # mencari jarak
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        jarak[key] = lib3.euclidean(matrix_akhir[0], vektor) # simpan nama file sbg key, jarak sbg value
    return jarak

# print main()


def findSim(pathfile, pathcorpus):
# def findSim(keyword, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    this_path = os.path.split(__file__)[0]
    pathcorpus = os.path.join(this_path, pathcorpus)
    pathfile   = os.path.join(this_path, pathfile)

    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = lib1.prepro_base(file.read())

    # tambahkan artikel yg dicari ke dictionary
    findname = pathfile.split("/")[-1]
    try:
        articles[findname]
    except:
        with open(pathfile, 'r') as file:
            articles[findname] = lib1.prepro_base(file.read())

    # tambahkan keyword yang dicari
    # keyw = lib1.prepro_base(keyword)

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = lib2.bow(list_token)
        list_of_bow.append(dic)

    # bow keyword
    # list_token_key = keyw.split() # jadikan list
    # dic_bow = lib2.bow(list_token_key) # jadikan dictionary
    # vector_key = []


    # matrix
    matrix_akhir = lib2.matrix(list_of_bow)
    # matrix_akhir = lib3.tfidf(dic_bow, list_of_bow)

    # jarak
    id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = lib3.euclidean(matrix_akhir[id_file], vektor)
            # jarak[key] = vektor

    resu = lib2.sortdic(jarak, descending=False)
    print resu
    return resu

print findSim('./text files/ot_2.txt','./text files')
