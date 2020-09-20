import argparse
import sys
import random
import string
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("n",help="Number of passwords you'd like to generate")
	parser.add_argument("min",help="minimum length of password",type=int)
	parser.add_argument("max",help="maximum length of password",type=int)
	data = parser.parse_args()
	letters = string.ascii_letters
	passwords = list()
	for _ in range(int(data.n)):
		passwords.append(''.join(random.choices(letters,k=random.randint(data.min,data.max))))

	filehandle = open("passwords.txt",'a')
	for pw in passwords:
		filehandle.write(pw+"\n")
	filehandle.close()



if __name__ == "__main__":
	main()