import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/utils")

import boto
import zu_zoonrc.Zoonrc
import zu_Metroon.Metroon

def CloudFormation:

    def __init__(self, **kw_params):
        self.region = kw_params['region']
        self.stack_name = kw_params['name']
        self.size = kw_params['size']
        self.env = kw_params['env']
        self.mode = kw_params['mode']

        self.zoonrc = Zoonrc(deployment_environment=self.env)
        self.metroon = metroon(deployment_environment=self.env)
        self.conn = self._create_cf_connection()

    def create(self):
        self.conn.create_stack(
            self.stack_name,
            template_body=_template(), 
            parameters=_params(),
            capabilities=['CAPABILITY_IAM'],
            tags=None 
        )
        
    def delete(self):

    def update(self):

    def status(self):

    def _template(self):

    def _params(self):
        params = [
            {"ParameterKey": "KeyName"              ,     "ParameterValue": metroon.get(self.env + '-keypair')},
            {"ParameterKey": "Subnets"              ,     "ParameterValue": metroon.get(self.env + '-subnets')},
            {"ParameterKey": "AvailabilityZones"    ,     "ParameterValue": metroon.get(self.env + '-azs')},
            {"ParameterKey": "ClientSecurityGroup"  ,     "ParameterValue": metroon.get(self.env + '-clientsg')},
            {"ParameterKey": "ClusterSize"          ,     "ParameterValue": self.size },
            {"ParameterKey": "ClusterName"          ,     "ParameterValue": self.env } 
        ]
        if self.mode == "create":
            params.append({"ParameterKey": "AdminSecurityGroup"   ,     "ParameterValue": metroon.get(self.env + '-adminsg')})
            params.append({"ParameterKey": "VpcId"                ,     "ParameterValue": metroon.get(self.env + '-vpc')})
        return params

def _create_cf_connection(self):
    # Connect to a cloudformation
    conn = boto.cloudformation.connect_to_region(
                   self.region,
                   aws_access_key_id = zoonrc.aws['access_key'],
                   aws_secret_access_key = zoonrc.aws['secret_key'] 
    )
 
    return conn
