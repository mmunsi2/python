import pickle
import json
import requests


import pickle
#import os
import requests
#from infer_all_vectors
#to do
#recuperer tous les uri de git
#POur chaque uri inferer le vector
#Mettre l'uri et le vecteur dans le fichier

import os
os.path.isfile('./file.txt')    # True

global model 
model = pickle.load(open("doc2vec_trainedmodel_cbow_docs1200000_negative10_epochs20_mincount1200.pkl","rb"))

def infer_all_vectors(uri):
    #print ('PMU get_closest_docs 62')
    #user_doc = requests.get(uri).text
    #print ('PMU get_closest_docs 63')
    #sys.stdout.flush()
    r = requests.get(uri)
    if r.status_code == 200:
		print ('PMU get_closest_docs 200')
		#sys.stdout.flush()
		user_doc = r.text
		print("URI content length",len(user_doc))
		#code, _ = separate_code_and_comments(user_doc,"user doc") 
		#normalized_code = normalize_text(code, remove_stop_words=False, only_letters=False, return_list=False)
		user_vector = model.infer_vector(user_doc)
		return user_vector




#filename = os.path.join(os.getcwd(), 'repo.zip')
url ='https://github.com/mmunsi2/python/tree/master/pythonic'
#url = 'https://raw.githubusercontent.com/mmunsi2/python/master/pythonic/Code03_1_ContextManager.py'


with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
	for line in oldfile:
		print(line)
		user_vector=infer_all_vectors(line)
		print(user_vector)
		newfile.write(user_vector)#check this


# with open(filename, 'wb') as f:
#     f.write(r.content)
