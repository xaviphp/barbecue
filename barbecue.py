barbecue = "barbecue"
# saluda a barbecue
print("Hola " + barbecue)

# barbecue es paindroma?
def isPalindrome(string):
	cont = 0
	stringLen = len(string)
	for i in range(stringLen):
		if string[i] == string[-1 * (i + 1)]:
			cont += 1

	if cont == stringLen:
		return True
	else:
		return False


if isPalindrome(barbecue):
	print(barbecue + " es palindroma!")
else:
	print(barbecue + " no es palindroma :(")


