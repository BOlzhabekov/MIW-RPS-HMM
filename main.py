import numpy as np

last_record = 0


def recs_2_str(order):
    arr_1 = []
    for i in order:
        if i == 0:
            arr_1.append("R")
        elif i == 1:
            arr_1.append("P")
        else:
            arr_1.append("S")
    return arr_1


def str_2_recs(order):
    arr_2 = []
    for i in order:
        if i == "R":
            arr_2.append(0)
        elif i == "P":
            arr_2.append(1)
        elif i == "S":
            arr_2.append(2)
        else:
            print("Error. Try again")
    return arr_2


def get_probs(quants):
    t_1 = np.array(quants)
    for i in range(3):
        equation = t_1[i, :] / sum(t_1[i])
        t_1[i] = equation
    return t_1



def update_amount(amount):
    global last_record
    for i in range(last_record, len(order) - 1):
        last_record = i + 1
        if order[i] == 0:
            amount[0][order[i + 1]] = amount[0][order[i + 1]] + 1
        elif order[i] == 1:
            amount[1][order[i + 1]] = amount[1][order[i + 1]] + 1
        else:
            amount[2][order[i + 1]] = amount[2][order[i + 1]] + 1
    return amount


order = [
    "P", #DRAW
    "P", #I WON
    "S", #VOVA WON
    "R", #DRAW
    "S", #DRAW
    "P", #I WON
    "R", #DRAW
    "R", #VOVA WON
    "P", #VOVA WON
    "S", #I WON
    "S", #DRAW
    "S", #DRAW
    "R", #VOVA WON
    "P", #I WON
    "S", #I WON
    "S", #I WON
    "S", #DRAW
    "P", #DRAW
    "R", #VOVA WON
    "R" #I WON
]
order = str_2_recs(order)

n = 20

t1 = ["R", "P", "S"]
t2 = [0, 1, 2]

amount = np.zeros((3, 3))
amount = update_amount(amount)
my_last_choice = order[-1]
p_t1 = get_probs(amount)
print(recs_2_str(order))
my_score = 0
comp_score = 0
msg = '\n'
print("Here we go!")

while True:

    my_choice = input(" ")#SHOULD ONLY WRITE IN UPPERCASE. GOAL - LATER CREATE AN EXCEPTION CATCHER AND MAKE IT UMDERSTAND LOWERCASE
    order.append(str_2_recs([my_choice])[0])
    comp_guess_choice = np.random.choice(t1, p=p_t1[my_last_choice])


#   COUNTER CHOICE FROM COMPUTER | CLUSTER
    comp_choice = None
    if comp_guess_choice == "R":
        comp_choice = "P"
    elif comp_guess_choice == "P":
        comp_choice = "S"
    else:
        comp_choice = "R"
#   COUNTER CHOICE FROM COMPUTER | CLUSTER




    if comp_choice == my_choice:
        msg = '\nDRAW'
        comp_score = comp_score + 1
        my_score = my_score + 1
    else:
        if comp_choice == "R":
            if my_choice == "P":
                my_score = my_score + 1
                msg = 'I won!'
            else:
                comp_score = comp_score + 1
                msg = 'Comp won!'
        elif comp_choice == "P":
            if my_choice == "S":
                my_score = my_score + 1
                msg = 'I won!'
            else:
                comp_score = comp_score + 1
                msg = 'Comp won!'
        else:
            if my_choice == "R":
                my_score = my_score + 1
                msg = 'I won!'
            else:
                comp_score = comp_score + 1
                msg = 'Comp won!'

    print(msg)
    print(f"\n Comp had: {comp_choice}  "
          f"\n Now comp score: {comp_score} "
          f"\n You had: {my_choice} "
          f"\n Now your score: {my_score}")
    print("\n Let's continue")
    my_last_choice = order[-1]

    amount = update_amount(amount)
    p_t1 = get_probs(amount)

