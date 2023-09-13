# this scripts installs necessary requirements and launches main program in webui.py
# borrow from : https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/launch.py
import subprocess
import os
import sys
import importlib.util
import shlex
import platform
import json

python = sys.executable
git = os.environ.get('GIT', "git")
index_url = os.environ.get('INDEX_URL', "")
stored_commit_hash = None
skip_install = False
dir_repos = "repositories"
script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if 'GRADIO_ANALYTICS_ENABLED' not in os.environ:
    os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'


def check_python_version():
    is_windows = platform.system() == "Windows"
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    if is_windows:
        supported_minors = [10]
    else:
        supported_minors = [7, 8, 9, 10, 11]

    if not (major == 3 and minor in supported_minors):

        raise (f"""
INCOMPATIBLE PYTHON VERSION
This program is tested with 3.10.6 Python, but you have {major}.{minor}.{micro}.
If you encounter an error with "RuntimeError: Couldn't install torch." message,
or any other error regarding unsuccessful package (library) installation,
please downgrade (or upgrade) to the latest version of 3.10 Python
and delete current Python and "venv" folder in WebUI's directory.
You can download 3.10 Python from here: https://www.python.org/downloads/release/python-3109/
{"Alternatively, use a binary release of WebUI: https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases" if is_windows else ""}
Use --skip-python-version-check to suppress this warning.
""")


def commit_hash():
    global stored_commit_hash

    if stored_commit_hash is not None:
        return stored_commit_hash

    try:
        stored_commit_hash = run(f"{git} rev-parse HEAD").strip()
    except Exception:
        stored_commit_hash = "<none>"

    return stored_commit_hash


def run(command, desc=None, errdesc=None, custom_env=None, live=False):
    if desc is not None:
        print(desc)

    if live:
        result = subprocess.run(command, shell=True, env=os.environ if custom_env is None else custom_env)
        if result.returncode != 0:
            raise RuntimeError(f"""{errdesc or 'Error running command'}.
Command: {command}
Error code: {result.returncode}""")

        return ""

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=os.environ if custom_env is None else custom_env)

    if result.returncode != 0:

        message = f"""{errdesc or 'Error running command'}.
Command: {command}
Error code: {result.returncode}
stdout: {result.stdout.decode(encoding="utf8", errors="ignore") if len(result.stdout)>0 else '<empty>'}
stderr: {result.stderr.decode(encoding="utf8", errors="ignore") if len(result.stderr)>0 else '<empty>'}
"""
        raise RuntimeError(message)

    return result.stdout.decode(encoding="utf8", errors="ignore")


def check_run(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.returncode == 0


def is_installed(package):
    try:
        spec = importlib.util.find_spec(package)
    except ModuleNotFoundError:
        return False

    return spec is not None


def repo_dir(name):
    return os.path.join(script_path, dir_repos, name)


def run_python(code, desc=None, errdesc=None):
    return run(f'"{python}" -c "{code}"', desc, errdesc)


def run_pip(args, desc=None):
    if skip_install:
        return

    index_url_line = f' --index-url {index_url}' if index_url != '' else ''
    return run(f'"{python}" -m pip {args} --prefer-binary{index_url_line}', desc=f"Installing {desc}", errdesc=f"Couldn't install {desc}")


def check_run_python(code):
    return check_run(f'"{python}" -c "{code}"')





def prepare_environment():
    global skip_install

    run(f'"{python}" -m pip install --upgrade pip', "upgrade pip", "upgrade pip", live=True)
    #torch_command = os.environ.get('TORCH_COMMAND', "pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html")

    torch_command = os.environ.get('TORCH_COMMAND', "pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117")

    requirements_file = os.environ.get('REQS_FILE', "requirements.txt")

    commit = commit_hash()

    if not is_installed("torch") or not is_installed("torchvision"):
       run(f'"{python}" -m {torch_command}', "Installing torch and torchvision", "Couldn't install torch", live=True)

    print(f"Python {sys.version}")
    print(f"Commit hash: {commit}")

    
    
    #run(f'"{python}" -m pip uninstall tensorflow', "uninstall tensorflow", "uninstall tensorflow", live=True) 

    run_pip(f"install -r \"{requirements_file}\"", "requirements install at first time)")



    


if __name__ == "__main__":
    prepare_environment()