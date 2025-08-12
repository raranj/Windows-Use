from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
from windows_use.agent import Agent
from dotenv import load_dotenv

from prompt_generator import generate_user_prompt
import time

load_dotenv()

def main():
    llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
    # llm=ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct',api_key=os.getenv("GROQ_API_KEY"))
    agent = Agent(llm=llm,browser='chrome',use_vision=False)

    # query=input("Enter your query: ")
    # agent.print_response(query)

    for i in range(5):
        query = generate_user_prompt()
        print(f"\n[Run {i+1}] Prompt: {query}")
        agent.print_response(query)
        time.sleep(5) # 5 second delay before the next prompt

if __name__ == "__main__":
    main()
