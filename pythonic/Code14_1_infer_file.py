import sys
import sys
#import numpy as np
import itertools
import requests 
import pickle
import gensim
from util.separate_code_and_comments import separate_code_and_comments
from util.normalize_text import normalize_text
from sklearn.metrics.pairwise import cosine_similarity
from gensim import models
from gensim.models import Word2Vec, KeyedVectors, Doc2Vec

def infer_file():
    print ('1...')
    #print (model.vocabulary())
    sys.stdout.flush()
    with open('oldfile.txt') as oldfile, open('data01_2.py', 'w') as newfile:
        print ('2...')
        sys.stdout.flush()
        first_line=True
        for line in oldfile:
            line=line.replace('\n', '')
            r = requests.get(line)
            if r.status_code == 200:
                print ('200...')
                sys.stdout.flush()
                user_doc = r.text
                code, _ = separate_code_and_comments(user_doc,"user doc")   
                normalized_code = normalize_text(code, remove_stop_words=False, only_letters=False, return_list=True)
                model.random.seed(0)
                #user_vector = model.infer_vector(normalized_code,100)
                #user_vector = model.infer_vector(doc_words=normalized_code, steps=500, alpha=0.025)
                user_vector = model.infer_vector(doc_words=normalized_code)
                print(line)
                #print(model.docvecs.most_similar([user_vector], topn=5))
                print(model.most_similar([user_vector], topn=5))
                #print("{}: {:.4f}".format(*result[0]))
                #print(model.similar_by_vector(user_vector, topn=5, restrict_vocab=None))
                #user_vector = model.infer_vector(normalized_code)
                if first_line:
                    newfile.write("my_vectors={")
                    first_line=False
                else:
                    newfile.write(",")
                newfile.write("'"+line+"':")
                newfile.write("\n")
                user_vector=list(user_vector)
                user_vector=str(user_vector)
                newfile.write(user_vector)
                newfile.write("\n")
                sys.stdout.flush()
        newfile.write("}")



print(sys.version)
#print(sys.modules.version()) 
global model
#model_file="/altair/altair/models/doc2vec_trainedmodel_cbow_docs1200000_negative10_epochs20_mincount1200.pkl"
#pickle.dump(model, model_file, protocol=2)
#model = pickle.load(open(model_file,"rb"))
#model = pickle.Unpickler(open(model_file))
#model = Word2Vec.load("model/word2vec.model")
#model =Doc2Vec.load("model/word2vec.model")
#model = pickle.load(open("model/word2vec.model", 'rb'))
model = pickle.load(open("word2vecp2.model","rb"))
#model = pickle.load(open("/home/patrick/Bureau/GITS/model/word2vecp2.model","rb"))

#print(model.wv.word_vec('test'))
#print(model.wv.most_similar('condition'))

#sys.exit()


# sentences2 = gensim.models.word2vec.LineSentence("Code01_2.py")
# model.build_vocab(sentences2, update=True)
# model.train(sentences2)






infer_file()
