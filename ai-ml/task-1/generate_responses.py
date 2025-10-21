import json
import logging
from openai import OpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Initialize Groq API client
client = OpenAI(
    api_key="",  # Enter the API key over here (I have NOT included it here, because this code is going on github lmao)
    base_url="https://api.groq.com/openai/v1"
)

def load_prompts(filepath: str) -> list[str]:
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_responses(prompts: list[str], model: str) -> list[dict]:
    results = []
    for i, prompt in enumerate(prompts, start=1):
        logging.info(f"Processing prompt {i}/{len(prompts)}")
        try:
            response = client.responses.create(model=model, input=prompt)
            results.append({"prompt": prompt, "response": response.output_text})
        except Exception as e:
            logging.error(f"Error on prompt {i}: {e}")
            results.append({"prompt": prompt, "error": str(e)})
    return results

def save_results(results: list[dict], filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

def main():
    prompts = load_prompts("prompts.txt")
    results = generate_responses(prompts, model="llama-3.3-70b-versatile")
    save_results(results, "responses.json")
    logging.info("Responses were sucessfully saved to responses.json")

if __name__ == "__main__":
    main()