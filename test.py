response = """
FLSM is a subnetting method where each subnet has the same size, meaning that each subnet has the same number of available host addresses. 
This approach simplifies the design and management of networks but may lead to inefficient use of IP addresses.

Key Features of FLSM:
- Uniform Subnet Sizes: All subnets have the same number of hosts. For example, if the subnet mask is /24, each subnet can accommodate 256 IP addresses (254 usable hosts).
- Simplicity: Easier to implement and manage, especially for smaller networks.
- Wastage of IP Addresses: May lead to unused IP addresses in subnets that do not require the maximum number of hosts.

Example of FLSM:
Given a network 192.168.1.0/24:
Divided into 4 subnets using /26:
- 192.168.1.0/26 (Hosts: 192.168.1.1 to 192.168.1.62)
- 192.168.1.64/26 (Hosts: 192.168.1.65 to 192.168.1.126)
- 192.168.1.128/26 (Hosts: 192.168.1.129 to 192.168.1.190)
- 192.168.1.192/26 (Hosts: 192.168.1.193 to 192.168.1.254)
""" 
for word in response.split():
    print(word)
 
                    