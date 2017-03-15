class Tree(object):
    def __init__(self, letters=None, weight=None, left=None, right=None):
        self.left = left
        self.right = right
        self.letters = letters if letters else left.letters + right.letters
        self.weight = weight if weight else left.weight + right.weight

    def __repr__(self):
        return '{letter} : {weight}'.format(letter=self.letters, weight=self.weight)

# string = input()
string = 'abacabad'
# string = 'a'
# string = 'ab'
trees = [Tree(letters=w, weight=string.count(w)) for w in set(string)]
# print(trees)
while len(trees) > 1:
    trees.sort(key=lambda tree: tree.weight)
    # print(trees)
    trees.append(Tree(left=trees.pop(0), right=trees.pop(0)))

tree = trees[0]


def get_code(letter, tree):
    if tree.letters == letter:
        return '0'  # one letter in string
    elif letter in tree.left.letters:
        return '0' + [get_code(letter, tree.left), ''][tree.left.letters == letter]
    else:
        return '1' + [get_code(letter, tree.right), ''][tree.right.letters == letter]


codes = {letter: get_code(letter, tree) for letter in tree.letters}
# print(codes)

encoded = ''.join([codes[letter] for letter in string])
# print(encoded)

# print("Output")
print(len(tree.letters), len(encoded))
for letter, code in codes.items():
    print('{letter}: {code}'.format(letter=letter, code=code))
print(encoded)
