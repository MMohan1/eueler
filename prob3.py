def prime_fac(n):
	flag=1
	list1=[]
	for i in range(2,n+1):
		if n%i==0:
			for j in range(2,int(i**0.5)+1):
				if i%j==0:
					flag=0
					break
			if flag:
				list1.append(i)
	if list1:
		print max(list1)
	else:
		print 'empty'
				 
				 
''' thanks VARUNPARTAP SINGH for this superab logic'''
def largest_prime():

  num = 100

  new_num = num

  largest_prime = 0

  counter = 2

  while(counter * counter <= new_num):

    if(new_num%counter ==0):

      new_num = new_num / counter

      largest_prime = counter

    else:

      counter += 1

  if new_num > largest_prime:

    largest_prime = new_num

  print largest_prime



if __name__ == '__main__':

  largest_prime()
