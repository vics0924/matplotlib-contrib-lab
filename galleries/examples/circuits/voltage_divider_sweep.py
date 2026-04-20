"""
Voltage Divider Sweep
====================

This example demonstrates the output voltage of a voltage divider circuit as the load resistor (R2) is swept over a range of values. The voltage divider is a fundamental circuit in electronics, used to scale down voltages. Here, we plot Vout as a function of R2 for a fixed input voltage (Vin) and series resistor (R1).

- Vin is set to 5V.
- R1 is fixed at 1 kOhm.
- R2 is swept logarithmically from 100 Ohms to 100 kOhms.

The plot shows how the output voltage approaches Vin as R2 increases, and approaches 0 as R2 decreases.
"""

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# Set circuit parameters
Vin = 5.0  # Input voltage in volts
R1 = 1e3   # Series resistor in ohms (1 kOhm)

# Generate a logarithmic sweep of R2 values
R2 = np.logspace(1, 10000, 200)  # 100 Ohms to 100 kOhms

# Calculate output voltage for each R2
Vout = Vin * R2 / (R1 + R2)

# Create the plot
plt.figure(figsize=(7, 4))  # Indentation: create a new figure with specified size
plt.semilogx(R2, Vout, label='Vout vs R2')  # Indentation: plot Vout vs R2 on a log scale for R2

# Label axes and add title
plt.xlabel('R2 (Ohms)')  # Indentation: label the x-axis
plt.ylabel('Vout (V)')   # Indentation: label the y-axis
plt.title('Voltage Divider Output vs. Load Resistance')  # Indentation: add a plot title

# Add grid and legend
plt.grid(True, which='both', ls='--', alpha=0.6)  # Indentation: add a grid for readability
plt.legend()  # Indentation: show the legend

# Adjust layout and display the plot
plt.tight_layout()  # Indentation: adjust layout to prevent overlap
plt.show()  # Indentation: display the plot