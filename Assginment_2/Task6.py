# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def calculate_earningd():
    n= int(input())
    shoe_sizes =list(map(int,input().split()))
    m = int(input())
    
    inventory =Counter(shoe_sizes)
    total_money =0
    
    for _ in range(m):
        size,price= map(int,input().split())
        if inventory[size]>0:
            total_money +=price
            inventory[size] -=1
            
    print(total_money)
    
if __name__ == '__main__':
    calculate_earningd()

