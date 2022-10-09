
scores = [line.strip('\n') 
    for line in open('scores.txt', 'r').readlines()]

my_list = []
for score in scores:
    sep = score.split()
    my_list.append(sep)

for thing in my_list:
    print(thing)