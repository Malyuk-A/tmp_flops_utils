import shlex
import subprocess


def run_in_shell(shell_cmd: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(shlex.split(shell_cmd), capture_output=True, check=True)
