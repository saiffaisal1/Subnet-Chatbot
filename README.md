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
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run Homepage.py
   ```

   This will launch the application in your default web browser. You can access it at `http://localhost:8501/`.

## Usage

1. **FLSM (Fixed-Length Subnet Masking)**:
   - Enter an IP address and select the CIDR.
   - Specify the number of subnets required.
   - Click on "Calculate FLSM Subnets" to view the results.

2. **VLSM (Variable-Length Subnet Masking)**:
   - Enter an IP address and select the CIDR.
   - Specify the number of hosts required per subnet, separated by commas or spaces.
   - Click on "Calculate VLSM Subnets" to view the results.

## Modifying the Code

### Folder Structure

- **`Homepage.py`**: The main Streamlit app script that provides the user interface and handles user input.
- **`Subnet-Calculator.py`**: A Streamlit page that provides the user with the subnetting calculator.
- **`subnet_calculator.py`**: Contains the core functions for calculating subnets using FLSM and VLSM.
- **`Subnet-Chatbot.py`**: A Streamlit page that provides the user with a ChatGPT like UI where they can interact with the AI to learn about subnetting.

### Adding New Features

1. **Modify `subnet_calculator.py`**:
   - Add new calculation logic or enhance existing functions.
   
2. **Update `Homepage.py`**:
   - Adjust the Streamlit UI to accommodate any changes to the calculation logic.
   - Ensure that new input fields or options are correctly handled and passed to the calculation functions.

3. **Test Your Changes**:
   - Run the application using `streamlit run Homepage.py` to verify your changes.

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.

## Contact

For any questions or feedback, feel free to reach out to [sf9441@rit.edu](mailto:sf9441@rit.edu) or [zas7030@rit.edu](mailto:zas7030@rit.edu).