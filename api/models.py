from typing import List

from pydantic import BaseModel


class ReplyResponse(BaseModel):
    prompt: str
    answer: str


class InputData(BaseModel):
    prompt: str
    history: List[List[str]] = []
    max_length: int
    top_p: float = 0.9
    temperature: float = 0.1
    # 当 temperature 越大时，生成的文本就越随机、越不可预测，因此可能更有创造性。相反，当 temperature 值较小时，生成的文本则更加保守、更具可预测性。

    __default__ = {
        'history': [],
        'context': [],
        "top_p": 0.9,
        "max_length": 10000,  #
        "temperature": 0.1
    }


class EmbeddingData(BaseModel):
    data: List[List[float]]


class EmbeddingInput(BaseModel):
    texts: List[str]


class EmbeddingsQueryInput(BaseModel):
    text: str


class EmbeddingQueryData(BaseModel):
    data: List[float]
