import numpy as np
# matchingStrings(['yah', 'aba', 'aba', 'shm', 'shm','yah' ], ['kng', 'aba', 'yah', 'shm'])
# You can't have two keys with the same value.

def matchingStrings(strings, queries):
    matches = dict()
    matches2 = dict()
    results = []
    
    # looping through strings
    for query in queries:
        if query in matches.keys():
            matches[query] = 0
        else:
            matches2[query] = 0
        print(f' \n QUERY  -> {query} \n  \n MATCH DICT -> \n {matches} \n MATCH2 DICT ->  {matches2}' )
        # looping through queries
    #     for string in strings:
    #         # if string matches the query
    #         if string == query:
    #             matches[query] += 1
    # for match in matches.values():
    #     results.append(match)

    # print("Matches List---->", matches)
    # print(results)


# matchingStrings(['yah', 'aba', 'aba', 'shm', 'shm','yah','kng' ], ['kng', 'aba', 'yah', 'shm', 'lte', 'kng', 'hsd'])
# matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'ab', 'xzxb', 'trae'])
list1 =["lekgdisnsbfdzpqlkg", "eagemhdygyv", "jwvwwnrhuai", "urcadmrwlqe", "mpgqsvxrijpombyv", "mpgqsvxrijpombyv", "urcadmrwlqe", "mpgqsvxrijpombyv", "eagemhdygyv", "eagemhdygyv", "jwvwwnrhuai", "urcadmrwlqe", "jwvwwnrhuai", "kvugevicpsdf", "kvugevicpsdf", "mpgqsvxrijpombyv", "urcadmrwlqe", "mpgqsvxrijpombyv", "exdafbnobg", "qhootohpnfvbl", "suffrbmqgnln", "exdafbnobg", "exdafbnobg", "eagemhdygyv", "mpgqsvxrijpombyv", "urcadmrwlqe", "jwvwwnrhuai", "lekgdisnsbfdzpqlkg", "mpgqsvxrijpombyv", "lekgdisnsbfdzpqlkg", "jwvwwnrhuai", "exdafbnobg", "mpgqsvxrijpombyv", "kvugevicpsdf", "qhootohpnfvbl", "urcadmrwlqe", "kvugevicpsdf", "mpgqsvxrijpombyv", "lekgdisnsbfdzpqlkg", "mpgqsvxrijpombyv", "kvugevicpsdf", "qhootohpnfvbl", "lxyqetmgdbmh", "urcadmrwlqe", "urcadmrwlqe", "kvugevicpsdf", "lxyqetmgdbmh", "urcadmrwlqe", "lxyqetmgdbmh", "jwvwwnrhuai", "qhootohpnfvbl", "qhootohpnfvbl", "jwvwwnrhuai", "lekgdisnsbfdzpqlkg", "kvugevicpsdf", "mpgqsvxrijpombyv", "exdafbnobg", "kvugevicpsdf", "lekgdisnsbfdzpqlkg", "qhootohpnfvbl", "exdafbnobg", "qhootohpnfvbl", "exdafbnobg", "mpgqsvxrijpombyv", "suffrbmqgnln", "mpgqsvxrijpombyv", "qhootohpnfvbl", "jwvwwnrhuai", "mpgqsvxrijpombyv", "qhootohpnfvbl", "lekgdisnsbfdzpqlkg", "eagemhdygyv", "jwvwwnrhuai", "kvugevicpsdf", "eagemhdygyv", "eagemhdygyv", "lxyqetmgdbmh", "qhootohpnfvbl", "lxyqetmgdbmh", "exdafbnobg", "qhootohpnfvbl", "qhootohpnfvbl", "exdafbnobg", "suffrbmqgnln", "mpgqsvxrijpombyv", "urcadmrwlqe", "eagemhdygyv", "lxyqetmgdbmh", "urcadmrwlqe", "suffrbmqgnln", "qhootohpnfvbl", "kvugevicpsdf", "lekgdisnsbfdzpqlkg", "lxyqetmgdbmh", "mpgqsvxrijpombyv", "jwvwwnrhuai", "lxyqetmgdbmh", "lxyqetmgdbmh", "lekgdisnsbfdzpqlkg", "qhootohpnfvbl"]

