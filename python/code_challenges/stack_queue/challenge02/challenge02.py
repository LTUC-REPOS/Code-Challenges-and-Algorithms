# Write here the code challenge solution

def isValid(s: str) -> bool:
    opening = '({[' 
    closings = ')}]'
    if s[0] not in opening:
        return False
    
 

    full = ['()','{}', '[]']          
    stack = []
    
    for ch in s:
        if ch not in opening and ch not in closings:
            continue
            
        if ch in opening:
            stack.append(ch)
        else:
                
            if len(stack) == 0:
                return False
                
            if (stack.pop()+ch) not in full:
                return False
        
        
    return len(stack) == 0
