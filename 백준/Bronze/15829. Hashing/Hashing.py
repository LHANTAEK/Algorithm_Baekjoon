def hash(strings : str):
    total_str = "abcdefghijklmnopqrstuvwxyz"
    total_str_dict = {}
    H = 0
    
    for l in range(len(total_str)):
        total_str_dict[total_str[l]] = (l+1)
    
    for i in range(len(strings)):
        
        H += total_str_dict[strings[i]] * 31**i
         
    return print(H % 1234567891)

_ = input()
strings = input()

hash(strings)