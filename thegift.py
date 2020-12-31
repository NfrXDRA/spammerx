import os
os.system('clear')
print ('''\033[1;36m     ____________________________
    !\_________________________/!\
    !!                         !! \
    !!                         !!  \
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  /
    !!_________________________!! /
    !/_________________________\!/
       __\_________________/__/!_
      !_______________________!/ )
    ________________________    (__
   /oooo  oooo  oooo  oooo /!   _  )_
  /ooooooooooooooooooooooo/ /  (_)_(_)
 /ooooooooooooooooooooooo/ /    (o o)
/C=_____________________/_/    ==\o/==''')
e = input ('\033[1;34m # Your Email:  ')
p = input ('\033[1;34m # Your Password:  ')
import amino
clint =amino.Client()
clint.login(email=e,password=p)
com=input('\033[1;32m # Enter community url:  ')
co=clint.get_from_code(com)
comId=co.path[1:co.path.index("/")]
subclint=amino.SubClient(comId=comId,profile=clint.profile)
os.system('clear')
print ('''\033[1;36m _____   _____       ___   _____    _____  
/  ___/ |_   _|     /   | |  _  \  |_   _| 
| |___    | |      / /| | | |_| |    | |   
\___  \   | |     / / | | |  _  /    | |   
 ___| |   | |    / /  | | | | \ \    | |   
/_____/   |_|   /_/   |_| |_|  \_\   |_|   ''')
x=1
p = '\033[1;36m'
name = input ('\033[1;31m# Enter blog title: ')
de=input('\033[1;31m# Enter blog describe:')
while True:
	subclint.post_blog(title=name,content=de)
	print (p,x,')spam')
	x+=1