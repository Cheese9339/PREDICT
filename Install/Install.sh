#!/bin/bash

echo "Installing at: $PWD"
echo "conda base path:$CONDA_BASE"
cd $PWD

# Ensure Conda is available
if [ ! -f "${CONDA_BASE}/etc/profile.d/conda.sh" ]; then
    echo "Conda not found at ${CONDA_BASE}. Please check Conda installation."
    exit 1
fi

source "${CONDA_BASE}/etc/profile.d/conda.sh"

# Check for required files
ENV_NAME="PREDICT"

if [ ! -f "PREDICT.yml" ]; then
    echo "Error: PREDICT.yml not found in current directory."
    exit 1
fi

if [ ! -f "R_Packages.R" ]; then
    echo "Error: R_Packages.R not found in current directory."
    exit 1
fi

# Create Conda environment
echo "Creating Conda environment: ${ENV_NAME}..."
conda env create -f PREDICT.yml

if [ $? -ne 0 ]; then
    echo "Failed to create environment. Check PREDICT.yml or Conda setup."
    exit 1
fi

# Activate Conda environment
echo "Activating Conda environment: ${ENV_NAME}..."
conda activate ${ENV_NAME}

if [ $? -ne 0 ]; then
    echo "Failed to activate environment ${ENV_NAME}."
    exit 1
fi

# Install R packages
echo "Running R_Packages.R to install R packages..."
Rscript R_Packages.R

if [ $? -ne 0 ]; then
    echo "Failed to install R packages. Check R_Packages.R or R setup."
    exit 1
fi

# Delete .gitkeep files
echo "Environment setup complete! ${ENV_NAME} created and all packages installed."
find "$PWD/../" -name ".gitkeep" -type f -delete

echo "Activate the environment with:"
echo "conda activate ${ENV_NAME}"
