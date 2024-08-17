def solution(num_list, n):
    answer = [[]]
    import numpy as np
    num_list_array = np.array(num_list)
    num_list_array = np.reshape(num_list_array, (len(num_list)//n, n))
    answer = num_list_array.tolist()
    return answer
