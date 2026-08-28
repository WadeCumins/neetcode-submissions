from typing import List

def read_integers() -> List[int]:
    ans = input().split(',')
    fin = []
    for i in ans:
        fin.append(int(i))
    return fin
    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
