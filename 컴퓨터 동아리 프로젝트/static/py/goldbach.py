
input_text = Element("input_text")
output_text = Element("output_text")

def function_add_text(*args):
  n=int(input_text.value)
  if (n<=3) or (n>1000000) or (n%2 !=0):
    output_text.element.innerText = "조건에 맞지 않는 수입니다."
  else:
    check = [False, False] + [True] * 1000000
    
    for i in range(2, 1001):
      if check[i] == True:
        for j in range(i + i, 1000001, i):
            check[j] = False
    a=n//2
    b=n//2
    for _ in range(1000000):
      if check[a] and check[b]:
        output_text.element.innerText = f"{a} + {b} = {n}"
        break
      a-=1
      b+=1
  input_text.clear()