list2=  ["exdafbnobg", "eagemhdygyv", "mpgqsvxrijpombyv", "kvugevicpsdf", "lekgdisnsbfdzpqlkg", "kvugevicpsdf", "exdafbnobg", "qhootohpnfvbl", "eagemhdygyv", "kvugevicpsdf", "suffrbmqgnln", "jwvwwnrhuai", "lekgdisnsbfdzpqlkg", "lekgdisnsbfdzpqlkg", "mpgqsvxrijpombyv", "jwvwwnrhuai", "kvugevicpsdf", "lekgdisnsbfdzpqlkg", "exdafbnobg", "suffrbmqgnln", "qhootohpnfvbl", "eagemhdygyv", "exdafbnobg", "suffrbmqgnln", "jwvwwnrhuai", "qhootohpnfvbl", "eagemhdygyv", "exdafbnobg", "exdafbnobg", "jwvwwnrhuai", "qhootohpnfvbl", "lxyqetmgdbmh", "qhootohpnfvbl", "suffrbmqgnln", "lxyqetmgdbmh", "qhootohpnfvbl", "eagemhdygyv", "jwvwwnrhuai", "eagemhdygyv", "qhootohpnfvbl", "mpgqsvxrijpombyv", "qhootohpnfvbl", "jwvwwnrhuai", "exdafbnobg", "eagemhdygyv", "eagemhdygyv", "kvugevicpsdf", "kvugevicpsdf", "jwvwwnrhuai", "urcadmrwlqe", "lxyqetmgdbmh", "qhootohpnfvbl", "exdafbnobg", "exdafbnobg", "eagemhdygyv", "qhootohpnfvbl", "exdafbnobg", "exdafbnobg", "lekgdisnsbfdzpqlkg", "jwvwwnrhuai", "eagemhdygyv", "urcadmrwlqe", "kvugevicpsdf", "lekgdisnsbfdzpqlkg", "jwvwwnrhuai", "eagemhdygyv", "lekgdisnsbfdzpqlkg", "exdafbnobg", "kvugevicpsdf", "jwvwwnrhuai", "exdafbnobg", "lxyqetmgdbmh", "exdafbnobg", "lxyqetmgdbmh", "jwvwwnrhuai", "mpgqsvxrijpombyv", "eagemhdygyv", "urcadmrwlqe", "kvugevicpsdf", "qhootohpnfvbl", "jwvwwnrhuai", "eagemhdygyv", "urcadmrwlqe", "urcadmrwlqe", "exdafbnobg", "qhootohpnfvbl", "exdafbnobg", "eagemhdygyv", "exdafbnobg", "jwvwwnrhuai", "eagemhdygyv", "jwvwwnrhuai", "mpgqsvxrijpombyv", "urcadmrwlqe", "urcadmrwlqe", "eagemhdygyv", "eagemhdygyv", "jwvwwnrhuai", "suffrbmqgnln", "eagemhdygyv"]

out = [9,8,16,10,9,10,9,14,8,10,4,10,9,9,16,10,10,9,9,4,14,8,9,4,10,14,8,9,9,10,14,9,14,4,9,14,8,10,8,14,16,14,10,9,8,8,10,10,10,11,9,14,9,9,8,14,9,9,9,10,8,11,10,9,10,8,9,9,10,10,9,9,9,9,10,16,8,11,10,14,10,8,11,11,9,14,9,8,9,10,8,10,16,11,11,8,8,10,4,8]

print("___________________________")

npArray1 = np.array(list1)
newArray1 = np.unique(npArray1)
list_unique_count1 = len(newArray1)
print(newArray1)
print(list_unique_count1)

print("___________________________")

npArray2 = np.array(list2)
newArray2 = np.unique(npArray2)
list_unique_count2 = len(newArray2)
print(newArray2)
print(list_unique_count2)


npOutPut = np.array(list1)
newNpOutPut  = np.unique(npOutPut)
list_output = len(newNpOutPut)
print("--->", newNpOutPut)
print("ouut --->", list_output)


print("Len of output --->", len(out))


matchingStrings(list1, list2)