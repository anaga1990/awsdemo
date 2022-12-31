name = 'nagarjuna';

myset = set()
for ch in name:
   # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
   if ch in 'aeiou':
        myset.add(ch)

print(sorted(myset))