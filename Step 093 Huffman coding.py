class Tree(object):
    def __init__(self, letters=None, weight=None, left=None, right=None):
        self.left = left
        self.right = right
        self.letters = letters if letters else left.letters + right.letters
        self.weight = weight if weight else left.weight + right.weight

    def __repr__(self):
        return '{letter} : {weight}'.format(letter=self.letters, weight=self.weight)


def get_code(letter, tree):
    if tree.letters == letter:
        return '0'
    elif letter in tree.left.letters:
        return '0' + [get_code(letter, tree.left), ''][tree.left.letters == letter]
    else:
        return '1' + [get_code(letter, tree.right), ''][tree.right.letters == letter]


string = input()
trees = [Tree(letters=w, weight=string.count(w)) for w in set(string)]
while len(trees) > 1:
    trees.sort(key=lambda tree: tree.weight)
    trees.append(Tree(left=trees.pop(0), right=trees.pop(0)))

tree = trees[0]
codes = {letter: get_code(letter, tree) for letter in tree.letters}
encoded = ''.join([codes[letter] for letter in string])

print(len(tree.letters), len(encoded))
for letter, code in codes.items():
    print('{letter}: {code}'.format(letter=letter, code=code))
print(encoded)
