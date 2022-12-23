import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
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
        Web_SG= ec2.SecurityGroup(self, "Web_SG",
            vpc= Web_vpc,
            security_group_name= "SG_web",
            allow_all_outbound= True,
            description= "Webserver Security Group")

        Web_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(),
            connection= ec2.Port.tcp(22),
            description= "allow SSH webserver"
        )

        Web_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(),
            connection= ec2.Port.tcp(80),
            description= "allow HTTP webserver"
        )

        Web_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(),
            connection= ec2.Port.tcp(443),
            description= "allow HTTPS webserver"
        )
        ########## Creating Security Group for the mngmt servers ###############################################
        Mngmt_SG= ec2.SecurityGroup(self, "Mngmt_SG",
            vpc= Mngmt_vpc,
            security_group_name= "SG_Mngmt",
            allow_all_outbound= True,
            description= "Mngmt server Security Group"
        )

        Mngmt_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(),
            connection= ec2.Port.tcp(22),
            description= "allow SSH Mngmt server"
        )

        Mngmt_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(),
            connection= ec2.Port.tcp(3389),
            description= "allow RDP Mngmt server"
        )

        ########## test S3 bucket###############################################################################
        Ud_bucket= s3.Bucket(self, "ud_bucket", #S3 bucket created
            bucket_name= "ud-bucket-project",
            # encryption=,
            versioned= True,
            removal_policy= cdk.RemovalPolicy.DESTROY,
            auto_delete_objects= True)

        Ud_upload_s3= s3deploy.BucketDeployment(self, "deployS3", #the userdata file is uploaded in the S3 bucket.
            sources= [s3deploy.Source.asset("./asset_folder")],
            destination_bucket= Ud_bucket)

        Ud_webserver= ec2.UserData.for_linux()
        Ud_webserver.add_s3_download_command(
            bucket= Ud_bucket,
            bucket_key= "userdata.sh") #the userdata is downloaded to the instance
        Ud_webserver.add_execute_file_command(file_path= r"./userdata.sh") # not working!

        role_test= iam.Role(self, "role_test",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description= "test webserver role",)
        
        Ud_bucket.grant_read_write(role_test)

        ########## test instance ###############################################################################
        web_AMI = ec2.MachineImage.latest_amazon_linux(
            cpu_type= ec2.AmazonLinuxCpuType.X86_64,
            edition= ec2.AmazonLinuxEdition.STANDARD,
            generation= ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            storage= ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            )
        
        web_instance = ec2.Instance(self, "web_instance_test",
            instance_type= ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            vpc= Web_vpc,
            availability_zone= Webserver_Vpc_AvailabilityZones[1],
            instance_name= "Testing web instance",
            machine_image= web_AMI,
            key_name= "Karim_KP",
            security_group= Web_SG,
            user_data= Ud_webserver,
            role= role_test
            # block_devices=)     
        )
        
        