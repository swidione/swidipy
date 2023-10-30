
print  ( "  / / / / /__  / _ \   /   / / / / \   / /" )
print ( " / /_/ / /__  / _  \  / / / / / / /\ \/ /" )
print( "/_/-/_/ /__  /_/ /_/ /___/ /_/ /_/  \__/" ) #Hero -In
import time 
from playsound import playsound



#  ___           ___           ___           ___                       ___     
#     /\__\         /\  \         /\  \         /\  \          ___        /\__\    
#    /:/  /        /::\  \       /::\  \       /::\  \        /\  \      /::|  |   
#   /:/__/        /:/\:\  \     /:/\:\  \     /:/\:\  \       \:\  \    /:|:|  |   
#  /::\  \ ___   /::\~\:\  \   /::\~\:\  \   /:/  \:\  \      /::\__\  /:/|:|  |__ 
# /:/\:\  /\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/__/ \:\__\  __/:/\/__/ /:/ |:| /\__\
# \/__\:\/:/  / \:\~\:\ \/__/ \/_|::\/:/  / \:\  \ /:/  / /\/:/  /    \/__|:|/:/  /
#      \::/  /   \:\ \:\__\      |:|::/  /   \:\  /:/  /  \::/__/         |:/:/  / 
#      /:/  /     \:\ \/__/      |:|\/__/     \:\/:/  /    \:\__\         |::/  /  
#     /:/  /       \:\__\        |:|  |        \::/  /      \/__/         /:/  /   
#     \/__/         \/__/         \|__|         \/__/                     \/__/   

#(_)   (_)                (_)      
# _______ _____  ____ ___  _ ____  
#|  ___  | ___ |/ ___) _ \| |  _ \ 
#| |   | | ____| |  | |_| | | | | |
#|_|   |_|_____)_|   \___/|_|_| |_|
#
                     
 #|_|  _  ._ _  o ._  
 #| | (/_ | (_) | | | 
      
#print ("__|  _  |__  ______  _____   _____  ____  ____   _  ")
#print("|  |_| |    ||   ___||     | /     \|    ||    \ | | ")
#print("|   _  |    ||   ___||     \ |     ||    ||     \| | ")
#print("|__| |_|  __||______||__|\__\\_____/|____||__/\____| ")
#10print("   |_____| " )
                                                      
                     
                                  


playsound("C:\Windows\Media\Windows Notify System Generic.wav")

a=input("Enter Target IP Address: ")
print("Scanning Target")
time.sleep(2)
print("Target Found!", a)
b=input("Enter Host IP Address(This Networks Public IP):  ")
z= input("Password (This Network/User) : ")

print("Connection Established!     ", b,":1337" "--->", a,":1337")
time.sleep(2)


print("\\\ Choose Attack Method: ///")
time.sleep(1)
print("1:Wireless Attack")

print("2:Password Attack")

print("3:Ransomeware Encryption Attack")
c =input("Enter # : ")
print("Good Choice! :", (c))
    
print("Bruteforcing Password...")
time.sleep(3)
print("\n")
print("------> Password FOUND! : ", (z), "Sent output: URL: tcp://www.ans098nq3g.com/password/ip_log.py")
time.sleep(7)
print("\n")
print("thank you for using n00b_PhisheR!...SEE You later!")
f = open("test.txt", "r")
o = (a,b,c,z)
print(f.read())



with open('hero_in_manifest.txt', 'wt') as f:
    print(o, file=f )
