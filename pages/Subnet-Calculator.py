import streamlit as st
from subnet_calculator import calculate_vlsm_subnets, calculate_flsm_subnets, format_subnet_info, parse_host_requirements
import math

st.title("Subnet Calculator Chatbot")
st.write("Please enter an IP address and CIDR notation to calculate the subnets.")

ip_address = st.text_input("IP Address", "192.168.1.0")
cidr = st.text_input("CIDR Notation", "24")
subnetting_type = st.selectbox("Subnetting Type", ["FLSM", "VLSM"])

if subnetting_type == "FLSM":
    num_subnets = st.number_input("Number of Subnets", min_value=1, value=2)
    if st.button("Calculate Subnets"):
        try:
            total_ips = 2 ** (32 - int(cidr))
            hosts_per_subnet = total_ips // num_subnets
            new_prefix = 32 - math.ceil(math.log2(hosts_per_subnet))

            subnets = calculate_flsm_subnets(ip_address, cidr, new_prefix)
            subnet_info = format_subnet_info(subnets)
            
            st.write(f"Subnets for {ip_address}/{cidr} with {num_subnets} subnets:")
            for idx, subnet in enumerate(subnet_info):
                st.write(f"Subnet {idx + 1}:")
                st.write(f"Network Address: {subnet['Network']}")
                st.write(f"Broadcast Address: {subnet['Broadcast']}")
                st.write(f"Prefix Length: {subnet['Prefix Length']}")
                st.write(f"Host Address Range: {subnet['Host Range']}")
        except ValueError as e:
            st.error(f"Error: {e}")

elif subnetting_type == "VLSM":
    host_requirements_input = st.text_area("Enter the required number of hosts per subnet (comma-separated):")
    host_requirements = parse_host_requirements(host_requirements_input)
    host_requirements.sort(reverse=True)
    if st.button("Calculate Subnets"):
        try:
            subnets = calculate_vlsm_subnets(ip_address, cidr, host_requirements)
            subnet_info = format_subnet_info(subnets)
            
            st.write(f"Subnets for {ip_address}/{cidr}:")
            for idx, subnet in enumerate(subnet_info):
                st.write(f"Subnet {idx + 1}:")
                st.write(f"Required Number of hosts: " + str(host_requirements[idx]))
                st.write(f"Network Address: {subnet['Network']}")
                st.write(f"Broadcast Address: {subnet['Broadcast']}")
                st.write(f"Prefix Length: {subnet['Prefix Length']}")
                st.write(f"Host Address Range: {subnet['Host Range']}")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    st._main_run_clExplicitRequestIdFlag = None  # type: ignore