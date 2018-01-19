S_TYPE = 'S'
L_TYPE = 'L'

def buildTypeMap(string):
    type_map = [0]*(len(string) + 1)
    #empty suffix at end of string is S type by definition
    type_map[-1] = S_TYPE
    #suffix containing last character of string is L type
    type_map[-2] = L_TYPE
    string_length = len(string)
    for i in range(2, string_length + 1):
        print(string[string_length - i])
        if string[string_length - i + 1] < string[string_length - i]:
            type_map[string_length - i] = L_TYPE
        elif string[string_length - i  + 1] > string[string_length - i]:
            type_map[string_length - i]  =  S_TYPE
        else:
            type_map[string_length - i] = type_map[string_length - i + 1]

    return type_map

    
print(''.join(buildTypeMap('cabbage')))
