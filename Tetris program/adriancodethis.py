
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

#For a given score compare against 2nd index of all values. If it finds that given score is larger than a number.
#Rewrite insert score into that position with name, then rewrite the list.
#Write new list into score.txt
for thing in my_list:
    print(thing)



#with open('scores.txt', 'w') as f:
#    for lines in lines:
#        f.write(f"{line}/n")


#this thing below
###################################
#writescores = open('scores.txt', 'w')
#count = 1
#for thing in my_list: 
#    writescores.write("%d %s %s" %count %thing[1] %thing[2])

#Double check
#    if count == 10:
#        break
#    count += 1