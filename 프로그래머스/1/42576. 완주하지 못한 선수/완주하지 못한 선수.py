def solution(participant, completion):
    answer = ''
    participant_dict = {}
    
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1
            
    for complete_name in completion:
        participant_dict[complete_name] -= 1
        
    for i in participant:
        if participant_dict[i] == 1:
            answer = i
    return answer