#count the number of the substring in the string that the user search for it 

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count        

if __name__ == '__main__':
    string = input("enter the main string  ").strip()
    sub_string = input("enter the substring  ").strip()
    
    count = count_substring(string, sub_string)
    print(count)
