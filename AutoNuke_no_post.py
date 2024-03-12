import subprocess
import os
import sys
import threading
import time



# ulimit -f unlimited.
# The ReadMe:
#
# NOTE: make sure to mkdir for "targets" and "tmp" in the same directory that you save this.
# ALSO: touch tmp/ASF00.log
# Prior to running.
# 
# https://www.youtube.com/watch?v=t4yYVB1KwpE&ab_channel=TEAMR00T
#

try:
    name = sys.argv[3]
    torPort = "9050"
    file = ' '.join(sys.argv[1:2])
    p = subprocess.Popen("touch tmp/" + name + " && touch tmp/" + name + ".txt && ulimit -f unlimited.", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    p.wait()

    with open(file, "r") as f:
        f = f.read().splitlines()
        for ip in f:
            if ip == "":
                pass;
            else:
                print("")
                print("Now Scanning: " + ip)
                print("")

                p = subprocess.Popen("sudo masscan --rate=2000 --interface " + sys.argv[2] + " -p80,443,8443,10443,22,3389,3306 -Pn " + ip + " -oJ tmp/" + name + ".log", stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen('grep -oE \"\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b\" tmp/' + name + '.log > tmp/unsorted.txt', stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen("sort tmp/unsorted.txt | uniq > tmp/" + name + "_targets.txt", stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen("echo "" > tmp/" + name + ".txt", stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen("cat tmp/" + name + "_targets.txt | httpx -random-agent -nf -rl 5000 -t 1000 -p 22,3389,3306,80,443,7547,8080,8089,4567,8008,8443,8081,2087,2083,2082,5985,2086,8000,8888,1024,21,81,8880,9080,5000,49152,9000,3128,7170,8085,8090,5001,8001,9999,10000,10443,8083,9090,3000,88,5357,9100,7777,82,52869,9443,4443,8800,9306,8181,444,7443,9001,2096,8086,5222,8010,1234,8009,8200,2095,10001,9002,83,6000,20000,9009,50000,5005,6443,9200,32400,2222,5555,3001,8069,8099,8889,6001,1900,8060,9998,5006,7001,84,5986,8123,888,25,12345,5800,631,10250,8098,7548,2000,2121,8112,3702,2077,8087,5010,8126,23,161,6667,6697 -o tmp/" + name + ".txt", stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen('nuclei -l tmp/' + name + '.txt -severity critical,high -o targets/' + name + '.nuked', stdout=subprocess.DEVNULL, shell=True)
                p.wait()
                p = subprocess.Popen('cat targets/' + name + '.nuked >> ./' + name, stdout=subprocess.DEVNULL, shell=True)
                p.wait()

except (IndexError):
    print("\nOperator Error:")
    print("     please include the following (in this order):")
    print("         - a file with IP blocks (0.0.0.0/0 format)")
    print("         - a network interface.")
    print("         - a name for the pad you wish to post to.")
    print("       IE: python3 nuclei.py file.txt tun0 AutoNuclei")
    print("           (python3 nuclei.py [ip block file] [network interface] [pad name])")
    print("\n NOTE: This script operates off of TOR PORT 9050 - please change if your tor port differs.")
