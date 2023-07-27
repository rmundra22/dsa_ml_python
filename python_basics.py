import collections

def main():
    # ALL ABOUT SETS --------------------------------------------------
    list_of_days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
    setA = set(list_of_days)
    print(setA)
    
    setA.add("today") 
    print(setA)
    setA.discard("Mon")
    print(setA)
    
    setD = setA - set(["Mon","Tue"])
    print(setD)
    
    daysA = set(["Mon","Tue","Wed"])
    daysB = set(["Wed","Thu","Fri","Sat","Sun"])
    print(daysA & daysB) # intersection
    print(daysA | daysB) # union
    
    SubsetRes = daysA <= daysB
    SupersetRes = daysB >= daysA
    print(SubsetRes)
    print(SupersetRes)
    
    list_of_days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
    setA = set(list_of_days)
    SubsetRes = daysA <= setA
    SupersetRes = setA >= daysA
    print(SubsetRes)
    print(SupersetRes)
    
    # DELETING ELEMENTS ------------------------------------------------
    listA = [1, 2, 3]
    del listA[0]
    print(listA)
    
    tupleA = (1, 2, 3)
    print(tupleA)
    del tupleA
    # print(tupleA)
    
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary
    
    # Maps (Chain Maps can be used as stacks) -------------------------
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    res = collections.ChainMap(dict1, dict2)
    # Creating a single dictionary
    print(res.maps,'\n')
    
    print('Keys = {}'.format(list(res.keys())))
    print('Values = {}'.format(list(res.values())))
    
    # using chain maps as stacks of dictionary (reordering of dicts)
    res1 = collections.ChainMap(dict1, dict2)
    print(res1.maps,'\n')
    res2 = collections.ChainMap(dict2, dict1)
    print(res2.maps,'\n')
    
    # updating chain maps
    dict2['day4'] = 'Fri'
    print(res.maps,'\n')
    res['day1'] = 1 # update value of first key
    print(res.maps,'\n')
    
    print(res['day1'])
    
    return 0

if __name__ == "__main__":
    main()