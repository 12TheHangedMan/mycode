#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

def main():
    
    #move into the working directory
    os.chdir("/home/student/mycode/")

    #copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #remove the previous folder if there is any
    os.system("rm -rf /home/student/mycode/5g_research_backup/")

    #copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


