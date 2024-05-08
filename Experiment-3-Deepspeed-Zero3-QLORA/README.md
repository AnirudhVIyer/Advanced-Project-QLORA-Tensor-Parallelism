# Experiment 3 : Experiment Setup Using DeepSpeed and QLORA

This experiment leverages the DeepSpeed library to establish a distributed training environment. We utilize the Accelerate library to facilitate the configuration and execution of the DeepSpeed setup as defined in the qlora.yaml configuration file. We finetune a Llama2 model on a instruction following dataset.

## Setup Instructions

### Step 1: Launch SageMaker Notebook
- Log in to your AWS console and navigate to the SageMaker service.
- Start a SageMaker notebook instance.
- Once the instance is running, open the Jupyter/JupyterLab interface from the SageMaker dashboard.

### Step 2: Prepare the Environment
- Clone the repository with the experiment scripts to your notebook instance environment. If you do not have a specific repository, you can upload the scripts manually.
- Navigate to the `/src/train` directory where the scripts are located.

### Step 3: Configuration Files:
- Review and modify the qlora.yaml file to set up the DeepSpeed configuration. 
- The number of GPUs can be adjusted using the `num_process` field in the qlora.yaml file.

## Modifying Training Parameters

- **Hyperparameters:** You can adjust the training hyperparameters directly within the notebook to tune the performance of your model.
- **LORA Configuration:** To alter the Low Rank Adaptation (LORA) settings or to remove LORA configurations altogether change the hyperparameters setting in the notebook 
- **QLORA Configuration:**  To alter the Quantization settings or to remove Quantization altogether change the hyperparameters setting in the notebook
- **Selecting the model - Specify the model - successfully run with Llama7b and Llama13b

### Step 3: Run the Experiment
- Open the `sagemaker_exp3_notebook.ipynb` notebook.
- Execute the cells sequentially to initialize the experiment setup and start the training process.


## Additional Notes
- Ensure that your AWS account has sufficient permissions and resource limits to create and run SageMaker notebook instances and perform distributed training.
- Monitor the experiment’s progress directly through the notebook interface and AWS CloudWatch to understand resource utilization and training metrics.
- If you have to add any further packages or update old ones, do a subprocess pip install in the accelerate.py file before the distributed environment is setup.

For any issues or further assistance, refer to the AWS SageMaker documentation or contact the support team.
