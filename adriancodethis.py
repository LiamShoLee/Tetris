
scores = [line.strip('\n') 
    for line in open('scores.txt', 'r').readlines()]

my_list = []

top_score = 6000
count = 1
for score in scores:
    sep = score.split()
    if int(sep[2]) < top_score:
        new_score = [count,"New Player", top_score]
        my_list.append(new_score)
        count += 1
        my_list.append([count, sep[1], sep[2]])
        top_score = -1
    else:
        my_list.append([count, sep[1], sep[2]])
    
    if count == 10:
        break
    count += 1

<<<<<<< HEAD:Tetris program/adriancodethis.py
#For a given score compare against 2nd index of all values. If it finds that given score is larger than a number.
#Rewrite insert score into that position with name, then rewrite the list.
#Write new list into score.txt

=======
f = open("scores.txt", "w")
f.close()
f = open("scores.txt", "a")
for num in range(10):
    f.write(str(num) + " " + my_list[num][1] + " " + str(my_list[num][2])+"\n")
f.close()

for thing in my_list:
    print(thing)
>>>>>>> 87c7257f95da5ce065c9e9c844c6f5b73c59548c:adriancodethis.py
