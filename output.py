with open('b.txt', 'r', encoding="utf8") as file1:
    with open('a.txt', 'r', encoding="utf8") as file2:
        difference = set(file1).difference(file2)

difference.discard('\n')

with open('d.txt', 'w', encoding="utf8") as fileoutput:
    for line in difference:
        fileoutput.write(line)
