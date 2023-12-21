file = open("h.txt", 'r')
replacing = {"nine": '9',
             "eight": '8',
             "seven": '7',
             "six": '6',
             "five": '5',
             "four": '4',
             "three": '3',
             "two": '2',
             "one": '1'}

final_numbers = []

for line in file:
    start = 0
    end = 0
    numbers = ""
    stop_start = 1
    stop = 1
    # start
    for i in range(len(line)):
        if stop_start == 1:
            for each in replacing: #turn words to nums
                if each in str(line)[0:i+1]:
                    numbers += str(replacing[each])
                    stop_start = 0
                    break
                if line[i].isnumeric():
                    numbers += str(line[i])
                    stop_start = 0
                    break
    #end
    for i in range(len(line), -1, -1):
        if stop == 1:
            for each in replacing:  # turn words to nums
                if each in str(line)[i-2:len(line)]:
                    numbers += str(replacing[each])
                    stop = 0
                    break
                if line[i-2].isnumeric():
                    numbers += str(line[i-2])
                    stop = 0
                    break
    final_numbers.append(numbers)

counter = 0
for i in final_numbers:
    print(i)
    counter += int(i)
print(counter)