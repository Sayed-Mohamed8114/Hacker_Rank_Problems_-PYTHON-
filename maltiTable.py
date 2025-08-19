# using only the math basics calculate the maltiplication table 

if __name__ == '__main__':
    n = int(input().strip())

    for i in range(11):
        if i==0:
            continue
        else:
          print(f'{n} x {i} = {n*i}')