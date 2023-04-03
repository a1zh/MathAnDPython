prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primefactorisation = []


number_input = input("Enter a Number smaller than 5301678250505: ")
number_input = int(number_input)
counter = 0;

for i in range(200):
    counter = counter + 1
    if counter > len(prime_factors)-1:
        counter = 0
    if number_input % prime_factors[counter] == 0:
        primefactorisation.append(prime_factors[counter])
        number_input = number_input / prime_factors[counter]
primefactorisation.sort()

print(primefactorisation)







