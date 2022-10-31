# Write here the code challenge solution

def isValid(s: str) -> bool:
    opening = '({[' 
    if s[0] not in opening:
        return False
    
    if len(s) % 2 !=0 or len(s) == 1:
        return False

    full = ['()','{}', '[]']          
    stack = []
    
    for ch in s:
        if ch in opening:
            stack.append(ch)
        else:
                
            if len(stack) == 0:
                return False
                
            if (stack.pop()+ch) not in full:
                return False
        
        
    return len(stack) == 0