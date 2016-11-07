import os
import syslog
import sys
import time

log_file = {
    'iptables': {
        'path': '/var/log/iptables.log',
        'size': 0
    },
    'apache_access': {
        'path': '/var/log/apache_access.log',
        'size': 0
    },
    'apache_error': {
        'path': '/var/log/apache_error.log',
        'size': 0
    },
    'auth': {
        'path': '/var/log/auth.log',
        'size': 0
    },
    'bccas': {
        'path': '/var/log/bccas.log',
        'size': 0
    },
    'cisco-asa': {
        'path': '/var/log/cisco-asa.log',
        'size': 0
    },
    'syslog': {
        'path': '/var/log/syslog',
        'size': 0
    },
    'proftpd': {
        'path': '/var/log/proftpd.log',
        'size': 0
    },
    'access': {
        'path': '/var/log/squid/access.log',
        'size': 0
    },
    'sourcefire': {
        'path': '/var/log/ossim/sourcefire.log',
        'size': 0
    }
}

def checksize(path, sizevar):
    if os.path.getsize(path) <= sizevar:
        syslog.syslog('Log file %s not receiving logs.' % (path))
        sys.stdout.flush()

def loop():
    while True:
        for key in log_file.keys():
            log_file[key]['size'] = os.path.getsize(log_file[key]['path'])
            time.sleep(3600)
            checksize(log_file[key]['path'], log_file[key]['size'])

loop()