import os
import google.generativeai as genai

try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.  Please set it before running.")
    exit(1)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "I want ai to tell the nutritional value of a fruit or vegetable, when the user gives input",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can do that!  To get the nutritional information, I need you to provide the name of the fruit or vegetable.  Please be as specific as possible (e.g., \"red delicious apple\" instead of just \"apple\").  My knowledge is based on common foods, so very obscure varieties might not have data available.\n",
      ],
    },
  ]
)

fruit_veg = input("Enter the name of the fruit or vegetable: ")

try:
    response = chat_session.send_message(fruit_veg)
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")