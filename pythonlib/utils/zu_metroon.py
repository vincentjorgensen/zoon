import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/utils")

import boto
import zu_zoonrc.Zoonrc

class Metroon:

    def __init__(self, deployment_environment=None):
        self.env = deployment_environment
        self.zoonrc = Zoonrc(deployment_environment=self.env)

        self.conn = self._create_ddb_connection()

        self.metroon = self.conn.get_table('Metroon')

    def get(self, item=None):
        return self.metroon.get_item('name',
        

    def _create_ddb_connection(self):
        conn = boto.dynamodb.connect_to_region(
                   self.region,
                   aws_access_key_id = zoonrc.aws['access_key'],
                   aws_secret_access_key = zoonrc.aws['secret_key']
    )
