import os
import time

def splash_screen(seconds):
  print('''                                
                                                                                             kkkkkkkk                  iiii  
                                                                                              k::::::k                 i::::i 
                                                                                              k::::::k                  iiii  
                                                                                              k::::::k                        
rrrrr   rrrrrrrrr        wwwwwww           wwwww           wwwwwww       aaaaaaaaaaaaa         k:::::k    kkkkkkk     iiiiiii 
r::::rrr:::::::::r        w:::::w         w:::::w         w:::::w        a::::::::::::a        k:::::k   k:::::k      i:::::i 
r:::::::::::::::::r        w:::::w       w:::::::w       w:::::w         aaaaaaaaa:::::a       k:::::k  k:::::k        i::::i 
rr::::::rrrrr::::::r        w:::::w     w:::::::::w     w:::::w                   a::::a       k:::::k k:::::k         i::::i 
 r:::::r     r:::::r         w:::::w   w:::::w:::::w   w:::::w             aaaaaaa:::::a       k::::::k:::::k          i::::i 
 r:::::r     rrrrrrr          w:::::w w:::::w w:::::w w:::::w            aa::::::::::::a       k:::::::::::k           i::::i 
 r:::::r                       w:::::w:::::w   w:::::w:::::w            a::::aaaa::::::a       k:::::::::::k           i::::i 
 r:::::r                        w:::::::::w     w:::::::::w            a::::a    a:::::a       k::::::k:::::k          i::::i 
 r:::::r                         w:::::::w       w:::::::w             a::::a    a:::::a      k::::::k k:::::k        i::::::i
 r:::::r                          w:::::w         w:::::w              a:::::aaaa::::::a      k::::::k  k:::::k       i::::::i
 r:::::r                           w:::w           w:::w                a::::::::::aa:::a     k::::::k   k:::::k      i::::::i
 rrrrrrr                            www             www                  aaaaaaaaaa  aaaa     kkkkkkkk    kkkkkkk     iiiiiiii
                                                                                                                              
                                     ''')
  time.sleep(seconds)
  #os.system('clear')  
  
  
#Main Program Starts Here....
splash_screen(3)
username=input("Type your username:")
