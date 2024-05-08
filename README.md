# Advanced Project: QLORA & Tensor Parallelism
Welcome to the GitHub repository for the "Advanced Project - Enhancing Model Training Efficiency through Tensor Parallelism, Quantization, and Low-Rank Adaptation." This repository contains all necessary code and instructions to conduct three experiments aimed at improving model training efficiency.

## Repository Structure
This project is organized into three main experiments, each with its specific setup and purpose:

### Experiment 1: AWS Tensor Parallelism
**File Structure:**
- README.md
- sagemaker_exp_notebook.ipynb
- /shared_scripts

### Experiment 2: DeepSpeed Zero Stage3 with LORA
**File Structure:**
- README.md
- sagemaker_exp2_notebook.ipynb
- /src/train

### Experiment 3: DeepSpeed Zero Stage3 with QLORA
**File Structure:**
- README.md
- sagemaker_exp3_notebook.ipynb
- /src/train

## Setup Instructions

### Launching SageMaker Notebook
To start your experiments using AWS SageMaker, follow these steps:
1. **Log In**: Access your AWS console and navigate to the SageMaker service.
2. **Start an Instance**: Launch a SageMaker notebook instance.
3. **Open Interface**: Once the instance is running, open the Jupyter or JupyterLab interface from the SageMaker dashboard.

### Running Experiments
Each experiment is designed to run on the AWS SageMaker platform using `ml.p4d.24xlarge` instances. Ensure your notebook instance has access to the necessary training scripts.

### Configuration and Execution
Utilize the provided Jupyter notebooks in conjunction with the deepspeed `config.yaml` files to execute various configurations of the experiments. Detailed instructions for each experiment are included in their respective README.md files.

## Additional Notes
Make sure to review each experiment’s specific README for detailed setup and execution instructions. Adjust your SageMaker settings according to the requirements of the tasks to optimize resource usage and cost efficiency.


