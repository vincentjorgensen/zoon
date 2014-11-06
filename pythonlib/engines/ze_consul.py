import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/techs")

import zt_boto

class Consul:
  
  def __init__(self, args):
      self.args = args
