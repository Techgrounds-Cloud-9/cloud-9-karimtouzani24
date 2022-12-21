from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    
)
from constructs import Construct

Webserver_Vpc_AvailabilityZones = ["eu-central-1a", "eu-central-1b"] 
Webserver_Vpc_Ipaddresses = "10.10.10.0/24"
Webserver_Vpc_Subnet_name = "Public"
Webserver_Vpc_Subnet_mask = 25

Mngmt_Vpc_AvailabilityZones = ["eu-central-1a", "eu-central-1b"] 
Mngmt_Vpc_Ipaddresses = "10.20.20.0/24"
Mngmt_Vpc_Subnet_name = "Public"
Mngmt_Vpc_Subnet_mask = 25

class ProjectFinalStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ########## Creating web VPC and subnets##################################################################
        Web_vpc = ec2.Vpc(self, "WebVPC",
            availability_zones= Webserver_Vpc_AvailabilityZones,
            ip_addresses= ec2.IpAddresses.cidr(Webserver_Vpc_Ipaddresses),
            subnet_configuration= [ec2.SubnetConfiguration(
                name= Webserver_Vpc_Subnet_name,
                subnet_type= ec2.SubnetType.PUBLIC,
                cidr_mask= Webserver_Vpc_Subnet_mask)]
        )

        ########## Creating mngmt VPC and subnets##################################################################
        Mngmt_vpc = ec2.Vpc(self, "MngmtVPC",
            availability_zones= Mngmt_Vpc_AvailabilityZones,
            ip_addresses= ec2.IpAddresses.cidr(Mngmt_Vpc_Ipaddresses),
            subnet_configuration= [ec2.SubnetConfiguration(
                name= Mngmt_Vpc_Subnet_name,
                subnet_type= ec2.SubnetType.PUBLIC,
                cidr_mask= Mngmt_Vpc_Subnet_mask)]
        )

        ########## Creating the peering connection#################################################################
        VpcPeeringConnection= ec2.CfnVPCPeeringConnection(self, "VpcPeerConnection",
            peer_vpc_id= Web_vpc.vpc_id,
            vpc_id= Mngmt_vpc.vpc_id)

        for subnet in Web_vpc.public_subnets:
            VpcRouteW_M= ec2.CfnRoute(self, 
                id= f"{subnet.node.id} W_MRoute",
                route_table_id= subnet.route_table.route_table_id,
                destination_cidr_block= Mngmt_vpc.vpc_cidr_block,
                vpc_peering_connection_id= VpcPeeringConnection.attr_id)

        for subnet in Mngmt_vpc.public_subnets:
            VpcRouteM_W= ec2.CfnRoute(self, 
                id= f"{subnet.node.id} M_WRoute",
                route_table_id= subnet.route_table.route_table_id,
                destination_cidr_block= Web_vpc.vpc_cidr_block,
                vpc_peering_connection_id= VpcPeeringConnection.attr_id)

        ########## Creating NACL for the web servers ###########################################################

        ########## Creating NACL for the mngmt servers #########################################################

        ########## Creating Security Group for the web servers #################################################
        
        ########## Creating Security Group for the mngmt servers ###############################################