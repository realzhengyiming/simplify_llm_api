import time

from api.models import InputData


def chat(model, tokenizer, input_data: InputData) -> str:
    prompt = input_data.prompt
    history = input_data.history
    max_length = input_data.max_length
    top_p = input_data.top_p
    temperature = input_data.temperature

    start = time.time()
    response, history = model.chat(tokenizer,
                                   prompt,
                                   history=history,
                                   max_length=max_length if max_length else 10000,
                                   top_p=top_p if top_p else 0.7,
                                   temperature=temperature if temperature else 0.95)
    print(f"model thinking spended: {time.time() - start}")
    return response
