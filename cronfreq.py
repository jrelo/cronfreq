#!/usr/bin/env python2.7
#depends on https://raw.githubusercontent.com/manos/Puppet-Cron-Analyzer/master/cronlib.py by Charlie Schluting <charlie@schluting.com>
#-jrelo
import cronlib
import subprocess
import sys
import os
import string

colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[1;36m{0}\033[00m"

def freq_test(list, Threshold):
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) <= Threshold:
            list.append((list[i] + list[i+1])/2) 
            #list.sort()
            print colorgrn.format("^") + "Above cronjob runs more than once in " + colorred.format(str(Threshold)) + " minute span."
            break

def main():
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' <cron file> <threshold>\n')
        sys.exit(1)

    thresh = int(sys.argv[2])
    fname = str(sys.argv[1])
    print fname
    with open(fname) as f:
        for li in f:
            line=li.strip()
            if not line.startswith(("#", "MAILTO", "@")):
                print line
                cron = line
                cron_normal = cronlib.normalize_entry(cron)
                #print cron_normal
                minutes = map(int, cron_normal[0].split(','))
                #print minutes
                freq_test(minutes,thresh)

if __name__ == '__main__':
    main()
