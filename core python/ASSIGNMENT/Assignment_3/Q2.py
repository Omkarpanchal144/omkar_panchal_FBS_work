#2. Write a program to input any alphabet and check whether it is vowel or consonant.

a=input("Enter the Alphabet :-") ### ONLY ALPHABET AND ONLY CAPITAL
Vowel="A,E,I,O,U"
Consonant="""B, C, D, F, G, H, J, K, L, M, N,
P, Q, R, S, T, V, W, X, Y, Z"""

if(a in Vowel and Consonant):
    print("It is a Vowel.")
else:
    print("It is a Consonant.")