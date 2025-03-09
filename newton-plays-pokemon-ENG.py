import socket
import pyautogui 
import threading
import time
import pandas as pd

# Twitch IRC server details
SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "" #Put your OAth key here
BOT = "TwitchBot"
CHANNEL = "" #Put your username here
OWNER = "" #Put your username here
message = ""

# Connecting to Twitch chat
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode()) 

# Base setup for vote collection
max_votes = 1 # If you want to change the number of votes per cycle, modify this variable
interval = 2 # Adjust this variable to change voting duration
last_action_time = time.time()
message_list = []
user_list = []
total_votes = []
keys = ['z', 's', 'q', 'd', 'a', 'b', 'enter']
key_counts = [0] * len(keys)
bool_exec = True

# Load previous votes from CSV file
#can be deleted along with the three lines starting at line 121
df_vote = pd.read_csv("votes.csv", sep=";")
vote_list = list(df_vote["Vote"])

def twitchSection():
    # Handles Twitch chat connection and message retrieval
    global last_action_time
    def joinChat():
        # Joins the Twitch chat
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024).decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = loadingComplete(line)
    
    def loadingComplete(line):
        # Confirms successful connection to chat
        if("End of /NAMES list" in line):
            print("The bot has joined " + CHANNEL + "'s channel!")
            sendMessage(irc, "Chat has been joined")
            return False
        else:
            return True
    
    def sendMessage(irc, message):
        # Sends a message to the Twitch chat
        tempMessage = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((tempMessage + "\n").encode())
    
    def getUser(line):
        # Extracts the username from a message
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user
    
    def getMessage(line):
        # Extracts the message content
        global message
        try:
            message = (line.split(":", 2))[2]
        except:
            message = ""
        return message
    
    def Console(line):
        # Checks if the line is a console message or a chat message
        return "PRIVMSG" not in line
    
    joinChat()

    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except: 
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            if "PING" in line and Console(line):
                # Responds to Twitch's ping messages to maintain connection
                messagepv = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(messagepv)
                print(messagepv)
                continue
            else:
                # Processes incoming messages
                user = getUser(line)
                message = getMessage(line)
                print(user + " : " + message)
                message_list.append(message.lower())  # Store received message
                user_list.append(user)
                current_time = time.time()
                if current_time - last_action_time >= interval:
                    winner = countVotes()
                    total_votes.append(winner)
                    sendMessage(irc, "Executed key: " + str(winner) + ".")
                    sendMessage(irc, " -> by: " + user_list[0])
                if len(message_list) >= max_votes:
                    message_list.clear()
                    user_list.clear()
                    last_action_time = current_time
            
            # Store vote results in CSV file
            #can be deleted along with the two lines starting at line 37
            vote_list.append(winner)
            df_vote = pd.DataFrame({"Vote": vote_list})
            df_vote.to_csv("votes.csv", index=False, sep=";")

def countVotes():
    # Counts the votes and executes the most voted key
    global key_counts, bool_exec
    for message in message_list:
        for i, key in enumerate(keys):
            if key in message:
                key_counts[i] += 1
    
    # Find the most voted key
    most_voted_index = key_counts.index(max(key_counts))
    if key_counts[most_voted_index] > 0:
        pyautogui.keyDown(keys[most_voted_index])
        pyautogui.keyUp(keys[most_voted_index])
        print(f"Executing action: {keys[most_voted_index]}")
        bool_exec = False
    key_counts = [0] * len(keys)

    return keys[most_voted_index]

print(f"The most voted key in this session is: {max(vote_list, key=vote_list.count)}")

# Using threading to run multiple loops simultaneously
if __name__ == '__main__':
    t1 = threading.Thread(target=twitchSection)
    t1.start()
