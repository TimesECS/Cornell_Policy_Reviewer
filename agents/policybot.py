import os, json, textwrap, pathlib
from openai import OpenAI
from typing import Optional
from dotenv import load_dotenv
from service.load_policy import POLICY_TEXT

PROMPTS = {
    "linguistic": {
        "system": """
You are an AI assistant specialised in policy linguistic analysis.
Return ONLY JSON:
{
  "clarity_score": int,            // 1–10
  "ambiguity_index": int,          // 0–100
  "conflict_potential": int,       // 0–100
  "ambiguous_phrases": [string],
  "suggested_rewrite": [string],
  "readability_grade": string
}
If unsure of any numeric value, output 0.
""".strip()
    },
    "compliance": {
        "system": """
You are a compliance checker comparing policy text to a given standard
and reporting gaps. Output ONLY JSON:
{
  "match_percent": int,             // 0-100
  "non_compliant_sections": [
    {"requirement": string, "issue": string, "severity": "low|med|high"}
  ],
  "risk_severity_map": {"low": int, "med": int, "high": int},
  "recommended_modifications": [string]
}
""".strip()
    },
    "comparison": {
        "system": """
You cross-reference the given policy with related organisational policies.
Return ONLY JSON:
{
  "overlap_percent": int,
  "contradiction_index": int,    // 0–100
  "redundant_sections": [string],
  "integration_suggestions": [string]
}
""".strip()
    },
    "burden": {
        "system": """
You evaluate administrative burden and operational impact.
Return ONLY JSON:
{
  "complexity_score": int,        // 1–10
  "resource_hours": float,        // annual estimate
  "efficiency_gain": string,
  "streamlining_opportunities": [string]
}
""".strip()
    },
    "history": {
        "system": """
You analyse historical compliance data and predict future challenges.
Return ONLY JSON:
{
  "compliance_trend": "↑|↓|→",
  "implementation_barriers": [string],
  "predictive_optimization": [string]
}
""".strip()
    },
}

def run_module(module: str, user_content: str,
               model: str = "anthropic.claude-3.5-sonnet.v2",
               temperature: float = 0.1) -> dict:
    client = OpenAI()
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
    data = json.loads(content)

    if isinstance(data, dict):
        if set(data.keys()) == {"analysis"}:
            data = data["analysis"]
        elif set(data.keys()) == {"data"}:
            data = data["data"]
    return data

def analyze_policy():
    # Load environment variables from .env file
    load_dotenv()
    
    results = {}
    for mod in PROMPTS:
        print(f"⏳ Running {mod}...")
        if mod == "compliance":
            user_msg = f"Compare the policy below with GDPR Article 32 and report gaps:\n\n{POLICY_TEXT}"
        else:
            user_msg = f"Analyse the following Cornell policy text:\n\n{POLICY_TEXT}"
        results[mod] = run_module(mod, user_msg)

    pathlib.Path("results").mkdir(exist_ok=True)
    out = pathlib.Path("results/policy5_10.json")
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\n✅  All done. JSON saved → {out.resolve()}\n")

    print(json.dumps(results, indent=2, ensure_ascii=False))