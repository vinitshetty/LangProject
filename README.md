# LangProject — Simple educational examples for MistralAI integrations

Friendly, minimal project demonstrating four ways to call a MistralAI LLM and integrate with LangWatch for tracing and metrics.

Tools used: MistralAI (model provider), LangWatch (tracing, monitoring and eval framework), LangChain (LLM orchestration), LiteLLM (wrapper works across all model providers), and ChainLit (easy to use chat frontend).

Project integrations shown in this repository are implemented using the tools listed above.

This repository is intentionally small and educational — it's a learning aid showing example wrappers for MistalAI integration with LangWatch in different scenarios:

- Direct Mistral client usage (mistral.py)
- LiteLLM provider usage (litellm_mistralai.py)
- LangChain integration (langchain_mistralai.py)
- LangChain + LiteLLM integration (langchain_litellm_mistralai.py)

📚 What you'll find

- `chat.py` — a minimal Chainlit front-end showing how to stream tokens from a chosen backend.
- `mistral.py` — example of using the official `mistralai` client.
- `litellm_mistralai.py` — example using `litellm` (provider agnostic wrapper).
- `langchain_mistralai.py` — example using LangChain's Mistral adapter.
- `langchain_litellm_mistralai.py` — LangChain with LiteLLM provider.


- `requirements.txt` — packages needed to run the examples.
- `examples/run_example.py` — a small runnable example script (see below).
- `.env.example` — sample environment file showing required keys.

Getting started — quick steps

1) Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

2) Create a `.env` file at the project root (you can copy `.env.example`) and fill in your API keys

```ini
# .env
MISTRAL_API_KEY=sk-your-mistral-key #https://admin.mistral.ai/organization/api-keys
LANGWATCH_API_KEY=sk-your-langwatch-key  # optional (used for tracing/monitoring) https://app.langwatch.ai/
MODEL_NAME=ministral-3b-latest
LLM_PROVIDER=mistral
```

3) Run a simple example (choose a backend):


```powershell
Launch Web Chat App: python -m chainlit run chat.py
CLI:
python run_example.py --backend mistral "What is the best French cheese and why?"
python run_example.py --backend litellm "Explain recursion in 30 words"
python run_example.py --backend langchain "Give me a short bio for Ada Lovelace"
python run_example.py --backend langchain_litellm "List 3 tips for unit testing"
```
##ChainLit Web App:
<img width="758" height="542" alt="image" src="https://github.com/user-attachments/assets/7bc59996-f8ef-42f5-a8b4-34050d360188" />

##LangWatch App Traces:
<img width="758" height="542" alt="image" src="https://github.com/user-attachments/assets/949793e4-b1a3-4ed0-89ab-30eefe04e585" />
<img width="758" height="542" alt="image" src="https://github.com/user-attachments/assets/a568d0c6-1543-4695-9350-3cf733a15d51" />

This project is provided as-is for educational purposes. Feel free to reuse and adapt the code for experiments.
