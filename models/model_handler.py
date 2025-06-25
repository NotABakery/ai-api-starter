import replicate
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
replicate.Client(api_token=REPLICATE_API_TOKEN)

def run_model(prompt: str) -> str:
    output = replicate.run(
        "meta/llama-2-7b-chat",
        input={"prompt": prompt, "max_new_tokens": 200}
    )
    return "".join(output)