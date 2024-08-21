import ipaddress
import math

def parse_host_requirements(input_string):
    host_list = input_string.replace(",", " ").split()
    return [int(hosts) for hosts in host_list if hosts.isdigit()]

def calculate_vlsm_subnets(ip, cidr, host_requirements):
    host_requirements.sort(reverse=True)
    
    network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    subnets = []
    
    for hosts in host_requirements:
        required_hosts = hosts + 2 
        required_bits = math.ceil(math.log2(required_hosts))
        new_prefix = 32 - required_bits
        
        if new_prefix <= network.prefixlen:
            raise ValueError("Not enough space for the requested subnet sizes")
        
        try:
            subnet = next(network.subnets(new_prefix=new_prefix))
            subnets.append(subnet)
            network = next(network.address_exclude(subnet)) 
        except StopIteration:
            raise ValueError("Not enough space for the requested subnet sizes")
    
    return subnets

def calculate_flsm_subnets(ip, cidr, new_prefix):
    network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    return list(network.subnets(new_prefix=new_prefix))

def format_subnet_info(subnets):
    subnet_info = []
    for subnet in subnets:
        # Directly calculate first and last usable hosts without generating all hosts
        first_host = subnet.network_address + 1
        last_host = subnet.broadcast_address - 1
        subnet_info.append({
            "Network": str(subnet.network_address),
            "Broadcast": str(subnet.broadcast_address),
            "Prefix Length": subnet.prefixlen,
            "Host Range": f"{first_host} - {last_host}"
        })
    return subnet_info