# Simplified llm API

This document is the English version of the README. Please visit [用中文看](README.md) for the Chinese version of the
README if you need.

If you find this simple project helpful, please give it a star!🤗

## Introduction

This is an extremely simple API interface for llm-like language models, providing three simple interfaces.

### Core model API interface

```shell
/ask  
```

### Additional embedding model usage interface

This is used for document queries. If not needed, you can skip this part.

```shell
/embedding  
/embedding_query
```

## Detailed interface introduction  
can be found after cloning the project
`assert/html2-client-generated/index.html`

# Usage
## Installing Dependencies
Tested with Python 10.
Run `pip install -r requirements.txt` to install the dependencies.

Return in markdown format:
```markdown
## Installing Dependencies
Tested with Python 10.
Run `pip install -r requirements.txt` to install the dependencies.
```

It's very simple. First, download the language model you need from Hugging Face. Then, configure environment variables
through the command line.

## Using only the simplest llm API

```shell
export USE_LLM_MODEL=True
export MODEL_PATH=The path to the folder where you downloaded your language model from Hugging Face.
```

## If additional embedding model calls are needed:

```shell
export USE_EMBEDDING_MODEL=True
export EMBEDDING_PATH=The path to the folder where you downloaded your embedding model from Hugging Face.
```

## Start your project:

`bash`

## Deployment

Navigate to the root directory of the project.

Update your environment variables in the Dockerfile, then build a local image:
`docker build -t sample_llm_api:v1 -f Dockerfile .`

Start the image as a container service:
`docker run -p 7866:7866 sample_llm_api:v1`

Return in markdown format:

```markdown
## Deployment

Navigate to the root directory of the project.

Update your environment variables in the Dockerfile, then build a local image:
```

docker build -t sample_llm_api:v1 -f Dockerfile .

```

Start the image as a container service:
```

docker run -p 7866:7866 sample_llm_api:v1

```