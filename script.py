#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Simple tool for finding out the vendor of a mac address
#
# Created by: r1l4r, 2018

import sys
import argparse
import json

vendors = {
    'apple' : 'Apple, Inc',
    'samsung' : 'Huawei Technologies Co. Ltd',
    'huawei' : 'Huawei Technologies Co. Ltd',
    'lg' : 'LG Corporation',
    'google' : 'Google, Inc',
    'nokia' : 'Nokia Corporation',
    'sony' : 'Sony Corporation',
    'xiaomi' : 'Xiaomi',
    'microsoft' : 'Microsoft Corporation',
    'motorola' : 'Motorola Solutions Inc',
    'nec' : 'NEC Corporation',
    'blackberry' : 'BlackBerry Limited',
    'ericsson' : 'Ericsson'

}

def main():
    print_banner()
    handle_args(parse_args())

def handle_args(args):
    if args.mac:
        get_vendor(args.mac[0:8])
        print("")
        sys.exit()

def parse_args():
    parser = argparse.ArgumentParser()
    required_group = parser.add_argument_group('required argument')
    mutex_group = required_group.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('-m', '--mac', dest='mac', help='script.py -m 10:dd:b1:ff:fe:0b')
    return parser.parse_args(sys.argv[1:])

def get_vendor(mac):
    for vendor_name in vendors:
        with open('vendors/'+vendor_name+'.json') as f:
            vendor_mac_addresses = json.load(f)
            if mac in vendor_mac_addresses:
                print('\033[92m'+'[+] '+vendors[vendor_name]+'\033[0m')
                return
            else:
                print('\033[91m'+'[-] '+vendors[vendor_name]+'\033[0m')
    print('')
    print('\033[91m'+'No results!'+'\033[0m')

def print_banner():
    print("")
    print('\033[94m'+'Vendor-Mac-Addresses 1.0 - By https://github.com/r1l4r'+'\033[0m')
    print("A tool to find the manufactoror by mac address with focus on mobile phones")
    print("")
    print("Last updated 2018-11-10:")
    print("https://udger.com/resources/mac-address-vendor")
    print("")

if __name__ == "__main__":
    main()
