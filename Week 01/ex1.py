import math

def precision(tp, fp):
    return tp / (tp + fp)   

def recall(tp, fn):
    return tp / (tp + fn)

def calc_f1_score(tp, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)
    return 2 * p * r / (p + r)

print ( round ( calc_f1_score ( tp =2 , fp =4 , fn =5) , 2) )