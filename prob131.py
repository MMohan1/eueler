'''This is a problem that would drive a person insane if they tried to brute force a solution; even though the search area is (relatively for a Project Euler problem) small. This problem has a very elegant solution as long as you know how to break down the problem to it’s base components. Writing the problem out gives us n3+n2p=y3 which we can rearrange to look like n2(n+p)=y3. Playing with a few values leads us to the conclusion that both n2 and (n+p) have to be cubes. This makes p a difference of cubes such that (a+1)3–a3=p

So we take this new knowledge and figure out when (a+1)3–a3 becomes greater than 1,000,000 and find that this happens around a = 577. This means that we just put the numbers from 1 to 577 into our difference of squares equation and count which ones return a prime. '''
def is_prime(n):
	flag = 1
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			flag = 0
			break
	if flag:
		return True
	else:
		return False 

def prob131():
	list1 = []
	for i in range(1, 578):
		x = (i+1)**3 - i**3
		if is_prime(x):
			list1.append(x)
	print list1
	print len(list1)
if __name__ == '__main__':
	prob131()
