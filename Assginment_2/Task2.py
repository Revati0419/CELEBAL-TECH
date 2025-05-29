def average(array):
   
    distinct =set(array)
    length= len(distinct)
    
    result = sum(distinct)/length
    return round(result,3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)