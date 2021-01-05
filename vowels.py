#Form a list of vowels selected from a given word
word=input("enter your sentence")
for letter in word:
     if letter in'aieou':
         print(letter,end=' ')
