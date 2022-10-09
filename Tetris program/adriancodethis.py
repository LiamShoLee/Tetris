
scores = [line.strip('\n') 
    for line in open('scores.txt', 'r').readlines()]

my_list = []
for score in scores:
    sep = score.split()
    my_list.append(sep)

#For a given score compare against 2nd index of all values. If it finds that given score is larger than a number.
#Rewrite insert score into that position with name, then rewrite the list.
#Write new list into score.txt
for thing in my_list:
    print(thing)