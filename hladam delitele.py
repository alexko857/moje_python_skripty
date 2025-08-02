def hladam_delitele(number):
    delitele = []
    for i in range(1,number+1):
        if number%i==0:
            delitele.append(i)
    return delitele
print(hladam_delitele(24))
def deletiele(number):
    return [x for x in range(1,number) if number %x==0]
def is_perfect(number):
    return sum(deletiele(number))==number
print(is_perfect(6))
