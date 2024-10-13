import streamlit as st
import math
from fractions import Fraction

# Streamlit header and subheader for the web interface
st.title("Scientific Calculator")
st.write("Welcome to the web-based scientific calculator!")

# List of operations to display in a dropdown
operations = ['Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)', 
              'Modulus (%)', 'Exponentiation (^)', 'Square Root (sqrt)', 
              'Logarithm (log)', 'Sine (sin)', 'Cosine (cos)', 'Tangent (tan)', 
              'Factorial (fact)']

# Dropdown for selecting operation
operation = st.selectbox("Choose an operation:", operations)

# Based on the operation, get the necessary inputs
if operation in ['Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)', 
                 'Modulus (%)', 'Exponentiation (^)']:
    num1 = st.number_input("Enter the first number", value=0.0, format="%.5f")
    num2 = st.number_input("Enter the second number", value=0.0, format="%.5f")

elif operation in ['Square Root (sqrt)', 'Logarithm (log)', 'Sine (sin)', 
                   'Cosine (cos)', 'Tangent (tan)', 'Factorial (fact)']:
    num1 = st.number_input("Enter the number", value=0.0, format="%.5f")
    if operation == 'Sine (sin)' or operation == 'Cosine (cos)' or operation == 'Tangent (tan)':
        num1 = st.number_input("Enter the angle in degrees", value=0.0, format="%.5f")

# Compute the result based on the selected operation
if st.button('Calculate'):
    if operation == 'Addition (+)':
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")

    elif operation == 'Subtraction (-)':
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")

    elif operation == 'Multiplication (*)':
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")

    elif operation == 'Division (/)':
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.write("Error: Division by zero!")

    elif operation == 'Modulus (%)':
        result = num1 % num2
        st.write(f"Result: {num1} % {num2} = {result}")

    elif operation == 'Exponentiation (^)':
        result = num1 ** num2
        st.write(f"Result: {num1} ^ {num2} = {result}")

    elif operation == 'Square Root (sqrt)':
        if num1 >= 0:
            result = math.sqrt(num1)
            st.write(f"Result: sqrt({num1}) = {result}")
        else:
            st.write("Error: Square root of a negative number!")

    elif operation == 'Logarithm (log)':
        if num1 > 0:
            result = math.log10(num1)
            st.write(f"Result: log({num1}) = {result}")
        else:
            st.write("Error: Logarithm of a non-positive number!")

    elif operation == 'Sine (sin)':
        result = math.sin(math.radians(num1))
        st.write(f"Result: sin({num1}°) = {result} or approximately {Fraction(result).limit_denominator()}")

    elif operation == 'Cosine (cos)':
        result = math.cos(math.radians(num1))
        st.write(f"Result: cos({num1}°) = {result} or approximately {Fraction(result).limit_denominator()}")

    elif operation == 'Tangent (tan)':
        result = math.tan(math.radians(num1))
        st.write(f"Result: tan({num1}°) = {result} or approximately {Fraction(result).limit_denominator()}")

    elif operation == 'Factorial (fact)':
        if num1 >= 0 and num1 == int(num1):
            result = math.factorial(int(num1))
            st.write(f"Result: factorial({int(num1)}) = {result}")
        else:
            st.write("Error: Factorial is only defined for non-negative integers!")

