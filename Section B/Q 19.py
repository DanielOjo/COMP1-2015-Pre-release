#Daniel Ogunlana
#01/05/15
#Section B

ISBN = []

for Count in range(1,13):
    print("Please enter next digit of ISBN")
    ISBN.append(int(input()))
    #ISBN = int(input())

CalculatedDigit = 0
Count = 0

while Count <13:
    CalculatedDigit = CalculatedDigit +ISBN[Count]
    Count = Count + 1
    CalculatedDigit = CalculatedDigit + (ISBN[Count] *3)
    Count = Count + 1

while CalculatedDigit >= 10:
    CalculatedDigit = CalculatedDigit -10

CalculatedDigit = 10 - CalculatedDigit

if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == ISBN[13]:
    print("Valid ISBN")
