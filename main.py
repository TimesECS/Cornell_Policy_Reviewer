import os, json, textwrap, pathlib
from openai import OpenAI
from typing import Optional
from dotenv import load_dotenv
from agents.policybot import PROMPTS, analyze_policy

# Load environment variables from .env file
load_dotenv()
API_KEY  = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.ai.it.cornell.edu/")

client = OpenAI()


def run_module(module: str, user_content: str,
               model: str = "anthropic.claude-3.5-sonnet.v2",
               temperature: float = 0.1) -> dict:
    resp = client.chat.completions.create(
        model=model,
        temperature=temperature,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": PROMPTS[module]["system"]},
            {"role": "user", "content": user_content},
        ],
    )
    content: Optional[str] = resp.choices[0].message.content
    if content is None:
        raise ValueError("No content returned from OpenAI")
    # At this point, content cannot be None
    data = json.loads(content)

    if isinstance(data, dict):
        if set(data.keys()) == {"analysis"}:
            data = data["analysis"]
        elif set(data.keys()) == {"data"}:
            data = data["data"]
    return data



if __name__ == "__main__":
    analyze_policy()
