import copy
import sys
import os
import random
import timeit

def match_pairs(all_guys, all_gals):
    guys_dict = copy.deepcopy(all_guys)
    gals_dict = copy.deepcopy(all_gals)
    pairs = {}
    guys_free = sorted(guys_dict.keys())
    while guys_free:
        guy = guys_free.pop(0)
        guy_list = guys_dict[guy]
        gal = guy_list.pop(0)
        guy2 = pairs.get(gal)
        if not guy2:
            pairs[gal] = guy
        else:
            gal_list = gals_dict[gal]
            i = gal_list.index(guy2)
            j = gal_list.index(guy)
            if i > j:
                pairs[gal] = guy
                still_had_gf = guys_dict[guy2]
                if still_had_gf:
                    guys_free.append(guy2)
                else:
                    #print(guy2 + " does not have any girls left.\n")
                    pairs = {}
                    break
            else:
                if guy_list:
                    guys_free.append(guy)
                else:
                    pairs = {}
                    break
    return pairs


def validate_pairs(all_guys, all_gals, all_pairs):
    reverse_pairs = {}
    for k, v in all_pairs.items():
        reverse_pairs[v] = k
    for gal, guy in all_pairs.items():
        guy_prefers = all_guys[guy]
        gal_prefers = all_gals[gal]
        i = guy_prefers.index(gal)
        j = gal_prefers.index(guy)
        guy_pref_better = guy_prefers[:i]
        gal_pref_better = gal_prefers[:j]
        for m in gal_pref_better:
            m_likes = all_guys[m]
            m_curr_gal = reverse_pairs[m]
            current_index = m_likes.index(m_curr_gal)
            gal_index = m_likes.index(gal)
            if current_index > gal_index:
                print(m + " prefers " + gal + " more than " + m_curr_gal + ".\n")
                return False
        for s in guy_pref_better:
            s_likes = all_gals[s]
            s_curr_guy = all_pairs[s]
            current_index = s_likes.index(s_curr_guy)
            guy_index = s_likes.index(guy)
            if current_index > guy_index:
                print(s + " prefers " + guy + " more than " + s_curr_guy + ".\n")
                return False
    return True

'''if __name__ == "__main__":
    sys_len = len(sys.argv)
    if sys_len != 2:
        print("please provide filepath as argument")
        sys.exit()
    file_path = sys.argv[1]'''
boydict={}
girldict={}
male=['m%d' %i for i in range(1,101)]
female=['w%d' %i for i in range(1,101)]
n=input('enter the value of n:')
n=int(n)
start = timeit.default_timer()

for x in range(0,n):
    finalmale=male[:n]
    finalfemale=female[:n]
print (finalmale)
print(finalfemale)

for x in range(0,n):
    guy=finalmale[x]
    boydict[guy]=random.sample(finalfemale,n)
y=str(boydict)

for x in range(0,n):
    gal=finalfemale[x]
    girldict[gal]=random.sample(finalmale,n)
z=str(girldict)
print("Relation Preferences are:")
with open("preferences.txt", 'w') as f:
    f.write("guys\n")
    for k,v in boydict.items():
        a=",".join(v)
        print(k +"="+ a )
        f.write(k +"= "+ a + "\n")
    f.write("gals\n")
    for k,v in girldict.items():
        a=",".join(v)
        print(k +"="+ a )
        f.write(k +"= "+ a + "\n")
file_path=os.path.abspath('preferences.txt')
guy_flag = False
gal_flag = False
a_guys = {}
a_gals = {}
with open(file_path) as f:
    for line in f:
        line = line.strip()
        if line == "guys":
            guy_flag = True
            gal_flag = False
            continue
        elif line == "gals":
            guy_flag = False
            gal_flag = True
            continue
        words = line.split("=")
        key = words[0].strip()
        v = words[1].strip().replace(" ", "")
        value = v.split(",")
        if guy_flag:
            a_guys[key] = value
        elif gal_flag:
            a_gals[key] = value
print("\n")
p = match_pairs(a_guys, a_gals)
print("After implementing Gale Shapely algorithm, matches are:")
if len(p) == 0:
    print("could not find perfect matches.\n")
    sys.exit()
for wife, man in p.items():
    print(man + " and " + wife)
print("Validating the pairs.\n")
t = validate_pairs(a_guys, a_gals, p)
if t:
    print("Matches are stable.\n")
    stop = timeit.default_timer()
    print "Program run time:", stop-start
    print("Now swapping 2 pairs and checking their stability.")
    #ss = sorted(a_gals.keys())
    #if len(ss) < 2:
     '  print("swapping not possible")
        sys.exit()
    k1, k2 = ss[0], ss[1]
    p[k1], p[k2] = p[k2], p[k1]
    t = validate_pairs(a_guys, a_gals, p)
    if t:
        print("still got stable pairs even after swapping.\n")
    else:
        print("New swapped pairs are unstable.\n")
else:
    print("These pairs are unstable.\n")
