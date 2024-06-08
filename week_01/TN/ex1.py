from TL.ex1 import f1_score as calc_f1_score

if __name__ == '__main__':
    print(round(calc_f1_score(tp=2,fp=4,fn=5), 2))