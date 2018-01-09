#MarkovChat.py


#---------------------------------------
# Import Libraries
#---------------------------------------
import socket
import re
import time
import random
import markovify
import signal
import sys


#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "MarkovChat"
Website = "https://www.twitch.tv/mr_friggz"
Description = "Creates markov chains to talk to chat!"
Creator = "mr_friggz"
Version = "1.0.0.0"


#---------------------------------------
# Set Variables
#---------------------------------------
m_Response = "Test Response"
m_Command_Shakes= "!shakespeare"
m_Command_Chat = "!chatsoundslike"
m_CooldownSeconds = 4
m_CommandPermission="Everyone"
m_CommandInfo=""
m_Num_Lines = 0

#read corpus to file
with open("shakespeare.txt") as f:
	shakes_corpus = f.read()


#build shakespeare markov model from file
shakes_model = markovify.NewlineText(shakes_corpus)


#---------------------------------------
# [Required] Intialize Data (Only called on Load)
#---------------------------------------
def Init():
	return


#---------------------------------------
# [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):


	global m_Num_Lines

	if data.IsChatMessage():

		#add to corpus
		with open("twitch_chat.txt", 'a') as k:
			chat_msg = data.GetParam(0) + "\r\n"
			k.write(chat_msg)
		m_Num_Lines += 1

		if data.GetParam(0).lower() == m_Command_Shakes and not Parent.IsOnCooldown(ScriptName,m_Command_Shakes) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):
			
			#generate sentence from model and send it out
			m_Response = shakes_model.make_sentence(tries=100)
			Parent.SendTwitchMessage(m_Response)

		if data.GetParam(0).lower() == m_Command_Chat and not Parent.IsOnCooldown(ScriptName,m_Command_Chat) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):


			if m_Num_Lines > 100:
				with open("twitch_chat.txt",'r') as j:
					chat_corpus = j.read()

				chat_model = markovify.NewlineText(chat_corpus)
				m_Response = "You sound like this chat: \"" +chat_model.make_sentence(tries=100) + "\""
				Parent.SendTwitchMessage(m_Response)
			else:
				m_Response = "Not enough messages in chat to imitate you"
				Parent.SendTwitchMessage(m_Response)


	return

#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
	return