import math


def PollardPMinus1(input_number):
	gcd = 1
	power = 2
	new_number = 2
	
	
	while gcd == 1:
		new_number = (new_number**power) % input_number
		power = power + 1
		gcd = math.gcd((new_number - 1), input_number)
		if gcd > 1:
			break
	
	return(gcd, input_number // gcd)


if __name__ == "__main__":
	print(PollardPMinus1(1403))
