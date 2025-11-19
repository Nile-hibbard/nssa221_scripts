#!/usr/bin/env python3

#Nile Hibbard 10/23/2025

import re
import subprocess
import os
import platform
from geoip import geolite2

pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

def main():
    with open(LogFile, "r") as f:
        log = f.readLines()

    ips =[]
    for line in log:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            ips.append(ip)
    
    common_ips = {}
    for ip in ips:
        if ip not in common_ips:
            common_ips[ip]=1
        else:
            common_ips[ip]+=1

    for ip in common_ips:
        match = geolite2.lookup(common_ips)
        output = str(common_ips[ip])+"   "+str(ip)+"  "+match.country