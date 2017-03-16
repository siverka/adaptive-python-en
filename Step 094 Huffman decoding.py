k = int(input().split()[0])
codes = [input().split(': ') for _ in range(k)]
codes.sort(key=lambda code: code[1])
encoded = input()

decoded = ''
while encoded:
    for letter, code in codes:
        if encoded[:len(code)] == code:
            decoded += letter
            encoded = encoded[len(code):]
            break

print(decoded)
