from openai import OpenAI

OPENAI_API_KEY = ""

client = OpenAI(api_key=OPENAI_API_KEY)

prompt = "You are an expert football transfer intelligence assistant helping build a football mercato application. Search for the latest transfer news, rumours, and official announcements across football. Your mission includes: identify confirmed transfers, identify credible transfer rumours, identify important contract renewals, identify loan deals, identify advanced negotiations and verbal agreements and ignore unrelated football match news"

response = client.responses.create(
    model="gpt-5.4",
    # reasoning={"effort": "low"},
    # instructions="You are a professional football journalist.",
    input="Write a one-sentence bedtime story about a unicorn.",
    # tools=[{"type": "web_search"}],
    # input=[
    #     {
    #         "role": "developer",
    #         "content": "You are a professional football journalist."
    #     },
    #     {
    #         "role": "user",
    #         "content": {prompt}
    #     }
    # ]
)

res = response.output_text

print(res)

with open("results_file.txt", "a") as f:
    f.write(response.output[0].content[0].text)