"""
author rochanaph
September 21 2017

edited by ashari
November 18 2017
"""
import math
def euclidean(vector1, vector2):
    """
    fungsi untuk menghitung jarak antara 2 vektor dengan rumus euclidean ddistance
    :param vector1: vektor 1
    :param vector2: vektor
    :return:
    """
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist

def cosine(vector1, vector2):
    """
    :param vector1:
    :param vector2:
    :return:
    """

    dot  = sum([a*b for a,b in zip(vector1, vector2)])
    mag1 = math.sqrt(sum([a**2 for a in vector1]))
    mag2 = math.sqrt(sum([a**2 for a in vector2]))
    return dot/(mag1*mag2)

# fungsi yang akan digunakan sebagai algoritme pembobotan
def tf(keyword_bow, list_of_bow):
    '''
    membuat matrix representasi bow dari query/keyword
    :param keyword : bow dari kata kunci
    :param list_of_bow : list yang berisi dictionary bow
    :return matrix representasi kemunculan kata dalam dokumen
    '''

    # menyimpan vocab unik terurut abjad dari semua bow
    vocab_key = []
    jumlah_artikel = len(list_of_bow)
    for item in keyword_bow:
        vocab_key.extend(item)
    vocab_key = sorted(list(set(vocab_key)))

    # membuat matriks kosong dengan ukuran jumlah bow x jumlah vocab unik
    matrix_result = []
    for i in range(jumlah_artikel):
        matrix_result.append([])

    for j in range(jumlah_artikel):
        for kata in vocab_key:
            if kata not in list_of_bow[j].keys():
                matrix_result[j].append(0)
            else :
                matrix_result[j].append(list_of_bow[j][kata])

    return matrix_result

def idf(keyword_bow, list_of_bow):
    jumlah_artikel = len(list_of_bow)
    jumlah_keyword = len(keyword_bow)

    matrix_tf = tf(keyword_bow, list_of_bow)
    matrix_df = []
    matrix_ddf = []
    matrix_idf = []

    for k in range(jumlah_artikel):
        matrix_df.append(0)
        matrix_ddf.append(0)
        matrix_idf.append(0)

    for i in range(jumlah_keyword):
        for j in range(jumlah_artikel):
            if matrix_tf[j][i] :
                matrix_df[i] = matrix_df[i] + 1

    for i in range(jumlah_artikel):
        if matrix_df[i] :
            matrix_ddf[i] = jumlah_artikel/matrix_df[i]
            matrix_idf[i] = math.log10(matrix_ddf[i])
        else :
            matrix_ddf[i] = matrix_idf[i] = 0

    return matrix_idf

def tfidf(keyword_bow, list_of_bow):
    jumlah_keyword = len(keyword_bow)
    jumlah_artikel = len(list_of_bow)

    matrix_tf = tf(keyword_bow, list_of_bow)
    matrix_idf = idf(keyword_bow, list_of_bow)

    matrix_result = []
    for i in range(jumlah_artikel):
        matrix_result.append(0)

    for j in range(jumlah_artikel):
        for k in range(jumlah_keyword):
            matrix_result[j] = matrix_result[j] + (matrix_tf[k][j] * matrix_idf[k])

    return matrix_result

p = [1,1,1,1,2,0,0]
q = [0,0,1,1,1,1,1]

# print euclidean(p,q)
# print cosine(p,q)
