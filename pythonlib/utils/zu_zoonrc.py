import os
import yaml

class Zoonrc:

    def __init__(self, deployment_environment=None, zoonrc=os.environ['HOME'] + '/.zoonrc'):
        stream = open(zoonrc, 'r')
        config = yaml.load(stream)
        self.config = config
        default_environment = config['default_environment']
        if not deployment_environment:
            env = config['environments'][default_environment]
        else
            env = config['environments'][deployment_environment]
        self.env = env
        self.aws = { 
            'username'   : self.env['username'],
            'access_key' : self.env['aws_access_key'],
            'secret_key' : self.env['aws_secret_key']
        }

    def get_config(self):
        return self.config

    def get_aws_keys(self):
        return self.aws

    def get_description(self):
        return self.env['description']
