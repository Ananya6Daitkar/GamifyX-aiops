import sys
import json
import os
import openai

# Make sure your OpenAI API key is set in GitHub secrets as OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    pr_data = json.load(sys.stdin)
    title = pr_data.get("title", "No title")
    body = pr_data.get("body", "No description")

    prompt = f"Summarize this GitHub PR:\nTitle: {title}\nBody: {body}\nSummary in 2-3 lines:"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    summary = response.choices[0].message.content.strip()
    print("=== PR SUMMARY ===")
    print(summary)

if __name__ == "__main__":
    main()

