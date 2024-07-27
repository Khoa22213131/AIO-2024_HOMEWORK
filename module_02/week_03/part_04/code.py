# ########################
# Create data
# ########################
import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


train_data = create_train_data()
print(train_data)


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(
            train_data[train_data[:, -1] == y_unique[i]]) / len(train_data)

    return prior_probability


prior_probablity = compute_prior_probablity(train_data)
print("P(play tennis = No) =", prior_probablity[0])
print("P(play tennis = Yes) =", prior_probablity[1])


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        print(x_unique)
        x_conditional_probability = []
        for j in range(len(x_unique)):
            tmp = []
            for k in range(len(y_unique)):
                tmp.append(len(train_data[(train_data[:, i] == x_unique[j]) & (
                    train_data[:, -1] == y_unique[k])])/len(train_data[train_data[:, -1] == y_unique[k]]))
            x_conditional_probability.append(np.array(tmp))

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


def get_index_from_value(feature_name, list_features):
    count = -1
    for i in list_features:
        count += 1
        if feature_name == i:
            return count


outlook = list_x_name[0]
print(outlook)
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny' | 'Play Tennis'='Yes') =",
      np.round(conditional_probability[0][x1][1], 2))

x2 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny' | 'Play Tennis'='No') =",
      np.round(conditional_probability[0][x2][0], 2))


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    p0 = 0
    p1 = 0
    for i in range(0, 2):
        p = prior_probability[i]
        p *= conditional_probability[0][x1][i]
        p *= conditional_probability[1][x2][i]
        p *= conditional_probability[2][x3][i]
        p *= conditional_probability[3][x4][i]
        if i == 0:
            p0 = p
        else:
            p1 = p

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1
    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability,
                              conditional_probability)
if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
