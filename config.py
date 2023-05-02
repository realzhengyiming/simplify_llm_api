import os

USE_EMBEDDING_MODEL = bool(os.environ.get('USE_EMBEDDING_MODEL', False))
USE_LLM_MODEL = bool(os.environ.get('USE_LLM_MODEL', False))  # here you can change your huggingface model path

assert USE_EMBEDDING_MODEL or USE_LLM_MODEL, "env USE_EMBEDDING_MODEL or USE_LLM_MODEL 至少有一个被设置好！!"

if USE_LLM_MODEL:
    MODEL_PATH = os.environ.get('MODEL_PATH', None)
    assert MODEL_PATH, "must set MODEL_PATH in env path first! export MODEL_PATH=xxxx"

if USE_EMBEDDING_MODEL:
    EMBEDDING_PATH = os.environ.get("EMBEDDING_PATH", None)
    assert EMBEDDING_PATH, "must set MODEL_PATH in env path first! export MODEL_PATH=xxxx"
print("model loading!")