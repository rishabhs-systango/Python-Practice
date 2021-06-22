def recursive_fun(count) :
    print('recursive called')
    count = count -1
    if count > 0 :
        recursive_fun(count)
recursive_fun(3)