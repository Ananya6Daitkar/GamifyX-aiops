# ci_cd/actual.py
import subprocess
import json
import datetime
import random
import os

def run_tests():
    print("🧪 Running Unit Tests...")
    result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"], capture_output=True, text=True)
    print(result.stdout)
    failed = 0 if "failed" not in result.stdout else 1
    return failed

def run_security_scan():
    print("🔒 Running Security Scan (Bandit)...")
    result = subprocess.run(["bandit", "-r", ".", "--quiet"], capture_output=True, text=True)
    issues = result.stdout.count(">> Issue:")
    print(f"Security Issues Found: {issues}")
    return issues

def compute_risk(failed_tests, security_issues):
    print("⚙️ Computing AI-Ops Risk Score...")
    risk_score = failed_tests * 50 + security_issues * 25 + random.randint(0, 20)
    status = "SAFE" if risk_score < 50 else "RISKY"
    return risk_score, status

def generate_summary(failed_tests, security_issues, risk_score, status):
    data = {
        "summary": {
            "timestamp": datetime.datetime.now().isoformat(),
            "failed_tests": failed_tests,
            "security_issues": security_issues,
            "risk_score": risk_score,
            "status": status
        },
        "insights": [
            "🧪 Tests completed successfully" if failed_tests == 0 else "❌ Some tests failed — fix before deploy",
            "🔐 Security check passed" if security_issues == 0 else "⚠️ Security issues detected — run Bandit report",
            f"📊 Overall Risk Score: {risk_score} ({status})"
        ]
    }
    with open("aiops_summary.json", "w") as f:
        json.dump(data, f, indent=4)
    print("✅ AIOps Summary saved → aiops_summary.json")

def main():
    print("🚀 Starting GamifyX-AIOps Actual Workflow\n")

    failed_tests = run_tests()
    security_issues = run_security_scan()
    risk_score, status = compute_risk(failed_tests, security_issues)
    generate_summary(failed_tests, security_issues, risk_score, status)

    print("\n🎯 Pipeline completed successfully!\n")

if __name__ == "__main__":
    main()
