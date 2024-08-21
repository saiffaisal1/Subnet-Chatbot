import streamlit as st

st.set_page_config(
    page_title="Subnetting App"
)

st.title(" Home Page ")

st.markdown("  What is Subnetting?  ")
st.markdown(" Subnetting is creating networks within a network for hosting multiple devices. Subnetting uses host bits and network bits to make any number of subnets of a network.  ")

st.markdown(" What is VLSM? ")
st.markdown(" Variable Length Subnet Masking is a subnetting technique that allows network admins to allocate IP addresses more efficiently using different subnet masks for different network segments. ")

st.markdown(" What is FLSM? ")
st.markdown(" Fixed Length Subnet masking is a subnetting technique to divide a 256 IP header into four equal sized subnets. ")

st.markdown(" Difference between VLSM and FLSM ")
st.markdown(" In VLSM, a network is divided into different sized subnets. In FLSM, one network is divided into mutliple equal-sized subnets. ")
st.markdown(" In VLSM, each subnet contains an equal number of hosts. In FLSM, the number of hosts per subnet varies. ")

st.title(" Instructions of Use ")

st.markdown(" There are 2 apps dedicated to learning the concepts of Subnetting IP addresses: ")
st.markdown(" 1. Subnet-Calculator: This app helps you calculate the subnets of any IP address with any given CIDR using VLSM and FLSM. ")
st.markdown(" 2. Subnet-Chatbot: This app helps you ask questions regarding Subnetting IP addresses using a Chatbot. ")

st.title(" More Information ")

st.markdown(" This Project is open source and provides the instructions on how to setup the app and how to cater the app for your Subnetting needs. :)")
st.link_button("Access GitHub", "https://github.com/saiffaisal1/Subnet-Chatbot")

st.divider()
st.write(" Created by Saif Faisal and Zafar Shaikh. 2024 ")
