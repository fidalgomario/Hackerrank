#!/bin/python3

if __name__ == '__main__':    
    h = int(input().strip())
    m = int(input().strip())
    mins = ""
    time = ""
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
              10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 
              17: "seventeen", 18: "eighteen", 19: "nineteen",}
    
    numby10 = ["twenty", "thirty", "forty", "fifty"]
    
    if(m == 0):
        time = str(numbers.get(h)) + " o' clock"
    
    if (m >= 1) and (m < 19):
        mins = numbers.get(m)
    elif(m >= 20 and m <= 30):
        mins = numby10[(int(m / 10)) - 2]
        if(m % 10 != 0):
            mins = mins + " " + numbers.get(m % 10)
    elif(m > 30):
        if(60 - m >= 20):
            mins = numby10[(int((60 - m) / 10)) - 2]
            if((60-m) % 10 != 0):
                mins = mins + " " + numbers.get((60-m) % 10)
        else:
            mins = numbers.get(60-m)
        
    if(m == 1):
        time = str(mins) + " minute past " + str(numbers.get(h))
    elif(m > 1 and m < 30 and m != 15):
        time = str(mins) + " minutes past " + str(numbers.get(h))
    elif(m == 15):
        time = str(mins) + " past " + str(numbers.get(h))        
    elif(m == 30):
        time = "half past " + str(numbers.get(h))
    else:
        if(h == 12 and m >= 1):
            if(60-m == 1):
                 time = str(mins) + " minute to one"
            elif(60-m == 15):
                time = str(mins) + " to one"
            else:
                 time = str(mins) + " minutes to one"

        elif(h < 12 and m >= 1):
            if(60-m == 1):
                time = str(mins) + " minute to " + str(numbers.get(h+1))
            elif(60-m == 15):
                time = str(mins) + " to " + str(numbers.get(h+1))
            else:
                time = str(mins) + " minutes to " + str(numbers.get(h+1))
                
                                              
    print(time)
