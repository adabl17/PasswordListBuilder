import os
import itertools
red='\033[31m'
green='\033[32m'
yellow= '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
white =  '\033[39m'
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("clear")
os.system("apt install figlet -y")
os.system("clear")
print(f'''{purple}
@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@%%%%%%%%%%%%%%%%%%%@%@@@@@@@@@
@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@%%@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@
@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@
@@@@@%%%%%%%%%%%%%######%%%%%%%%%%%%%@@@
@@@@@%%%%%%%%###*#*+++++*##%%%%%%%%%%@@@
@@@@@%%%%%%%#%###*+===++++#%%%%%%%%%%@@@
@@@@%%%%%%%%####*++===+++**#%%%%%%%%%@@@
@@@%%%%%%%%######*++++++++**###%%%%%%@@@
@@@%%%%%%#########****++++***#%%%%%%%@@@
@@%%%%%%%%%#######******+++**#%%%%%%%@@@
@@@%%%%%%%%######******#####**##%%%%%@@@
@@@%%%%%%%%**#*#********###**#*#%%%%%%@@
@@%%%%%%%##+*************#**+*#%%%%%%%@@
@@%%%%%%%%#*****=++***++***++*%%%%%%%%@@
@@%%%%%%%%%****#%%***+%%#**++#%%%%%%%%@@
@%%%%%%%%%#+**%%%%%**#%##%#++#%%%%%%%%@@
@%%%%%%%##*+*#%%%%#=-+=.:+#++#%%%%%%%%%@
@@%%%%%%%%%**#%%%%%*##%##%%*+%%%%%%%%%%@
@@%%%%%%%%%%###%%#*%%###%%#**#####%%%%@@
@@%%%%%%%###*###**#%%#+#####**#%%%%%%%@@
@@%%%%%%%%##*###**#%%#**##*+#%%%%%%%%%@@
@@%%%%%%%%##*+*****##*****++#%%%%%%%%%@@
@@%%%%%%%%%%#*%*********+%++#%%%%%%%%%@@
@@%%%%%%%%%%#*%*+*****+=+%++#%%%%%%%%%@@
@@%%%%%%%%%%%#%#******+=+%+%%%%%%%%%%%%@
@@%%%%%%%%%%####*+++++++*#+###%%%%%%%%@@
@@%%%%%%%%%%%%####***#*##*#%%%%%%%%%%%@@
@@@%%%%%%%%%%##########****###%%%%%%%%@@
@@@%%%%%%%%#%###########**%%%%%%%%%%%%@@
@@@%%%%%%%%%#######***#**#%%%%%%%%%%%%@@
@@@%%%%%%%%%%%%%%##+*+***%##%%%%%%%%%@@@
@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@%@%@@@@
@@@@@@@@@%@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@
''')
print(f"{red}===========================================")
print(f"{yellow}  rubika channel: @https://rubika.ir/amuzesh_hackre         ")
print(f"{yellow}  rubika me: @Hacker___name___adabl          ")
print(f"{red}===========================================")
print(f"{white} [1]"+ f"{blue} start")
print(f"{white} [2]"+ f"{blue} exit")
king = int(input(f"{yellow} [~]"+ f"{purple} Select ---> "))
if king == 1:


    dig = input(f"{yellow} [~]"+ f"{purple} Einter digs: ")

    dig = list(dig)

    passwords = itertools.permutations(dig)
    with open('pass.txt', 'a') as file:
        for pas in passwords:
            password = ''.join(pas)
            file.write(password+'\n')
        file.close()
        print(f"{white} [1]"+ f"{blue} Copy the file on Android")
        print(f"{white} [2]"+ f"{blue} Copy the file to Windows")
        ja = int(input(f"{yellow} [~]"+ f"{purple} Select ---> "))
        if ja == 1:
            os.system("cp -r pass.txt /sdcard")
        elif ja == 2:
            os.system("cp -r pass.txt /mnt/c/Users/Avand/Desktop")
        else:
            print(f"{red}erorrrrrrr")
        print(f"{yellow} ok \n good job")

elif king == 2:
    os.system("clear")
    print(f"{blue}good")
else:
    print(f"{red}erorrrrrrr")
