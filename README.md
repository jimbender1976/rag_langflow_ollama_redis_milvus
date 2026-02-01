# RAG with Langflow, Ollama, Redis, and Milvus

> **Note**
> This project uses Python 3.13.0

## Setup

1. Create a VENV and activate it.
```bash
python -m venv .venv
.venv/Scripts/activate
```

2. Install Langflow
```bash
python -m pip install --upgrade pip
python -m pip install --force-reinstall --no-cache-dir "langflow>=1.7.1,<2"
```
> **Note**
> This will download the internet and take forever.  You might have to try it a few times for it to even work.

3. Run Langflow
```bash
langflow run
```
> **Note**
> This will start Langflow on its default port.  The localhost URL Langflow is running on will show in the shell's output once ready.

## Create Flow

1. Open the Langflow URL that the shell showed
2. Click "Create first flow" or "New Flow"
3. Click Blank Flow
4. Give Flow a name
> **Note**
> You can also choose the "Vector Store RAG" template if you would prefer to just customize that.

## User Input

Add each of the following components to your flow:
- Text Input
- Prompt Template
- Chat Input
