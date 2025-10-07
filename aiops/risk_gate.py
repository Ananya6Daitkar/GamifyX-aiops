# Mock risk gate.
# Input: JSON via stdin: {"diff_lines": 123, "test_coverage": 82}
# Exits with code 0 = pass, 1 = block deploy
import sys, json

def check(payload):
    diff = payload.get('diff_lines',0)
    cov = payload.get('test_coverage',100)
    # Block if diff > 500 or coverage < 70
    if diff > 500 or cov < 70:
        print(f"BLOCK: diff_lines={diff}, coverage={cov}")
        return 1
    print(f"PASS: diff_lines={diff}, coverage={cov}")
    return 0

if __name__ == '__main__':
    try:
        payload = json.load(sys.stdin)
        code = check(payload)
        sys.exit(code)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
