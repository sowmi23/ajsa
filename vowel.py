var=input()
lis=['a','e','i','o','u']
key=['!','@','#','$','%','^','&','*','(',')']

if var in lis:
	print("Vowel")
elif var in key:
	print("invalid")
else:
	print("Consonant")
