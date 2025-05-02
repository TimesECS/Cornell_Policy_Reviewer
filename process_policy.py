import json
import pathlib
from typing import Dict, Any

def load_analysis_results() -> Dict[str, Any]:
    """Load the policy analysis results from JSON file"""
    results_path = pathlib.Path("results/policy5_10.json")
    return json.loads(results_path.read_text())

def generate_severity_table(risk_map: Dict[str, int]) -> str:
    """Generate HTML table for risk severity distribution"""
    rows = "".join([
        f'<tr><td>{severity}</td><td>{count}</td></tr>'
        for severity, count in risk_map.items()
    ])
    return f'''
    <table class="severity-table">
        <thead>
            <tr><th>Severity</th><th>Count</th></tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    '''

def generate_html_report(analysis: Dict[str, Any]) -> str:
    """Generate formatted HTML report from analysis results"""
    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Policy Analysis Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        .section {{
            margin-bottom: 30px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }}
        h1, h2 {{
            color: #2c3e50;
        }}
        .severity-table {{
            border-collapse: collapse;
            width: 100%;
            margin: 10px 0;
        }}
        .severity-table th, .severity-table td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        .severity-table th {{
            background-color: #f5f5f5;
        }}
        .metric {{
            display: inline-block;
            margin: 10px;
            padding: 10px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }}
        .list-section {{
            margin: 10px 0;
        }}
        .list-section ul {{
            list-style-type: disc;
            padding-left: 20px;
        }}
        .trend {{
            font-size: 24px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Policy Analysis Report</h1>
    
    <div class="section">
        <h2>Linguistic Analysis</h2>
        <div class="metric">Clarity Score: {analysis['linguistic']['clarity_score']}/10</div>
        <div class="metric">Ambiguity Index: {analysis['linguistic']['ambiguity_index']}%</div>
        <div class="metric">Conflict Potential: {analysis['linguistic']['conflict_potential']}%</div>
        <div class="list-section">
            <h3>Ambiguous Phrases:</h3>
            <ul>
                {''.join(f'<li>{phrase}</li>' for phrase in analysis['linguistic']['ambiguous_phrases'])}
            </ul>
            <h3>Suggested Rewrites:</h3>
            <ul>
                {''.join(f'<li>{rewrite}</li>' for rewrite in analysis['linguistic']['suggested_rewrite'])}
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>Compliance Analysis</h2>
        <div class="metric">GDPR Match: {analysis['compliance']['match_percent']}%</div>
        <h3>Risk Severity Distribution:</h3>
        {generate_severity_table(analysis['compliance']['risk_severity_map'])}
        <div class="list-section">
            <h3>Non-Compliant Sections:</h3>
            <ul>
                {''.join(f'<li><strong>{issue["requirement"]}</strong><br>Issue: {issue["issue"]}<br>Severity: {issue["severity"]}</li>' for issue in analysis['compliance']['non_compliant_sections'])}
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>Policy Integration</h2>
        <div class="metric">Overlap: {analysis['comparison']['overlap_percent']}%</div>
        <div class="metric">Contradiction Index: {analysis['comparison']['contradiction_index']}%</div>
        <div class="list-section">
            <h3>Integration Suggestions:</h3>
            <ul>
                {''.join(f'<li>{suggestion}</li>' for suggestion in analysis['comparison']['integration_suggestions'])}
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>Administrative Burden</h2>
        <div class="metric">Complexity Score: {analysis['burden']['complexity_score']}/10</div>
        <div class="metric">Annual Resource Hours: {analysis['burden']['resource_hours']}</div>
        <div class="list-section">
            <h3>Efficiency Gain:</h3>
            <p>{analysis['burden']['efficiency_gain']}</p>
            <h3>Streamlining Opportunities:</h3>
            <ul>
                {''.join(f'<li>{opportunity}</li>' for opportunity in analysis['burden']['streamlining_opportunities'])}
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>Historical Analysis</h2>
        <div class="metric">Compliance Trend: <span class="trend">{analysis['history']['compliance_trend']}</span></div>
        <div class="list-section">
            <h3>Implementation Barriers:</h3>
            <ul>
                {''.join(f'<li>{barrier}</li>' for barrier in analysis['history']['implementation_barriers'])}
            </ul>
            <h3>Optimization Recommendations:</h3>
            <ul>
                {''.join(f'<li>{opt}</li>' for opt in analysis['history']['predictive_optimization'])}
            </ul>
        </div>
    </div>
</body>
</html>
'''

def main():
    """Main function to generate the HTML report"""
    analysis = load_analysis_results()
    html_content = generate_html_report(analysis)
    
    # Create results directory if it doesn't exist
    pathlib.Path("results").mkdir(exist_ok=True)
    
    # Write HTML report
    output_path = pathlib.Path("results/policy_analysis.html")
    output_path.write_text(html_content)
    print(f"HTML report generated: {output_path.resolve()}")

if __name__ == "__main__":
    main()