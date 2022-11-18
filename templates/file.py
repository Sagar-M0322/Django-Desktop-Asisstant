from collections import Counter


c = 0
count = 0
arr = []
file_name = 'C:/Users/Sagar/Desktop/file.txt'
fre = {}
#m = {}
wd = input("enter a word")
with open('C:/Users/Sagar/Desktop/file.txt', 'r') as file:

    for line in file:
        wds = line.split()
        count = count + len(wds)

        for i in wds:
            if(i == wd):
                c = c+1
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1

    print("occurence of the word:", c)
    print("the frequency of chatecters is " + str(fre))

    print("total number of words in the file:"+str(count))


def search(file_name, string_to_search):
    lnum = 0
    lres = []
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            lnum += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in wd:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    lres.append((string_to_search, lnum, line.rstrip()))
        # Return list of tuples containing matched string, line numbers and lines where string is found
    return lres


matched_lines = search(file_name, [wd])
print("total num of lines in the file", len(matched_lines))
for ele in matched_lines:
    print('Word = ', ele[0], ' :: Line Number = ',
          ele[1], ' :: Line = ', ele[2])
