def merge_the_tools(string, k):
    n =len(string) // k
    for i in range(n):
        substring =string[i*k:(i+1)*k]
        seen=set()
        result=[]
        
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
                
        print(''.join(result))
   
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)