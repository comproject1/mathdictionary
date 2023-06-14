input_text = Element("input_text")
output_text = Element("output_text")
output_text01=Element("output_text01")

def function_add_text(*args):
    n=int(input_text.value)
    num=[n]
    res=1
    while(n!=2):
        if (n%2==0):
            n=n//2
            res+=1
            num.append(n)
        else:
            n=3*n+1
            res+=1
            num.append(n)
    num.append(1)
    output_text.element.innerText=f"{num}"  
    output_text01.element.innerText=f"{res}번 반복했습니다."
    input_text.clear()