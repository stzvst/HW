print ("Задание 1")

age = 21
name = 'Илья'

print ('Привет, меня зовут ',name,' и мне ',age, 'год')

name_friend = input('А как зовут тебя? ')

print ('Приятно познакомиться ', name_friend)
age_friend = int(input("Сколько тебе лет? "))

if age == age_friend:
    print ("Да мы с тобой ровестники")
elif  age < age_friend:
    print ("Ты старше меня на ", age_friend - age)
else:
    print ("Я старше тебя на ", age - age_friend)