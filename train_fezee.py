import subprocess

# # Create output directory
# subprocess.run(["mkdir", "output"], check=True)

# Define the command as a list of arguments

"""
python src/train_bash.py --do_train --model_name_or_path /home/aistudio/work/chatglm2-6b --dataset self_cognition --dataset_dir data --finetuning_type freeze --output_dir output/freeze_sft_checkpoint --overwrite_cache --per_device_train_batch_size 2 --gradient_accumulation_steps 2 --lr_scheduler_type cosine --logging_steps 10 --save_steps 1000 --learning_rate 5e-5 --num_train_epochs 3.0 --plot_loss --fp16
"""

"""
python src/train_bash.py --do_train --model_name_or_path D:\\Project\\AI\\ChatGLM-Efficient-Tuning\\chatglm2-6b --dataset self_cognition --dataset_dir data --finetuning_type freeze --output_dir output/freeze_sft_checkpoint --overwrite_cache --per_device_train_batch_size 2 --gradient_accumulation_steps 2 --lr_scheduler_type cosine --logging_steps 10 --save_steps 1000 --learning_rate 5e-5 --num_train_epochs 3.0 --plot_loss --int8
"""

command = [
    "python", "src\\train_bash.py",
    "--do_train",
    "--model_name_or_path", "D:\\Project\\AI\\ChatGLM-Efficient-Tuning\\chatglm2-6b",
    "--dataset", "self_cognition",
    "--dataset_dir", "data",
    "--finetuning_type", "freeze",
    "--output_dir", "output\\freeze_sft_checkpoint",
    "--overwrite_cache",
    "--per_device_train_batch_size", "2",
    "--gradient_accumulation_steps", "2",
    "--lr_scheduler_type", "cosine",
    "--logging_steps", "10",
    "--save_steps", "1000",
    "--learning_rate", "5e-5",
    "--num_train_epochs", "3.0",
    "--plot_loss",
    "--fp16"
]

# Execute the command
subprocess.run(command, check=True)
