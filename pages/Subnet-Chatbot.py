import streamlit as st
import shelve

st.title("Subnetting Chatbot")
st.markdown("Note: This Chatbot is not an AI model and works on given prompts.")

# Load chat history to shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])
    if st.button("Save Chat History"):
        save_chat_history(st.session_state.messages)

# Loads the chat history after app rerun
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

response = """ Hello there! I can explain any Subnetting terms to help you understand better. 
               Prompts like Subnetting, CIDR, IP Address, VLSM etc works."""

with st.chat_message("assistant"):
    st.write(response)
# Streamed response emulator
def response_generator():
        match prompt:
            case "Subnetting":
                response = """
                Subnetting is a technique used in computer networking to divide a single network into smaller, manageable sub-networks, or subnets. 
                This process helps to improve network performance and security by organizing and isolating network traffic."""  
                yield response
            
            case "IP Address":
                response = """
                IP Address: An identifier for a device on a network, composed of two main parts: 
                Network Portion: Identifies the specific network. 
                Host Portion: Identifies the specific device on that network.""" 
                yield response
            
            case "FLSM":
                response = """
                FLSM is a subnetting method where each subnet has the same size, meaning that each subnet has the same number of available host addresses. 
                This approach simplifies the design and management of networks but may lead to inefficient use of IP addresses.

                Key Features of FLSM:
                - Uniform Subnet Sizes: All subnets have the same number of hosts. For example, if the subnet mask is /24, each subnet can accommodate 256 IP addresses (254 usable hosts).
                - Simplicity: Easier to implement and manage, especially for smaller networks.
                - Wastage of IP Addresses: May lead to unused IP addresses in subnets that do not require the maximum number of hosts.

                Example of FLSM:
                - Given a network 192.168.1.0/24:
                - Divided into 4 subnets using /26:
                - 192.168.1.0/26 (Hosts: 192.168.1.1 to 192.168.1.62)
                - 192.168.1.64/26 (Hosts: 192.168.1.65 to 192.168.1.126)
                - 192.168.1.128/26 (Hosts: 192.168.1.129 to 192.168.1.190)
                - 192.168.1.192/26 (Hosts: 192.168.1.193 to 192.168.1.254)
                """ 
                yield response

            case "VLSM":    
                response = """
                VLSM is a more advanced subnetting method that allows for subnets of different sizes within the same network. 
                This technique enables more efficient use of IP addresses by allocating subnet sizes based on specific network requirements.
                
                Key Features of VLSM:
                - Variable Subnet Sizes: Subnets can have different numbers of hosts. This allows for better utilization of available IP addresses. 
                - Efficient IP Address Usage: Reduces wastage by allocating only the necessary number of addresses for each subnet. 
                - Complexity: More complicated to implement and manage compared to FLSM, as it requires careful planning and calculation. 

                Example of VLSM:
                - Given a network 192.168.1.0/24: 
                - Divided into various subnets based on requirements: 
                - 192.168.1.0/26 (Hosts: 192.168.1.1 to 192.168.1.62) for a department with 60 hosts. 
                - 192.168.1.64/27 (Hosts: 192.168.1.65 to 192.168.1.94) for a smaller group with 30 hosts. 
                - 192.168.1.96/28 (Hosts: 192.168.1.97 to 192.168.1.110) for an even smaller group with 14 hosts.""" 
                yield response

            case "CIDR":    
                response = """
                CIDR (Classless Inter-Domain Routing): A method for allocating IP addresses and IP routing that replaces the traditional class-based method. 
                CIDR notation uses a slash followed by the number of bits in the subnet mask (eg, /24). """ 
                yield response
        
            case "Subnet Mask":    
                response = """
                Subnet Mask: A 32-bit number that divides the IP address into the network and host portions. 
                It defines which part of the address refers to the network and which part refers to the host.""" 
                yield response
            
            case "Bye":
                response = "Bye! :)"
                yield response

if prompt := st.chat_input("Please enter a Subnetting term"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


