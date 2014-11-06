import os
import yaml

class Zoonrc(Object):

    def __init__(self, zoonrc=os.environ['HOME'] + '/.zoonrc'):
        stream = open(zoonrc, 'r')
        config = yaml.load(stream)
        self.config = config
        default_environment = config['default_environment']
        env = config['environments'][default_environment]
        self.env = env

    def get_config(self):
        return self.config

    def get_aws_keys(self):
        return { 
            'username'       : self.env['username'],
            'aws_access_key' : self.env['aws_access_key'],
            'aws_secret_key' : self.env['aws_secret_key']
        }

    def get_description(self):
        return self.env['description']
