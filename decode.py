#!/usr/bin/env python3

import json, sys, re
from os.path import expanduser
from subprocess import call, Popen


fileName = expanduser("~") + "/.config/shit-talk/commands.json"
param = sys.argv[1]



print("Decode is called")

file = open(fileName)
text_json = json.loads( file.read() )

file.close()

#print(text_json)

tuples = text_json["all"]

tup = []
for strings in tuples:
	conds=[]
	for x in strings["condition"]:
		
		conds.append(x)		
	
	
	tup.append (  (conds, strings["command"]) )

default_command = text_json["default_command"]



found = False
to_exec = "var="+ "\""+param + "\";"
for i in range(0,len(tup)):
	#building command and conditions	
	conds = tup[i][0] 
	comm = tup[i][1]
	#print("cond: "+cond+"\ncomm: "+comm) 
	for cond in conds:
		if re.search(cond, param):
			print("in for ;" + cond + ";")
			found = True
			to_exec += comm
			print("executing: " + to_exec)
			call(to_exec, shell=True)
			break;
		else:
			print("next for ;" + cond + ";")

	if found : break


if not found:
	to_exec += default_command
	print("Doing default: " + to_exec )
	call(to_exec, shell=True)



