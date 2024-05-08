"""Train.py."""

import os
os.environ["NVTE_TORCH_COMPILE"] = "0"

from arguments import parse_args
import train_lib
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Main function to train GPT."""
    args, _ = parse_args()
    install('peft')
    train_lib.main(args)


if __name__ == "__main__":
    main()
