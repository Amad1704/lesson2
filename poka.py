
names=['Вася', 'Маша', 'Петя', 'Валера','Саша' , 'Даша']
# x=0

# while  x<len(names):
# 	print(names[x]) +# 	x+=1
	
def find_person(find):
	x=0
	while x<len(names):
		if names[x]=="Валера":
			print(names.pop(x) +' Нашелся')
		x+=1
		
find_person("Валера")

        										
        										