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

## Results Summary

### Experiment 1 — AWS Tensor Parallelism (LLaMA 7B, GLUE-SST2)

| GPUs | Per Epoch Training Time (s) | Total Run Time (s) | Val Loss |
|------|----------------------------|-------------------|----------|
| 2    | 697                        | 1291              | 1.8261   |
| 4    | 377                        | 1084              | 1.5351   |
| 8    | 291                        | 754               | 1.3843   |

**Speedup: 2.39x going from 2 to 8 GPUs**

---

### Experiment 2 — DeepSpeed Zero3 + LoRA (FlanT5 Large & XL)

| Config    | Total Run Time (s) | Per Epoch (s) | Val Loss |
|-----------|--------------------|---------------|----------|
| 2-LORA    | 5636               | 2082          | 1.1260   |
| 2-Plain   | OOM                | OOM           | OOM      |
| 4-LORA    | 3144               | 1062          | 0.9727   |
| 8-LORA    | 1853               | 545           | 0.8720   |

**Key finding: Plain fine-tuning failed with OOM on 2 and 4 GPUs. 
LoRA enabled successful training across all configurations 
without compromising validation loss.**

---

### Experiment 3 — DeepSpeed Zero3 + QLoRA (LLaMA 7B & 13B)

| Config     | Total Run Time (s) | Per Epoch (s) | Val Loss |
|------------|--------------------|---------------|----------|
| 2-QLORA    | 4737               | 4131          | 1.023    |
| 4-QLORA    | 2625               | 1777          | 1.029    |
| 8-QLORA    | 1662               | 1066          | 1.028    |
| 2/4-Plain  | OOM                | OOM           | OOM      |

**QLoRA reduced GPU memory utilization by ~40% vs LoRA 
across all GPU configurations without impacting validation loss.**

---

## Key Findings

- **2.39x training speedup** scaling from 2 to 8 GPUs via Tensor Parallelism
- **LoRA resolved OOM errors** on 2 and 4 GPU configs where full fine-tuning failed
- **QLoRA reduced GPU memory by ~40%** vs LoRA while maintaining comparable validation loss
- Tensor Parallelism + QLoRA together enable fine-tuning of LLaMA 13B 
  on hardware that would otherwise be insufficient
- Validated across LLaMA 7B, LLaMA 13B, FlanT5 Large, FlanT5 XL 
  on AWS SageMaker ml.p4d.24xlarge (8x A100 40GB)

---

## Hardware
- AWS SageMaker `ml.p4d.24xlarge`
- 8x NVIDIA A100 40GB GPUs per node

## Libraries Used
- AWS Model Parallelism Library
- DeepSpeed Zero Stage 3
- HuggingFace PEFT (LoRA/QLoRA)
- Bitsandbytes (4-bit quantization)
- HuggingFace Accelerate
- HuggingFace Transformers

  
## Additional Notes
Make sure to review each experiment’s specific README for detailed setup and execution instructions. Adjust your SageMaker settings according to the requirements of the tasks to optimize resource usage and cost efficiency.


