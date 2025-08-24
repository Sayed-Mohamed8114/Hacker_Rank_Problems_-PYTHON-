if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result=[
        [i,j,k] for i in range(x+1)
                for j in range(y+1)
                for k in range(z+1)
                if i+j+k != n  
    ] 
    print(result)
    
# gave you all the possible lists of x y z that if we sum the x and y and z in it , the sum != n