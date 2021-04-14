import hashlib
import time
import os
import cowsay
from colorama import init
from colorama import Fore, Back, Style


print()


def clear_window():

	if os.name == 'nt':
		os.system("cls")
	elif os.name == 'posfix':
		os.system("clear")


while True:

	init()

	time.sleep(1)


	print(Fore.RED +"     ..:::CYBERWARE SECURTY:::..     ")
	print("      [*]  Cyber-Hash Generator  [*]")
	print(Style.RESET_ALL)
	print()
	print(Fore.YELLOW + "github.com/cyberware-security | Instagram @antonio_gonzalez_cr")
	print()
	print("                                      Coded by Antonio Gonzalez\nV 0.2")
	print(Style.RESET_ALL)

	print()

	time.sleep(1)

	print("Choose type to hash: ")
	print()
	print("1 - MD5")
	print("2 - SHA-1")
	print("3 - SHA-224")
	print("4 - SHA-256")
	print('5 - SHA-384')
	print("6 - SHA-512")
	print("99 - To exit")
	print()


	time.sleep(1)

	x = input("Your Choose: ")

	if x == "1":
		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		md5 = hashlib.md5(passwd.encode('utf-8')).hexdigest()
		print()
		time.sleep(1)
		print("MD5 file:",md5)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED + " [!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(2)
			clear_window()


	elif x == "2":
		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		sha1 = hashlib.sha1(passwd.encode('utf-8')).hexdigest()
		print()
		time.sleep(1)
		print("SHA-1 file:",sha1)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED +"[!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(2)
			clear_window()

	elif x == "3":
		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		sha224 = hashlib.sha224(passwd.encode('utf-8')).hexdigest()
		print()
		time.sleep(1)
		print("SHA-224F file:",sha224)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED + "[!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(1)
			clear_window()

	elif x == "4":
		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		sha256 = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
		print()
		time.sleep(1)
		print("SHA-256 file:",sha256)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED + "[!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(2)
			clear_window()


	elif x == "6":
		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		sha512 = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
		print( )
		time.sleep(1)
		print("SHA-512 file:",sha512)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED + "[!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(2)
			clear_window()

	elif x == "99":
		time.sleep(1)
		print()
		print("Bye... :)")
		time.sleep(2)
		clear_window()
		break

	elif x  == '5':

		time.sleep(1)
		passwd = input("Type your path-File or word: ")
		sha384 = hashlib.sha384(passwd.encode('utf-8')).hexdigest()
		print( )
		time.sleep(1)
		print("SHA-384 file:",sha384)

		y = input("Continue? y/n: ")
		y = y.lower()

		if y == "y":
			clear_window()
			time.sleep(1)
			continue
		elif y == "n":
			print()
			print("Bye...")
			time.sleep(1)
			break

		else:
			print()
			print(Fore.RED + "[!] SyntaxxError [!]")
			print(Style.RESET_ALL)
			time.sleep(1)
			clear_window()


	else:
		time.sleep(1)
		print()
		print(Fore.RED + "[!] SyntaxxError [!]")
		print(Style.RESET_ALL)
		time.sleep(2)
		clear_window()




