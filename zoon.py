#!/usr/bin/env python
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/engines")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/techs")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/utils")

import argparse

def f_consul(args):
    print 'Ave Consul ' + args.name + '!'

def command_line():
    # Common "parent" parsers
    # Mode
    mode = argparse.ArgumentParser(add_help=False)
    mode.add_argument("mode", help="mode", choices=['create', 'delete'])

    name = argparse.ArgumentParser(add_help=False)
    name.add_argument("name", help="name")

    # Top Level Parser
    parser = argparse.ArgumentParser(description='AWS lightweight application management')

    # Optional Arguments to TLP
    parser.add_argument("--aws", help="whether to USE AWS", action="store_true")
    parser.add_argument("-s","--size", help="cluster size per region", type=int, default=1)
    parser.add_argument("-r","--region", help="aws region", default='us-east-1', choices=['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1', 'ap-southeast-2'] )

    vpc_group = parser.add_mutually_exclusive_group()
    vpc_group.add_argument("--no-vpc", help="use EC2 Classic", action="store_true", default=False)
    vpc_group.add_argument("--vpc", help="use EC2 VPC", action="store_true", default=True)

    # Engine Sub-Parser
    engines = parser.add_subparsers(help='engines')

    # Engines go here
    # Consul Parser
    consul = engines.add_parser('consul', description='Consul: tool for discovering and configuring services in your infrastructure', help='tool for discovering and configuring services', parents=[mode,name]) 
    consul.set_defaults(func=f_consul)

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    prog = sys.argv[0]
    args = command_line()
    args.func(args)

#    print args
    
# END
