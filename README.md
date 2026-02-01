# RAG with Langflow, Ollama, Redis, and Milvus

> **Note**
> This project uses Python 3.13.0


## Setup

1. Create a VENV and activate it.
```bash
python -m venv .venv
.venv/Scripts/activate
```
> **Note**
> This will take several minutes!  Langflow has a LOT of dependencies

2. Install Langflow
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install --force-reinstall --no-cache-dir "langflow>=1.7.1,<2"
```
