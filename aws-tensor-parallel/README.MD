# Experiment 1: AWS Tensor Parallelism

This experiment leverages AWS SageMaker training instances to set up a distributed training environment using Tensor Parallelism. Follow the instructions below to configure and run the experiment.

## Setup Instructions

### Step 1: Launch SageMaker Notebook
- Log in to your AWS console and navigate to the SageMaker service.
- Start a SageMaker notebook instance.
- Once the instance is running, open the Jupyter/JupyterLab interface from the SageMaker dashboard.

### Step 2: Prepare the Environment
- Clone the repository with the experiment scripts to your notebook instance environment. If you do not have a specific repository, you can upload the scripts manually.
- Navigate to the `/shared/scripts` directory where the scripts are located.

### Step 3: Run the Experiment
- Open the `sagemaker_exp_notebook.ipynb` notebook.
- Execute the cells sequentially to initialize the experiment setup and start the training process.

## Configuring the Experiment

Within the `sagemaker_exp_notebook.ipynb`, you have the ability to control various aspects of the training process:

- **Hyperparameters**: Set and adjust the hyperparameters related to the training process, including learning rate, batch size, etc.
- **Tensor Parallelism Degree**: Specify the degree of Tensor Parallelism to tailor the distributed training process according to your computational resource availability and requirements.

## Additional Notes
- Ensure that your AWS account has sufficient permissions and resource limits to create and run SageMaker notebook instances and perform distributed training.
- Monitor the experiment’s progress directly through the notebook interface and AWS CloudWatch to understand resource utilization and training metrics.






