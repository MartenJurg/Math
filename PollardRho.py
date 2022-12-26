import math


def FuncToApply(x, i):
	return x**2 + i


def PollardRho(input_number):
	tortoise = 0
	rabbit = 0
	gcd = 1
	i = 1

	while gcd == 1:
		tortoise = FuncToApply(tortoise, 1) % input_number
		rabbit = FuncToApply(rabbit, 1) % input_number
		rabbit = FuncToApply(rabbit, 1) % input_number
		gcd = math.gcd(abs(tortoise - rabbit), input_number)

		if gcd == input_number:
			tortoise = 0
			rabbit = 0
			gcd = 1
			i = i + 1

	return (gcd, input_number // gcd)


if __name__ == "__main__":
	print(PollardRho(1403))
