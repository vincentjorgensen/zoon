#!/usr/bin/env python
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/engines")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/techs")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/utils")

import argparse

def command_line(arg_vec):
    engine = argparse.Action( help="App or Engine to operate on")
    engine = d_argument("engine", help="App or Engine to operate on")
    parser.add_argument("mode", help="create, delete")
    
    parser = argparse.ArgumentParser(description='lightweight application management')
    args = parser.parse_args(arg_vec)

# END
