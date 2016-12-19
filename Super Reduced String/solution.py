if __name__ == '__main__':
    s = input()
    
    while(True):
        init = len(s)
        
        for i in range(0,len(s)-1):
            if(s[i] == s[i+1]):
                s = s[:i] + s[i+2:]
                break
        if(init == len(s)):
            break
    
    if(len(s)==0):
        print("Empty String")
    else:
        print(s)    
