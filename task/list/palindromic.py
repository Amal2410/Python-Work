words= ['madam','aba','bcb','hello','python']

for i in range (0,len(words)):

    left=i

    right=i

    while(left>=0 and right<len(words) and words[left]==words[right]):

        current_palindrome=words[left:right+1]
        
        print(current_palindrome)
            
        left=left-1

        right=right+1
