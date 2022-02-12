#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Connecting 4
import os

def printtable():	#Print the table.
	i=os.system("cls")
	print("       |   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
	for i in range(6):	#rows
		row="abcdef"
		row="       | "+row[i]
		for j in range(7):	#columns
			if table[i*7+j]==0:
				row=row+" |  "
			elif table[i*7+j]==1:
				row=row+" | o"
			elif table[i*7+j]==-1:
				row=row+" | x"
		row=row+" |"
		print(row)
	return 0

def start():	#Empty the table. Clear all steps.
	for i in range(42):
		table[i]=0
	while len(step)>0:
		step.remove(step[0])
	printtable()
	return table

def do(column,player):	#Game ends return 1. Update step and table.
	column-=1
	if (table[column]!=0) or (column not in range(7)):
		printtable()
		print("   Error: invalid column! Please choose again.")
		return 0
	row=5
	while table[column+7*row]!=0:
		row-=1
	table[column+7*row]=player
	step.append(column)
	printtable()
	end = win(row,column,player)
	if end==1:
		print("   Player1 wins!")
		return 1
	elif end==-1:
		print("   Player2 wins!")
		return 1
	if len(step)==42:
		print("   Game draw!")
		return 1
	return 0

def undo():	#Update step and table.
	if len(step)>0:
		column=step[-1]
		i=0
		while table[column+7*i]==0:
			i+=1
		table[column+7*i]=0
		del step[-1]
		printtable()
	else:
		printtable()
		print("   Error: cannot undo at the begining! Please choose a column.")
	return 0

def win(row,column,player):	#Check if a player wins. Player1 wins return 1; Player2 wins return -1; Else return 0.
	for i in range(4):
		ifrow=0
		ifcol=0
		if (row-i in range(6)) and (row+3-i in range(6)):
			ifrow=1
			s=0
			for j in range(4):
				s+=table[7*(row-i+j)+column]
			if s*player==4:
				return player
		if (column-i in range(7)) and (column+3-i in range(7)):
			ifcol=1
			s=0
			for j in range(4):
				s+=table[7*(row)+column-i+j]
			if s*player==4:
				return player
		if ifcol==1 and ifrow==1:
			s=0
			for j in range(4):
				s+=table[7*(row-i+j)+column-i+j]
			if s*player==4:
				return player
		if (column+i in range(7)) and (column+i-3 in range(7)) and ifrow==1:
			s=0
			for j in range(4):
				s+=table[7*(row-i+j)+column+i-j]
			if s*player==4:
				return player

def play():	#Check witch player goes next. Player1 return 1; Player2 return -1.
	if len(step)%2==0:
		return 1
	else:
		return -1

if __name__ == "__main__":	#Main game.
	table=[0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,
           0,0,0,0,0,0,0]
	step=[]
	game="1"
	while game=="1":
		start()
		x=0
		while x==0:
			player=play()
			if player==1:
				d = input("   Player1: choose a column, or input \"u\" to undo.")
			if player==-1:
				d = input("   Player2: choose a column, or input \"u\" to undo.")
			if d != "u":
				x = do(int(d),player)
			else:
				x = undo()
		game = input("   Input 1 for try again, input others for end:")
