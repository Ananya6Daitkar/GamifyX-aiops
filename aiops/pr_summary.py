# Mock PR summary generator.
# Replace this with real LLM calls (OpenAI, etc.) if you want.
import sys, json

def summarize(pr_title, pr_body):
    # Very simple heuristic summary
    summary = f"PR Summary — Title: {pr_title}\n"
    summary += pr_body[:500] + ("..." if len(pr_body)>500 else "")
    summary += "\nSuggested tests: unit tests for changed modules. Risk: low."
    return summary

if __name__ == '__main__':
    # Expect JSON input: {"title":"...", "body":"..."}
    try:
        payload = json.load(sys.stdin)
        print(summarize(payload.get('title','(no title)'), payload.get('body','')))
    except Exception as e:
        print('Error reading input:', e)
