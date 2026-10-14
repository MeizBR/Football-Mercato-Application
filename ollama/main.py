from pathlib import Path
import os
from ollama import chat

current_dir = Path.home() / "Desktop" / "Football-Mercato-Application" / "rumours_details"

# print (type(os.listdir(current_dir)))

rumour_file = "alessandro_romano_rumour_2026-10-12_details.html"

def analyze_rumour() -> str:
    """Read the predefined transfer rumour HTML file and return its content."""
    file_path = current_dir / rumour_file

    if not file_path.is_file():
        return f"Error: Rumour file not found: {file_path}"

    return file_path.read_text(encoding="utf-8")


messages = [
    {
        "role": "user",
        "content": (
            "Analyze the transfer rumour in the file available through "
            "the analyze_rumour tool. Summarize the player involved, "
            "the clubs mentioned, the reported claims, potential biases, "
            "and uncertainties. Distinguish facts stated in the file "
            "from claims that have not been verified."
        ),
    }
]

response = chat(
    model="qwen3:4b",
    messages=messages,
    tools=[analyze_rumour],
    think=True,
)

messages.append(response.message)

if response.message.tool_calls:
    for call in response.message.tool_calls:
        if call.function.name == "analyze_rumour":
            result = analyze_rumour()

            messages.append({
                "role": "tool",
                "tool_name": call.function.name,
                "content": result,
            })

    final_response = chat(
        model="qwen3:4b",
        messages=messages,
        tools=[analyze_rumour],
        think=True,
    )

    print(final_response.message.content)
else:
    print(response.message.content)