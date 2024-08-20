# Subnet Calculator with Streamlit

This repository contains a simple Streamlit-based application for subnet calculation, supporting both Fixed-Length Subnet Masking (FLSM) and Variable-Length Subnet Masking (VLSM). The application allows users to input an IP address and subnet requirements to calculate subnets based on their needs.

## Features

- **FLSM (Fixed-Length Subnet Masking)**: Enter the number of subnets required, and the app will calculate and display the subnets.
- **VLSM (Variable-Length Subnet Masking)**: Enter the number of hosts required per subnet, and the app will calculate the most efficient subnets, sorted from largest to smallest.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Step-by-Step Guide

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/subnet-calculator.git
   cd subnet-calculator

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. 
