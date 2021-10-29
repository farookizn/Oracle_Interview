OCI infra creating a compute server with access via 8080/TCP from load balancer, and with port 22 from bastion compartment..

Requirements
An Oracle Cloud Infrastructure account. See Signing Up for Oracle Cloud Infrastructure.
A MacOS, Linux, or Windows computer.

Follow the below steps:

STEP 1:
*******
Create SSH Encryption Keys
Create ssh encryption keys to connect to your compute instance.

Open a terminal window:
MacOS or Linux: Open a terminal window in the directory where you want to store your keys.
Run the below command:
ssh-keygen -t rsa -N "" -b 2048 -C <your-ssh-key-name> -f <your-ssh-key-name>
  
Windows: Right-click on the directory where you want to store your keys (you can use puttygen for generating the key)

STEP 2:
******
Create a Virtual Cloud Network (VCN)
 Follow the steps here for VCN creation and to gather compatartment, oci id, subnet etc 
  https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/tf-compute/01-summary.htm
  
STEP 3
******  
The actual challenge terraform scripts , do the below
  
  Fill in the required details in terraform.tfvars.template
Rename terraform.tfvars.template to terraform.tfvars
Do 'terraform init'
Do 'terraform plan'
Do 'terrform apply'
Once done, Do 'terrform destroy'

