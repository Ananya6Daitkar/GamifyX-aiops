import json

def compute_aiops_risk():
    print("Starting AI-Ops risk computation...")  # Add this line for debugging
    # Example static risk computation
    security_issues = 20
    test_failures = 0
    risk_score = security_issues + test_failures

    summary = {
        "security_issues": security_issues,
        "test_failures": test_failures,
        "risk_score": risk_score
    }

    with open("aiops_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("✅ AI-Ops summary generated → aiops_summary.json")

if __name__ == "__main__":
    compute_aiops_risk()
