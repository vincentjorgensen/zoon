import os
import sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/pythonlib/utils")

import boto
import zu_zoonrc.Zoonrc
import zu_Metroon.Metroon

def CloudFormation:

    def __init__(self, **kw_params):
        self.region = kw_params['region']
        self.stack_name = kw_params['stack_name']
        self.app_name = kw_params['app_name']
        self.app_type = kw_params['app_type']
        self.size = kw_params['size']
        self.env = kw_params['env']
        self.mode = kw_params['mode']
        self.stack_name = self.region + '-' + self.app_type + '-' + self.app_name

        self.zoonrc = Zoonrc(deployment_environment=self.env)
        self.metroon = metroon(deployment_environment=self.env)
        self.conn = self._create_cf_connection()

        if self.region in ['us-east-1','us-west-1','us-west-2','eu-west-1']:
            self.azs = 3
        else:
            self.azs = 2
        self.azsize = self.size/self.azs

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
        template={
          "Parameters" = {},
          "Mappings" = {},
          "Resources" = {}
        }
        parameters = [
          ("KeyName", "String"), 
          ("AvailabilityZoneA", "CommaDelimitedList"),
          ("AvailabilityZoneB", "CommaDelimitedList"),
          ("ClientSecurityGroup", "String"),
          ("AZSize","Number"),
          ("AvailabilityZoneC","CommaDelimitedList"),
          ("AZSize","Number"),
          ("ConsulDataCenter","String"),
          ("ConsulEndpoint","String"),
          ("DeployEnv","String"),
          ("ClusterName","String"),
          ("VPCName","String"),
          ("SubnetA","CommaDelimitedList"),
          ("SubnetB","CommaDelimitedList")
          ("InstanceType","String")
        ]

        if self.azs == 3:
          parameters.append(("AvailabilityZoneC", "CommaDelimitedList"))
          pramaters.append(("SubnetC","CommaDelimitedList"))

        if self.mode == "create":
          parameters.append(("AdminSecurityGroup", "String"))
          parameters.append(("VPCName", "String"))

       for tup in parameters:
        template['Parameters'][tup[0]] = {"Type": tup[1]}

        mappings = {
          "RegionToAmi" = {},
          "AwsAccountMap": {
            "076336089575": {
              "Bucket": "spongecell-devops"
            }
          }
        }

       # Supported regions format:
       # 
       supportedregions = metroon.get(self.env + '-supportedregions')

       for reg in supportedregions:
           mappings['RegionToAmi'][reg] = metroon.get(self.env + '-' + reg + '-hvm')



    def _params(self):
        params = [
            {"ParameterKey": "KeyName"              ,     "ParameterValue": metroon.get(self.env + '-keypair')},
            {"ParameterKey": "SubnetA"              ,     "ParameterValue": metroon.get(self.env + '-subnetA')},
            {"ParameterKey": "SubnetB"              ,     "ParameterValue": metroon.get(self.env + '-subnetB')},
            {"ParameterKey": "AvailabilityZoneA"    ,     "ParameterValue": metroon.get(self.env + '-azA')},
            {"ParameterKey": "AvailabilityZoneB"    ,     "ParameterValue": metroon.get(self.env + '-azB')},
            {"ParameterKey": "ClientSecurityGroup"  ,     "ParameterValue": metroon.get(self.env + '-clientsg')},
            {"ParameterKey": "DeployEnv          "  ,     "ParameterValue": self.env },
            {"ParameterKey": "AZSize"               ,     "ParameterValue": self.azsize },
            {"ParameterKey": "ClusterName"          ,     "ParameterValue": self.env } 
        ]
        if self.azs == 3:
            params.append({"ParameterKey": "SubnetC"              ,     "ParameterValue": metroon.get(self.env + '-subnetC')})
            params.append({"ParameterKey": "AvailabilityZoneC"    ,     "ParameterValue": metroon.get(self.env + '-azC')})

        if self.mode == "create":
            params.append({"ParameterKey": "AdminSecurityGroup"   ,     "ParameterValue": metroon.get(self.env + '-adminsg')})
            params.append({"ParameterKey": "VPCName"              ,     "ParameterValue": metroon.get(self.env + self.region + '-vpcname')})

        return params

def _create_cf_connection(self):
    # Connect to a cloudformation
    conn = boto.cloudformation.connect_to_region(
                   self.region,
                   aws_access_key_id = zoonrc.aws['access_key'],
                   aws_secret_access_key = zoonrc.aws['secret_key'] 
    )
 
    return conn
