text="qwertyuioplkjhgfdsazxcvbnm"

vowels="aeiou"

v_count=0

for ch in text:

    if vowels.count(ch)!=0:
        
        v_count+=1

print(v_count)



