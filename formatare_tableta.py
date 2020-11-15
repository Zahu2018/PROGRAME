# Formateaza fisiere txt pt tableta la lungimea specificata

with open(filename, 'r') as f:
    lines = f.readlines()

def wrap(line):
    broken = textwrap.wrap(line, 20, break_long_words=False)
    return '\n'.join(broken)

wrapped = [wrap(line) for line in lines]


# ============================================
'''
# Alt program pt formatare tableta

with open("test.txt") as f:
    lines = f.readlines()
    max_width = 25 
    result = ""
    col = 0
    for line in lines:
        for word in line.split():
            end_col = col + len(word)
            if col != 0:
                end_col += 1
            if end_col > max_width: 
                result += '\n'
                col = 0    
            if col != 0:
                result += ' ' 
                col += 1
            result += word 
            col += len(word)
        print result
'''