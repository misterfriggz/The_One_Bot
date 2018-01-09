#Worship.py


#---------------------------------------
# Import Libraries
#---------------------------------------
import socket
import re
import time
import random
import signal
import sys


#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "Worship"
Website = "https://www.twitch.tv/mr_friggz"
Description = "Allows Twitch Chat to worship The One Bot in exchange for Gratitude (uniquely available every 10 minutes)"
Creator = "mr_friggz"
Version = "1.0.0.0"


#---------------------------------------
# Set Variables
#---------------------------------------
m_Response = "Test Response"
m_Command= "!worship"
m_CooldownSeconds = 600 #10 minutes
m_CommandPermission="Everyone"
m_CommandInfo=""
worship_counter = -1






#---------------------------------------
# [Required] Intialize Data (Only called on Load)
#---------------------------------------
def Init():
	global worship_counter
	with open('worship.txt', 'r') as f:
		worship_counter = int(f.readline())

	return


#---------------------------------------
# [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):


	global m_Response
	global worship_counter

	if data.IsChatMessage():
		user = data.User

		if data.GetParam(0).lower() == m_Command:

			if Parent.IsOnCooldown(ScriptName,m_Command):
			
				m_Response = "A single worship is available every 10 minutes " + user + ". Git gud, greedy scum"
				Parent.SendTwitchMessage(m_Response)

			else:


				#add Gratitude points
				Parent.AddPoints(user,10)
				worship_counter += 1

				with open('worship.txt', 'w') as f:
					f.write(str(worship_counter))

				m_Response = "You've succesfully worshipped me " + user + ". I bestow 10 Gratitude upon you. Total chat worship is " + str(worship_counter) + " btw"
				Parent.SendTwitchMessage(m_Response)
				Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)




	return

#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
	return