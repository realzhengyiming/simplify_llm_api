FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

# 把你的环境变量通过ENV增加到此处
# ENV USE_LLM_MODEL=True
# ENV MODEL_PATH=你从huggingface中下载下来的语言模型文件夹路径

RUN conda config --remove channels defaults \
  && conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
  && conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r \
  && conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2 \
  && conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ \
  && conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ \
  && conda config --set show_channel_urls yes
RUN conda install -c pytorch faiss-cpu
COPY requirements.txt .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["uvicorn", "app_main:app", "--host", "0.0.0.0", "--port", "8001"]

