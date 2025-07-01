import os
from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic
from typing_extensions import TypedDict

# Load environment variables
load_dotenv()

# Get and clean the API key
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("Error: ANTHROPIC_API_KEY not found in environment variables.")
    print("Please create a .env file with your Anthropic API key:")
    print("ANTHROPIC_API_KEY=your_actual_api_key_here")
    exit(1)

# Clean the API key (remove any whitespace/newlines)
api_key = api_key.strip()

print(f"API key loaded: {api_key[:15]}...{api_key[-5:]}")

# Initialize the chat model with explicit API key
try:
    llm = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        api_key=api_key,
        max_tokens=1000
    )
    
    # Test the connection immediately
    test_response = llm.invoke("Test connection - respond with 'OK'")
    print(f"✅ Connection test successful: {test_response.content}")
    
except Exception as e:
    print(f"❌ Error initializing chat model: {e}")
    print("Please verify your API key is correct.")
    exit(1)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    try:
        return {"messages": [llm.invoke(state["messages"])]}
    except Exception as e:
        print(f"Error in chatbot function: {e}")
        raise

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

try:
    user_input = input("Enter a message: ")
    state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    print("\n" + "="*50)
    print("Response:")
    print("="*50)
    print(state["messages"][-1].content)
except Exception as e:
    print(f"Error during execution: {e}")
    print("Please check your API key and try again.")