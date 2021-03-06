# Change these two as required.
max_word_length = 6
min_word_length = 4

word_list = set([])
f = open("words.txt", "r")

for line in f: 
    words = line.split(" ")
    for word in words:        
        word_list.add(word)

print "Words Ready!\n Enter: "
target = []

for i in range(4):
    inp = raw_input()
    target.append(list(inp))

def search(word, i, j , depth) :
    if(depth>max_word_length): return

    if(visited[i][j]): return
    visited[i][j] = 1

    if(''.join(word) in word_list and len(word)>=min_word_length):
        print ''.join(word),

    if(j!=3):
        search(word + [target[i][j+1]], i, j+1, depth+1)
    if(j!=0):
        search(word + [target[i][j-1]], i, j-1, depth+1)
    if(i!=0):
        search(word + [target[i-1][j]], i-1, j, depth+1)
    if(i!=3):
        search(word + [target[i+1][j]], i+1, j, depth+1)
    if(i!=0 and j!=0):
        search(word + [target[i-1][j-1]], i-1, j-1, depth+1)
    if(i!=3 and j!=0):
        search(word + [target[i+1][j-1]], i+1, j-1, depth+1)
    if(i!=0 and j!=3):
        search(word + [target[i-1][j+1]], i-1, j+1, depth+1)
    if(i!=3 and j!=3):
        search(word + [target[i+1][j+1]], i+1, j+1, depth+1)
    visited[i][j] = 0

for i in range(4):
    for j in range(4):
        word = [target[i][j]]
        visited = []
        for k in range(4):
            temp = [0]*4
            visited.append(temp)
        search(word, i,j,0)