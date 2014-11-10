#!/usr/bin/env python
import os
import sys
import argparse
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/engines")
#sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/techs")
#sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/utils")


import ze_consul

def f_consul(args):
    cosul = ze_consul.Consul(args)

def command_line():
    # Common "parent" parsers
    # Mode
    mode = argparse.ArgumentParser(add_help=False)
    mode.add_argument("mode", help="usage mode", choices=['create', 'delete', 'update', 'status'])

    name = argparse.ArgumentParser(add_help=False)
    name.add_argument("name", help="name of consul cluster")

    aws = argparse.ArgumentParser(add_help=False)
    aws.add_argument("--aws", help="whether to USE AWS", action="store_true", default=True)

    size = argparse.ArgumentParser(add_help=False)
    size.add_argument("-s","--size", help="cluster size per region", type=int, default=1)



    # Valid Regions
    regions = argparse.ArgumentParser(add_help=False)
    regions.add_argument("-r","--region", help="aws region", default='us-east-1', choices=['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1', 'ap-southeast-2'] )

    useast1 = argparse.ArgumentParser(add_help=False)
    useast1.add_argument("--us-east-1", help="AWS US-East-1", action="store_true", default=False)

    uswest1 = argparse.ArgumentParser(add_help=False)
    uswest1.add_argument("--us-west-1", help="AWS US-West-1", action="store_true", default=False)

    uswest2 = argparse.ArgumentParser(add_help=False)
    uswest2.add_argument("--us-west-2", help="AWS US-West-2", action="store_true", default=False)

    euwest1 = argparse.ArgumentParser(add_help=False)
    euwest1.add_argument("--eu-west-1", help="AWS EU-West-1", action="store_true", default=False)

    apsoutheast1 = argparse.ArgumentParser(add_help=False)
    apsoutheast1.add_argument("--ap-southeast-1", help="AWS AP-Southeast-1", action="store_true", default=False)

    apsoutheast2 = argparse.ArgumentParser(add_help=False)
    apsoutheast2.add_argument("--ap-southeast-2", help="AWS AP-Southeast-2", action="store_true", default=False)

    vpc = argparse.ArgumentParser(add_help=False)
    vpc_group = vpc.add_mutually_exclusive_group()
    vpc_group.add_argument("--vpc", help="use EC2 VPC", action="store_true", default=True)
    vpc_group.add_argument("--no-vpc", help="use EC2 Classic", action="store_true", default=False)

    # Optional Arguments to TLP
    deployment_environment = argparse.ArgumentParser(add_help=False)
    deployment_environment.add_argument("-e", "--env", help="Deployment Environment", default="dev")

    # Top Level Parser
    parser = argparse.ArgumentParser(description='AWS lightweight application management', parents=[deployment_environment])
    

    # Engine Sub-Parser
    engines = parser.add_subparsers(help='engines')

    # Engines go here
    # Consul Parser
    cosul = engines.add_parser('consul', description='Consul: tool for discovering and configuring services in your infrastructure',
                               help='tool for discovering and configuring services',
                               parents=[mode, name, size, vpc, useast1, uswest1, uswest2, euwest1, apsoutheast1, apsoutheast2]) 
    cosul.set_defaults(func=f_consul)

    args = parser.parse_args()

    if args.no_vpc:
        args.vpc = False

    return args

if __name__ == '__main__':
    prog = sys.argv[0]
    args = command_line()
    args.func(args)

    print args
    
# END
