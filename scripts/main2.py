'''
created by ashari
November 20 2017

adopted from rochana
'''

import os, tfidf, lib1, math

def findSim(keyword, pathcorpus):
    this_path = os.path.split(__file__)[0]
    pathcorpus = os.path.join(this_path, pathcorpus)

    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    table = tfidf.TfIdf()
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                # articles[item] = lib1.prepro_base(file.read()).split()
                table.add_document(item, lib1.prepro_base(file.read()).split())

    keys = keyword.split()
    result = table.similarities(keys)
    res = []
    # for x, title in result, articles:
    #     if x[1]:
    #         res.append([x[0], (round(x[1], 3)*100), title.value()])

    for x in result:
        if x[1]:
            with open(pathcorpus + '/' + x[0], 'r') as file:
                res.append([x[0], x[1], file.readline()])

    print(res)

    return res
