# %%
# Open the Codespace in your local VS Code

## terminal display path: /workspaces/daytwostuff

# %%
# Create a virtual environment 

# command for creating virtual environment: python -m venv .venv
# command for activation: $ source .venv/bin/activate
# Should you include the environment in your repo or not? --> no because the virtual environment is specific to my machine
# The terminal display path remains the same: /workspaces/daytwostuff but there is a (.venv) at the front showing that the virtual environment is active


# %%
# Viewing Data
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/MMiDS-textbook/MMiDS-textbook.github.io/refs/heads/main/utils/datasets/penguins-measurements.csv')

# %%
# Extension Management

# From the extension menu, the Data Wrangler extension was installed and enabled on my codespace
# 3 useful capabilities:
# 1. Provides a histogram of values for each column in the dataset
# 2. Shows summary statistics such as the min and max
# 3. Reveals the count of missing and unique values for each column in the dataset
# Overall the extension makes it really easy to view and understand the data and its characteristics


# %%
# Package Managing

# Version of plotly: 6.5.1
# We use a requirements.txt file is used to list the libraries and their respective versions that is needed for a python project. It's especially important when sharing projects across GitHub because the requirements file ensures consistency across different computer environments.
 








