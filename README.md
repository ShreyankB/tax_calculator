# Streamlit Income Tax Calculator

This project is a Streamlit application that calculates income tax based on user input. It allows users to enter their annual income, NPS investment percentage, and basic salary percentage to compute their taxable income and total tax payable.

## Project Structure

```
streamlit-tax-app
├── src
│   ├── calc.py        # Contains the logic for calculating income tax
│   └── app.py         # Entry point for the Streamlit application
├── requirements.txt    # Lists the dependencies required for the project
└── README.md           # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-tax-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Features

- Input for annual income
- Input for NPS investment percentage
- Input for basic salary percentage
- Calculation of taxable income and total tax payable

## License

This project is licensed under the MIT License - see the LICENSE file for details.