from fastapi import FastAPI

from api.controller import chat
from api.models import InputData, ReplyResponse, EmbeddingInput, EmbeddingData, EmbeddingsQueryInput, EmbeddingQueryData
from config import USE_EMBEDDING_MODEL, USE_LLM_MODEL, MODEL_PATH, EMBEDDING_PATH
from globle_logger_util import global_logger
from model_init import init_global_model, init_embeddings

app = FastAPI()
app.logger = global_logger

if USE_LLM_MODEL:
    global_model, global_tokenizer = init_global_model(MODEL_PATH)
    # global global_model
    # global global_model

if USE_EMBEDDING_MODEL:
    global_embeddings = init_embeddings(EMBEDDING_PATH)
    # global global_embeddings


@app.post("/ask")
async def predict(input_data: InputData) -> ReplyResponse:
    print("input_data", input_data)
    if USE_EMBEDDING_MODEL and input_data.prompt:
        print("prompt", len(input_data.prompt))
        response_text = chat(global_model, global_tokenizer, input_data)
    else:
        response_text = "没用配置模型，无法使用！"
    return ReplyResponse(prompt=input_data.prompt, answer=response_text)


@app.post("/embedding")
async def embedding(input_data: EmbeddingInput) -> EmbeddingData:
    texts = input_data.texts
    if USE_EMBEDDING_MODEL and texts:
        print("input", texts[0][:100])
        result = global_embeddings.embed_documents(texts)
        return EmbeddingData(data=result)
    else:
        return EmbeddingData(data=[])


@app.post("/embedding_query")
async def embedding_query(input_data: EmbeddingsQueryInput) -> EmbeddingQueryData:
    text = input_data.text
    print("input", text[:100])
    if USE_EMBEDDING_MODEL and text:
        result = global_embeddings.embed_query(text)
        return EmbeddingQueryData(data=result)
    else:
        return EmbeddingQueryData(data=[])

# todo 释放显存的操作
# @app.exception_handler(CustomException)
# async def custom_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail},
#         headers=exc.headers,
#     )

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=6666)
