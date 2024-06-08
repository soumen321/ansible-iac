There are so many tools in market like Puppet, Chef, Salt etc. but

#Why Ansible ?

Ansible is an open source automation engin which help us for -

• Provisioning (EC2 / S3 etc)

• Configuration Management (Virtual Machine configuration)

• Orchestration - Deployment using CI/CD (Like K8S deployment)

• Network Automation (Like VLAN Automation)

Ansible written in Python, the project benefits from the experience and intelligence of its thousands of contributors.

#Ansible follow Master - Slave Architecture, in ansible term it is

Control Node(Master) - The m/c that to install ansible softwate called as control node.

Manage Node(Slave) - All the m/c i.e target machine , using which managing the confguration called manage node.

Advantages :

Agentless -> No need to install any agent in host machine, passwordless communication ->

YAML ( a human readable data serialization language)

Push base mechanism

Ansible Vs Terraform -> both are use for automation

Terraform : Infrastructure Provisioning Tool e.g. create EC2, S3 bucket, EKS cluster, VPC etc.

Ansible : Infrastructure Configuration Tool e.g. update servers, install software, patches update etc.

Why Ansible is so Popular Tool ?

IaC tool like :

Puppet - Own declarative languge.

Salt - Python

Chef - Ruby -> use Agent -> means a angent need to install in manage node and agent can communicate with control node and also pull base mechanism

ANSIBLE -

1. Agent less 
2. Push base mechnism 
3. Large communit ans contributor
4. RedHat Support
5. Support YAML 
6. Automation 
7. Ansible GALAXY (like docker hub in ansible galaxy you can use for contribute module or you yan use other contributor module.)

Installation :

Linux Support [Windows WSL]

Pre requisite : Python

Link : ttps://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

1. Create ec2 instance with pem key

a node for control node [for installation ansible, you can create ur own m/c as control node] and other nodes where to update/ istall software i.e manage node.

Password less Authentication, no need to touch manage node.

ssh-keygen -t rsa

ssh-copy-id -f "-o IdentityFile ~/pem-key/test-new.pem"ubuntu@18.205.233.146

Will show on screen: ssh -o ' IdentityFile ~/pem-key/test-new.pem' 'ubuntu@18.205.233.146'

Put the command ssh -o ' IdentityFile ~/pem-key/test-new.pem' 'ubuntu@18.205.233.146'

exit

sshubuntu@18.205.233.146

connect , done!

you need to setup a inventory which is a file i.e contails group i.e server group under this set ip of the manage server.

got to -> vim /etc/ansible/host -> set it

[servers] -> group

server_1 ansible_host=18.205.233.146 -> manage node ip/s

[servers:vars]

ansible_user=ubuntu ansible_python_interpreter=/usr/bin/python3

ansible_ssh_private_key_file=/home/soumen321/pem-key/test-new.pem

or you can just create a inventory file in like iniventory.ini and set

[web]

ubuntu@12.123.123.123

[db]

ubuntu@12.123.123.123

ansible -i inventory.ini -m ping all