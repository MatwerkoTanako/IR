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
		sys.stdout.write("\t1 - Test connectivity to your gateway.\n")
		sys.stdout.write("\t2 - Test for remote connectivity.\n")
		sys.stdout.write("\t3 - Test for DNS resolution.\n")
		sys.stdout.write("\t4 - Display gateway IP adddress.\n")
		numbers = colored("number (1-4)", "green")
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


def default():
	# printing for troubleshooting
	sys.stdout.write("Obtaining Default Gateway... : ")
	with open("/proc/net/route") as nr:
		for l in nr:
			fields = l.strip().split()
			#error handling
			if fields[1] != '00000000' or not int(fields[3],16)&2:
				continue
			gatewayIP = socket.inet_ntoa(struct.pack("<L", int(fields[2],16)))
			if type(gatewayIP)==type(None):
				sys.stdout.write("Cannot determine default gateway... defaulting to loopback adddress...\n")
				gatewayIP = "127.0.0.1"
			return gatewayIP

def inform(response):
	#default response message at end of command
	sys.stdout.write("\nPlease inform your system administrator that the test was "+response+"!\n\n")
	

def success():
	#success message
	success = colored("SUCCESSFUL", "yellow")
	inform(success)

def failure():
	#failure message
	failure = colored("A FAILURE", "red")
	inform(failure)

def ping(host):
	try:
		response = subprocess.check_output(["ping", "-c", "4", "host"], stderr = subprocess.STDOUT,universal_newlines = True)
		success()
	except:
		failure()

def gateway():
	os.system('clear')
	sys.stdout.write("Testing Connectivity to your gateway...\n\n")
	#getting dns from system
	gatewayIP = default()	
	if type(gatewayIP)==type(None):
		sys.stdout.write("Cannot determine default gateway... defaulting to loopback adddress... \n")
		gatewayIP = "127.0.0.1"
	else:
		sys.stdout.write("Your default gateway IP is "+gatewayIP+" \n\n")
	#wait to let user read
	time.sleep(1)
	os.system('clear')
	sys.stdout.write("Running test, please wait.\n\n")
	ping(gatewayIP)
	
def remote():
	os.system('clear')
	sys.stdout.write("Testing for remote connectivity... trying IP address 129.21.3.17\n\n")
	#wait to let user read
	time.sleep(1)
	os.system('clear')
	sys.stdout.write("Running test, please wait.\n\n")
	ritDNS = "129.21.3.17"
	ping(ritDNS)


def dns():
	os.system('clear')
	sys.stdout.write("Resolving DNS: trying URL... \"www.google.com\"\n\n")
	#wait
	time.sleep(1)
	os.system('clear')
	sys.stdout.write("Running test, please wait.\n\n")
	google = "www.google.com"
	ping(google)

if __name__ == "__main__":
	main()
