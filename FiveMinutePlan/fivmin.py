#!/usr/bin/env python3
#Masaki Tanaka, 09/17/2022
import os, sys, socket, struct, subprocess, time
from termcolor import colored, cprint


def main():
	menu()

def menu():
	while(True):
		os.system('clear')
		asterisks = '*'*36
		text = colored("Ping Test Troubleshooter", 'green', attrs=['reverse','blink'])
		intro = "\t\t"+asterisks+"\n\t\t***** "+text+" *****\n\t\t"+asterisks+"\n"
		sys.stdout.write(intro)
		sys.stdout.write("\nEnter a selection:\n\n")
        sys.stdout.write("\t0 - Risk Audit Process\n")
		sys.stdout.write("\t1 - Users and Groups\n")
		sys.stdout.write("\t2 - System Configuration\n")
		sys.stdout.write("\t3 - User Activities\n")
		sys.stdout.write("\t4 - Log Analysis\n")
        sys.stdout.write("\t5 - Persistence Mechanisms\n")
        sys.stdout.write("\t6 - Forensics Tools\n")
		numbers = colored("number (0-6)", "green")
		quit = colored("\"Q/q\"", "green")
		sys.stdout.write("\nPlease enter a "+numbers+" or "+quit+" to quit the program.\t")
		command = input()
		if command.lower()=="q" :
			break
		elif command=="1":
			gateway()
		elif command=="2":
			remote()
		elif command=="3":
			dns()
		elif command=="4":
			gatewayIP = colored(default(),"yellow")
			os.system("clear")
			sys.stdout.write("Your default gateway is "+ gatewayIP+"\n")
		else:
			error = colored("invalid option","red")
			sys.stdout.write("You have entered an "+error+"!\n")
			sys.stdout.write("\nPlease enter a "+numbers+" or "+quit+" to quit the program.\t\n")
		sys.stdout.write("Press enter to continue...")
		input()
	sys.stdout.write("Quitting program, exitting to shell...\n\n")
	goodbye = colored("Goodbye! Have a nice day!\n", "green")
	sys.stdout.write(goodbye)
	time.sleep(0.75)
	os.system("clear")

"""
auditing function

hunts passwords, hunts for ssh keys,linpeas, linux smart enumaration
"""
def audit():
    sys.stdout.write("Initializing audit...\n\n")
    sys.stdout.write("Hunting for passwords...\n")
    os.system("grep --color = auto -rnw '/' -ie \"PASSWORD\" --color=always 2> /dev/null")


dict{
    0 : audit(),
     
}
