
#to do
#recupérer tous les uri de git
#POur chaque uri inferer le vector
#Mettre l'uri et le vecteur dans le fichier

def infer_all_vectors(uri):
    #print ('PMU get_closest_docs 62')
    #user_doc = requests.get(uri).text
    #print ('PMU get_closest_docs 63')
    sys.stdout.flush()
    r = requests.get(uri)
	#print ('PMU get_uri')
	#sys.stdout.flush()
	if r.status_code == 200:
		#print ('PMU get_closest_docs 200')
		#sys.stdout.flush()
		user_doc = r.text
		print("URI content length",len(user_doc))
		code, _ = separate_code_and_comments(user_doc,"user doc") 
		normalized_code = normalize_text(code, remove_stop_words=False, only_letters=False, return_list=False)
		user_vector = model.infer_vector(normalized_code)


