from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-3.6-flash",temperature =1.8, max_completion_tokens =10)

result = model.invoke("Write a five line poem on cricket")

print(result.text)


