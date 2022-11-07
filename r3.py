def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    for line in lines:
        s = line.split(' ')
        time = s[0][:5]
        name = s[0][5:]
        print(name)
        

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('3.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)


main()