import subprocess

def run_model(model_name: str, prompt: str) -> str:
    """
    Runs a local model via Ollama with the given prompt.
    Assumes ollama is installed and model is available locally.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model_name, prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"[Error] Model execution failed: {e.stderr.strip()}"
