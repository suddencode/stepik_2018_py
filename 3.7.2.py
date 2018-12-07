inputAlphabet, inputSecure, needToEncrypt, needToDecrypt = input(), input(), input(), input()
myDict1 = dict(zip(inputAlphabet, inputSecure))
myDict2 = {v:k for k, v in myDict1.items()}
for i in range(len(needToEncrypt)):
    print(myDict1[needToEncrypt[i]], end='')
print('')
for i in range(len(needToDecrypt)):
    print(myDict2[needToDecrypt[i]], end='')
