string = input()
cro_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for cro_alphabet in cro_alphabets:
    if string.find(cro_alphabet) != -1:
        while True:
            string = string.replace(cro_alphabet, ' ', 1)
            cnt += 1
            if string.find(cro_alphabet) == -1:
                break
print(cnt+len(string.replace(' ', '')))
