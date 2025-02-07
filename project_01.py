


def gray_code(n):  
    if n == 0:  
        return ["0"]  
    if n == 1:  
        return ["0", "1"]  

    
    gray_codes = gray_code(n - 1)  
    
  
    first_half = ["0" + code for code in gray_codes]  
    
    
    second_half = ["1" + code for code in reversed(gray_codes)]  

    
    return first_half + second_half  

  
n = int(input("enter n : "))  
gray_codes = gray_code(n)  


for code in gray_codes:  
    print(code)