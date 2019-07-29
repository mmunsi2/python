import sys
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances


#Exemple
#vectors={'https://raw.githubusercontent.com/mmunsi2/python/master/pythonic/Code01_1.py':
#[0.4023787, 0.40510143]}
from data01_2 import my_vectors
vectors = my_vectors
#vectors = pickle.load(open("/altair/altair/models/doc2vec_trainedmodel_cbow_docs1200000_negative10_epochs20_mincount1200.pkl","rb"))
vectors = pickle.load(open("/home/patrick/Bureau/GITS/model/word2vecp2.vectors_old","rb"))

stored_urls = list()
stored_vectors = list()
vectors_pair_sims = list()
vectors_point = list()
vectors_pair_sims_all = list()
vectors_point_all= list()

# for idx, url0 in enumerate(vectors):
#     filename = url0[url0.rfind("/Code")+5:]
#     filename = filename[0:2]     
#     del stored_vectors[:]
#     for url in vectors:
#         filename1 = url[url.rfind("/Code")+5:]
#         filename1 = filename1[0:2]
#         if filename1 ==filename and url0 != url:
#             stored_urls.append(url)
#             stored_vectors.append(vectors[url])
#             listOfStrings1 = [idx]
#             vectors_point=vectors_point+list(listOfStrings1)
#     v_url0=vectors[url0]
#     pair_sims = cosine_similarity( np.array(v_url0).reshape(1, -1), stored_vectors)
#     #pair_sims = euclidean_distances( np.array(v_url0).reshape(1, -1), stored_vectors)
#     pair_sims=pair_sims.tolist()
#     pair_sims = list(itertools.chain(*pair_sims))
#     vectors_pair_sims=vectors_pair_sims+pair_sims
#     print(idx)
# print(idx)
del stored_vectors[:]
for url in vectors:
    stored_vectors.append(vectors[url])
for idx_all, url in enumerate(vectors):
    if idx_all <5:
        listOfStrings_all = [idx_all] 
        pair_sims = cosine_similarity( np.array(vectors[url]).reshape(1, -1), stored_vectors)
        #print(model.most_similar([user_vector], topn=5))
        #print(stored_vectors.most_similar([user_vector], topn=5))
        vectors_pair_sims_all=vectors_pair_sims_all+list(pair_sims)
        vectors_point_all=vectors_point_all+list(listOfStrings_all)
        print(idx_all)
        print(pair_sims)
        indices = (-pair_sims[0]).argsort()[:5]
        print(indices)
        #return [(stored_urls[index],round(float(pair_sims[0][index]),4)) for index in indices]
        sys.exit()


a=vectors_pair_sims
x=vectors_point
a_all=vectors_pair_sims_all
x_all=vectors_point_all



plt.plot(x_all,a_all,'b.')
plt.plot(x,a,'r.')
plt.axis([-1, 55, -0.25, 1.1])
plt.show()


plt.show()






