import subprocess

# # Create output directory
# subprocess.run(["mkdir", "output"], check=True)

# Define the command as a list of arguments

"""
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train \
    --model_name_or_path /workspace/ChatGLM-Efficient-Tuning/chatglm2-6b \
    --dataset oaast_rm \
    --dataset_dir data \
    --finetuning_type lora \
    --output_dir output/lora_sft_checkpoint \
    --overwrite_cache \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 1e-3 \
    --num_train_epochs 3.0 \
    --fp16 
"""

command = [
    "python", "src\\train_bash.py",
    "--stage", "sft",
    "--do_train",
    "--model_name_or_path", "D:\\Project\\AI\\ChatGLM-Efficient-Tuning\\chatglm2-6b",  # Update the path
    "--dataset", "self_cognition",
    "--dataset_dir", "data",
    "--finetuning_type", "lora",
    "--output_dir", "output\\lora_sft_checkpoint",
    "--overwrite_cache",
    "--per_device_train_batch_size", "2",
    "--gradient_accumulation_steps", "2",
    "--lr_scheduler_type", "cosine",
    "--logging_steps", "10",
    "--save_steps", "1000",
    "--learning_rate", "1e-3",
    "--num_train_epochs", "3.0",
    "--fp16"
]

# Execute the command
subprocess.run(command, check=True)
