#Viết function thực hiện đánh giá classification model bằng F1-Score.

def precision(tp, fp):
    if type(tp) != int:
        return 'tp must be an integer'
    if type(fp) != int:
        return 'fp must be an integer'
    elif tp < 0:
        return 'tp must be positive'
    elif fp < 0:
        return 'fp must be positive'
    
    return tp / (tp + fp)   

def recall(tp, fn):
    if type(tp) != int:
        return 'tp must be an integer'
    if type(fn) != int:
        return 'fn must be an integer'
    elif tp < 0:
        return 'tp must be positive'
    elif fn < 0:
        return 'fn must be positive'
        
    return tp / (tp + fn)

def f1_score(tp, fp, fn):
    if type(tp) != int:
        return 'tp must be an integer'
    if type(fp) != int:
        return 'fp must be an integer'
    if type(fn) != int:
        return 'fn must be an integer'
    elif tp < 0:
        return 'tp must be positive'
    elif fp < 0:
        return 'fp must be positive'
    elif fn < 0:
        return 'fn must be positive'
        
    p = precision(tp, fp)
    r = recall(tp, fn)
    
    return 2 * p * r / (p + r)

