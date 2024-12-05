def solution(a, b, c, d):
    answer = 0
    list = [a,b,c,d]
    list.sort()
    
    if(list[0] == list[3]):
        answer = 1111 * list[0]
        
        
    elif((list[0] != list[1] == list[2] == list[3])):
        answer = (10 * list[1] + list[0]) ** 2
    elif((list[0] == list[1] == list[2] != list[3])):
        answer = (10 * list[1] + list[3]) ** 2
        
        
    elif((list[0] == list[1]) and (list[2] == list[3]) and (list[1] != list[3])):
        answer = (list[0] + list[2]) * abs(list[2] - list[0])
        
        
    elif((list[0] == list[1]) and (list[2] != list[3])):
        answer = list[2] * list[3]
        
    elif((list[0] != list[1]) and (list[2] == list[3])):
        answer = list[0] * list[1]
        
    elif((list[0] != list[1]) and (list[2] != list[3]) and list[1] == list[2]):
        answer = list[0] * list[3]
        
        
        
    else: answer = list[0]
    
    
    return answer