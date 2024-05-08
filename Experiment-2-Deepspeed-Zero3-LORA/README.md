# Experiment 2 : Experiment Setup Using DeepSpeed and LORA

This experiment leverages the DeepSpeed library to establish a distributed training environment. We utilize the Accelerate library to facilitate the configuration and execution of the DeepSpeed setup as defined in the ds_zero3.yaml configuration file. We train a T5 model on a DialogueSum dataset.

## Setup Instructions

### Step 1: Launch SageMaker Notebook
- Log in to your AWS console and navigate to the SageMaker service.
- Start a SageMaker notebook instance.
- Once the instance is running, open the Jupyter/JupyterLab interface from the SageMaker dashboard.

### Step 2: Prepare the Environment
- Clone the repository with the experiment scripts to your notebook instance environment. If you do not have a specific repository, you can upload the scripts manually.
- Navigate to the `/src/train` directory where the scripts are located.

### Step 3: Configuration Files:
- Review and modify the ds_zero3.yaml file to set up the DeepSpeed configuration. 
- The number of GPUs can be adjusted using the `num_process` field in the ds_zero.yaml file. In the notebook training search for `world_size` to verify

## Modifying Training Parameters

- **Hyperparameters:** You can adjust the training hyperparameters directly within the notebook to tune the performance of your model.
- **LORA Configuration:** To alter the Low Rank Adaptation (LORA) settings or to remove LORA configurations altogether, modify the src/train/train.py script according to your requirements.
- **Selecting the model - Specify the T5 - Large or T5 - XL model to be used in the notebook.

### Step 3: Run the Experiment
- Open the `sagemaker_exp2_notebook.ipynb` notebook.
- Execute the cells sequentially to initialize the experiment setup and start the training process.


## Additional Notes
- Ensure that your AWS account has sufficient permissions and resource limits to create and run SageMaker notebook instances and perform distributed training.
- Monitor the experiment’s progress directly through the notebook interface and AWS CloudWatch to understand resource utilization and training metrics.
- If you have to add any further packages or update old ones, do a subprocess pip install in the accelerate.py file before the distributed environment is setup.

For any issues or further assistance, refer to the AWS SageMaker documentation or contact the support team.
