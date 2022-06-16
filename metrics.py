import pickle, random
import numpy as np
import matplotlib.pyplot as plt
with open("teamsvecs.pkl", 'rb') as t:
    vecs = pickle.load(t)

#member indixes
members = vecs['member']
col_sums = members.sum(axis=0)

#sort the member indixes
stats = {k: v for k, v in enumerate(sorted(col_sums.A1.astype(int), reverse=True))}
plt.plot(stats.keys(),stats.values())
# plt.show()

ppl = []
unppl = []

#print(np.array(col_sums)[0][0])
col_sums = np.array(col_sums)
for i in range(col_sums.shape[1]):
    if col_sums[0][i] > 5:
       ppl.append(i)
    else:
        unppl.append(i)
print(col_sums)
print(ppl)
print(unppl)

theta = input("enter theta")

#skeew definition
def skew( predicted_teams, theta,pp_auth, unppl_auth):
    ppl_count_pred = 0
    unppl_count_pred = 0
    for i in predicted_teams:
        if int(i) in pp_auth:
            ppl_count_pred = ppl_count_pred+1
        else:
            unppl_count_pred = unppl_count_pred+1
    pred_distr_ppl = ppl_count_pred / len(predicted_teams)
    ppl_ratio = len(ppl)/len(col_sums[0])
    print(pred_distr_ppl / ppl_ratio)

all_authors = col_sums.flatten().tolist()
random.shuffle(all_authors)
print(all_authors[:3])
print(col_sums.shape)
print(type(col_sums))
skew(all_authors[:3],theta, ppl,unppl)
#print(ppl_ratio)
