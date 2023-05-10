def bakshali_sqrt(n,m):
    start = 0
    while start**2 < n:
        start += 1
    start -= 1
    def correct(guess,times):
        if times == 0:
            return guess
        correction = (n - guess**2)/(2*guess)
        refinement = (correction**2)/(2*(guess + correction))
        new_guess = guess + correction - refinement
        return correct(new_guess,times-1)
    return correct(start,m)

def madhava_pi(n,m):
    sum = 0
    for k in range(n):
        sum += ((-3)**(0-k))/(2*k + 1)
    return sum * (bakshali_sqrt(12,m))


π = (madhava_pi(99,9))

def circarea(r):
    return π * (r**2)

def hypoteneuse(a,b):
    return bakshali_sqrt(a**2+b**2,9)

