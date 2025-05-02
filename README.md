# Policy Analysis Tool

A Python-based tool for analyzing information security policies using AI. This tool performs multi-dimensional analysis of policy documents, including linguistic analysis, compliance checking, policy integration assessment, administrative burden evaluation, and historical trend analysis.

## Features

- **Linguistic Analysis**: Evaluates policy clarity, identifies ambiguous phrases, and suggests improvements
- **Compliance Analysis**: Checks GDPR compliance and identifies gaps in security measures
- **Policy Integration**: Analyzes overlap with existing policies and suggests integration opportunities
- **Administrative Burden**: Assesses implementation complexity and resource requirements
- **Historical Analysis**: Tracks compliance trends and predicts future challenges

## Project Structure

```
.
├── main.py                 # Main entry point for policy analysis
├── process_policy.py       # HTML report generator
├── agents/
│   └── policybot.py       # Policy analysis logic and prompts
├── service/
│   └── load_policy.py     # Policy text loader
└── results/
    ├── policy5_10.json    # Analysis results in JSON format
    └── policy_analysis.html# Generated HTML report
```

## Requirements

- Python 3.x
- OpenAI API access
- Required Python packages:
  - openai
  - python-dotenv

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install openai python-dotenv
```
3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the policy analysis:
```bash
python main.py
```
This will analyze the policy and generate a JSON file with the results.

2. Generate an HTML report:
```bash
python process_policy.py
```
This will create a formatted HTML report from the analysis results.

## Output

The tool generates two types of output:

1. **JSON Analysis** (`results/policy5_10.json`):
   - Detailed analysis scores and metrics
   - Compliance gaps and recommendations
   - Policy integration opportunities
   - Resource requirements and optimization suggestions

2. **HTML Report** (`results/policy_analysis.html`):
   - User-friendly visualization of analysis results
   - Interactive tables and metrics
   - Formatted recommendations and findings

## Analysis Components

### Linguistic Analysis
- Clarity scoring (1-10)
- Ambiguity detection
- Improvement suggestions

### Compliance Analysis
- GDPR compliance matching
- Risk severity assessment
- Non-compliant section identification

### Policy Integration
- Policy overlap assessment
- Contradiction detection
- Integration recommendations

### Administrative Burden
- Complexity scoring
- Resource estimation
- Efficiency opportunities

### Historical Analysis
- Compliance trends
- Implementation barriers
- Future optimization recommendations