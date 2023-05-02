本文档为中文版 README，请访问 [Read in English](README_EN.md) 获取英文版 README。
如果你觉得这个简单的项目有帮到你，欢迎狠狠的star!🤗


# Simplified llm API
非常，异常简单的llm 类语言模型api接口，提供了三个简单的接口
## 核心主要的模型api化的接口
```shell
/ask  
```

## 额外，embedding 模型使用接口
用于文档查询的封装用的，如果不需要，可以不看这部份，基础的  

```shell
/embedding  
/embedding_query
```

## 详细的接口介绍
可以在clone 项目后阅读
`assert/html2-client-generated/index.html`


# 使用方法
非常的简单，就从huggingface下载你需要用到的语言模型，然后通过命令行，配置环境变量
## 安装依赖
已测试版本python10
`pip install -r requirements.txt`

## 只使用最简单的llm api
```shell
export USE_LLM_MODEL=True
export MODEL_PATH=你从huggingface中下载下来的语言模型文件夹路径
```

## 额外的embedding模型调用如果也需要的话
```shell
export USE_EMBEDDING_MODEL=True
export EMBEDDING_PATH=你从huggingface中下载下来的embedding模型文件夹路径
```

## 启动你的项目
`bash start_server.sh` or `uvicorn app_main:app --host 0.0.0.0 --port 7866 --reload`
启动后也可以在 `http://127.0.0.1:7866/docs` 查看到接口的文档，和使用方法，直接try it out 尝试请求即可

## 部署
进入到项目根目录下，
更新你的环境变量到Dockerfile中，然后构建本地镜像
`docker build -t sample_llm_api:v1 -f Dockerfile .`  
启动镜像为容器服务  
`docker run -p 7866:7866 sample_llm_api:v1`