print ('Задание 2')

seconds = int(input("Введите случайное число "))

hours = seconds // (60*60)
print (hours,'часов')

minutes = (seconds - hours*(60*60)) // 60
print (minutes, "минут")

seconds = (seconds - ((hours*(60*60) + minutes*60)))
print (seconds, 'секунд')

print ('%02d : %02d : %02d  ' % (hours,minutes,seconds) )


