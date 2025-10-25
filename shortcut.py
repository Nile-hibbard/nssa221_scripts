#!/usr/bin/env python3

#Nile Hibbard 10/23/2025

import subprocess
import os
import platform

os.system('clear')

#ask for goal
print("enter command(help for options)")
done=0
while done==0:
    command=input(os.getcwd()+">")
    part=command.split(" ")
    user=os.getlogin()
    if part[0]=="create":
        try:
            os.symlink(part[1],"/home/"+user+"/Desktop/"+part[2],True)
        except ValueError:
            print("File was not found")
    elif part[0]=="remove":
        try:
            os.unlink("/home/"+user+"/Desktop/"+part[1])
        except:
            print("File was not found")
    elif part[0]=="generate":
        homedir=os.path.expanduser("/home/"+user)
        desktopdir=(os.path.join(homedir,"Desktop"))
        links=0
        print("- Symlinks on desktop -")
        for item in os.listdir(desktopdir):
                path=(homedir+"/Desktop/"+item)
                if os.path.islink(path):
                    target="/home/"+user+"/"+os.readlink(path)
                    print(path+"->"+target)
        for root, dirs, files in os.walk(homedir):
            for name in dirs + files:
                path=os.path.join(root, name)
                if os.path.islink(path):
                    links+=1
        print("# of links "+str(links))
  elif part[0]=="help":
        print("Commands:")
        print("help -prints this help message")
        print("create [source path] [link-name] -creates a new link")
        print("remove [link-name -removes designated link")
        print("generate report -compiles a report of all symbolic links on the users desktop")
        print("exit -ends the program")
    elif part[0]=="exit":
        done+=1
    else:
        print("Unknown command, for help use help")
                                                    
