import os


def addtostartup():
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	with open(bat_path + '\\' + "SCH_SYSTEM.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % PATH + "FaceAppControl.exe")
        return 0
dir_ = os.getcwd()
tbr = ["*.cpp","*.h","*.ui","*.xml","*.bat","*.py","*.txt","*.pro"]
PATH = ""

os.system("cd ..")
for i in tbr:
	os.system("rm " + i)
os.system("cd " + dir_)
print("Enter Dir to put system in")
PATH = input()
tree = od.walk(PATH)
os.system("cd " + PATH)
os.mkdir("SCH_SYSTEM")
os.system("cd " + dir_)
os.system("cp * " + PATH + "\\SCH_SYSTEM")
addtostartup()
os.system("cd " + dir_)
os.system("requriments-install.bat")
print("Enter DB Server IP")
Server = input()
with open("C:\\Windows\\System32\\drivers\\etc\\hosts","a") as f:
	f.write(Server + "\t" + "schdb.sch")


print("DONE\n Now Put your Students DB into Server, call it 'SCH_DB.db' and use creds in Readme for login in" + "\n " + "Press any ket when db will be on a Server")
os.system("pause")
os.system("shutdown /r -t 0")
