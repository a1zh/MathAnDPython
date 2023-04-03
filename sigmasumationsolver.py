#Σ Summation Formulas and Sigma Notation Examples:

#n(index of Summation)
#k(last Index Value)
#i(n) function depending on the index(k)

# [1] n/kΣc = c*n


def sigma_sum_constant(c,k):
    sum = c * k
    print(sum)

#Example: 4/1 Σ 8 = c*k = 4 * 8       
#sigma_sum_constant(8,4)

#example k=8, n=1, c = 7
#sigma_sum_constant(8,7)

#example k=5, n=1, c = 9
#sigma_sum_constant(5,9)



# [2] k/nΣ i = c*Σ*i(n) 


def sigma_sum_withVariable_noformula(c,k,n,i):
    sum1 = 0
    for s in range(k):
        if hasattr(i, '__call__'):
            sum1 = sum1 + i(n)
            n = n+1
        else:
            i = 1
            n = n * i
            sum1 = sum1 + n
            n = n + 1
    sum1 = sum1*c
    print(sum1)

# Example: k=5 n=1 Σ i = 1 + 2 + 3 + 4 + 5 = 15
#sigma_sum_withVariable_noformula(1,5,1,1)

# Example: k=4 n=1 Σ c*i = c*Σ = 6*(1 + 2 + 3 + 4) = 60
#sigma_sum_withVariable_noformula(6,4,1,1)

# Example: k=4 n=1 Σ c*[7*i-3] = 90

#integrate as parameter for i
def example_func_i(i):
    i = ((7*i)-3)
    return i

#sigma_sum_withVariable_noformula(1, 5, 1, example_func_i)



#[3] k/nΣ i = k(k+1)/2


def sigma_sum_withVariable_withformula(c,k,n,i):
    i = i
    sum2 = (((k*(k+1))*(1/2))*c)
    print(sum2)

#Example: k=4 n=1 Σ c*i = c*Σi = c*(k(k+1))/2

#sigma_sum_withVariable_withformula(6,4,1,1)



#[4] k/nΣ i => i = (k(k+1)/2) => c*Σi - Σ*c


def sigma_sum_withVariable_withFormulaWithFunction(k,i,n,c=None):
    sum1 = 0
    for s in range(k):
        if hasattr(i, '__call__'):
            sum1 = i((((k*(k+1))*(1/2))),k)
        else:
            i=1
            sum1 = (((k*(k+1))*(1/2))) * c
    print(sum1)

#integrate as parameter for i
#Example: k=5 n=1 i=[7i-3] => 7Σi - Σc => 7*(k(k-1)/2) -3*k =  90
def example_func_i2(i,k):
    i = ((7*i)-3*k)
    return i

#sigma_sum_withVariable_withFormulaWithFunction(5,example_func_i2,1)




#Practive Examples:

#example k=4, n=1, c=6, i=1
#sigma_sum_withVariable_withFormulaWithFunction(4,1,1,6)

#example k=8, n=1, c=1, i=[9i+7]

#integrate as parameter for i
def example_func_i3(i,k):
    i = ((9*i)+(7*k))
    return i

sigma_sum_withVariable_withFormulaWithFunction(8,example_func_i3,1)
