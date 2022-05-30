indics = []
for i, ele in enumerate(line):
    if ele == '\t':
        indics.append(i)
line = list(line)
for i in indics:
    line[i] = "###"
line = ''.join(line)
print(line)