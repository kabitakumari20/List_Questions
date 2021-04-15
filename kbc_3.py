questions_list=[["1.how many continenets  are there?"],["2.what is capital of india?"],["ng m kon sa course hota h?"]]
options_list=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software","2.counselling","3.tourism","4.agriculture"]]
solutions_list=[3,4,1]
lifeline_key=[["1.four","3.seven"],["1.chandigarh","4.delhi"],["1.software","2.counselling"]]
print("there is one lifeline key if you want you can use it by entering 5050")
c=0
i=0
while i<len(questions_list):
	print(questions_list[i])
	j=0
	while j<len(options_list[i]):
		print(options_list[i][j])
		j=j+1
	user=int(input("any number="))
	if user==solutions_list[i]:
		print("congress")
	elif user==5050:
		if c==0:
			print(lifeline_key[i])
			c=c+1
			user1=int(input("any number="))
			if user1==solutions_list[i]:
				print("congrets")
			else:
				print("sadly")
		else:
			print("you used lifeline key, so please enter your answer")
			user2=int(input("any number="))
			if user2==solutions_list[i]:
				print("your answer is correct")
			else:
				print("your answer is wrong")
	else:
		print("oops,your answer is wrong")
		print("quite")
	i=i+1