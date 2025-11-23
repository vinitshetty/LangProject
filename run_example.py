"""Small convenience script to run a request against the example backends.

Usage:
  python examples/run_example.py --backend mistral "My question here"

Backends supported: mistral, litellm, langchain, langchain_litellm

This script demonstrates the small wrapper functions in the project and provides
helpful checks for missing environment variables.
"""
import argparse
import os
import sys
from importlib import import_module

from dotenv import load_dotenv
load_dotenv()

BACKEND_TO_MODULE = {
    "mistral": "mistral",
    "litellm": "litellm_mistralai",
    "langchain": "langchain_w_mistralai",
    "langchain_litellm": "langchain_litellm_mistralai",
}


def has_required_env():
    # Mistral key is required for all examples; LangWatch optional
    return bool(os.getenv("MISTRAL_API_KEY"))


def run_request(backend: str, prompt: str):
    module_name = BACKEND_TO_MODULE.get(backend)
    if not module_name:
        raise ValueError(f"Unknown backend '{backend}' — choose from: {list(BACKEND_TO_MODULE)}")

    try:
        module = import_module(module_name)
    except Exception as e:
        raise RuntimeError(f"Failed to import module '{module_name}': {e}")

    # Most example modules provide a function named call_mistral_api(prompt)
    fn = getattr(module, "call_mistral_api", None)
    if fn is None:
        raise RuntimeError(f"Module {module_name} does not expose call_mistral_api()")

    return fn(prompt)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=BACKEND_TO_MODULE.keys(), default="mistral")
    parser.add_argument("prompt", nargs="+", help="Prompt (wrap in quotes)")
    args = parser.parse_args()

    prompt = " ".join(args.prompt)

    if not has_required_env():
        print("Missing MISTRAL_API_KEY environment variable. Create a .env or export it in your shell.")
        print("See .env.example for the variables used by this project.")
        sys.exit(2)

    try:
        print(f"Using backend: {args.backend}\nPrompt: {prompt}\n")
        result = run_request(args.backend, prompt)
        print("--- Response ---")
        print(result)
    except Exception as exc:
        print("Example failed:", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
