s = input()
dial = {
    'ABC': 3, 'DEF': 4, 'GHI': 5,
    'JKL': 6, 'MNO': 7, 'PQRS': 8,
    'TUV': 9, 'WXYZ': 10
}
time = 0
for alpa in s:
    for key,value in dial.items():
        if alpa in key:
            time = time + value
            break
        
        
        
print(time)