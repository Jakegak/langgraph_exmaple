# LangGraph Chatbot Example

A simple conversational AI chatbot built with LangGraph and Anthropic's Claude, demonstrating the basics of creating stateful conversational flows.

## 🚀 Features

- **Simple Chat Interface**: Interactive command-line chatbot
- **LangGraph Integration**: Uses LangGraph for conversation state management
- **Claude 3.5 Sonnet**: Powered by Anthropic's latest language model
- **Environment Configuration**: Secure API key management with environment variables
- **Error Handling**: Comprehensive error handling and debugging capabilities

## 📋 Prerequisites

- Python 3.8 or higher
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))
- UV package manager (or pip)

## 🛠️ Installation

### 1. Clone or Download the Project

```bash
git clone git@github.com:Jakegak/langgraph_exmaple.git
cd langgraph_exmaple
```

### 2. Set Up Virtual Environment (if using pip)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

**Using UV (recommended):**
```bash
uv add python-dotenv langgraph "langchain[anthropic]" ipykernel
```

**Using pip:**
```bash
pip install python-dotenv langgraph "langchain[anthropic]" ipykernel
```

### 4. Get Your Anthropic API Key

1. Visit [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in to your account
3. Navigate to "API Keys" in the settings
4. Click "Create Key"
5. Copy your API key (it starts with `sk-ant-`)

### 5. Configure Environment Variables

Create a `.env` file in your project directory:

```bash
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual API key from step 4.

**Example `.env` file:**
```
ANTHROPIC_API_KEY=sk-ant-api03-K1P...YaAA
```

## 🚀 Usage

### Basic Usage

Run the chatbot:

```bash
uv run main.py
```

Or if using pip:
```bash
python main.py
```

### Example Interaction

```
API key loaded: sk-ant-api03-K1P...
✅ Connection test successful: OK
Enter a message: Hello, how are you?

==================================================
Response:
==================================================
Hello! I'm doing well, thank you for asking. I'm Claude, an AI assistant created by Anthropic. How are you doing today? Is there anything I can help you with?
```

## 📁 Project Structure

```
langgraph-example/
├── main.py              # Main chatbot application
├── .env                 # Environment variables (create this)
├── pyproject.toml       # UV project configuration
└── README.md           # This file
```

## 🔧 Code Overview

### Main Components

1. **State Management**: Uses LangGraph's `StateGraph` to manage conversation state
2. **Message Handling**: Employs `add_messages` for conversation history
3. **LLM Integration**: Direct integration with Anthropic's Claude via `ChatAnthropic`
4. **Graph Structure**: Simple linear flow: START → chatbot → END

### Key Functions

- `chatbot(state: State)`: Main function that processes user messages and generates responses
- `State`: TypedDict that defines the conversation state structure
- Graph compilation and execution for stateful conversations

## 🐛 Troubleshooting

### Common Issues

#### 1. Authentication Error (401)
```
anthropic.AuthenticationError: Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error', 'message': 'invalid x-api-key'}}
```

**Solutions:**
- Verify your API key is correct and complete
- Check that your `.env` file is properly formatted
- Ensure no extra spaces or hidden characters in the API key
- Run the debug script: `uv run debug_api_key.py`

#### 2. Missing API Key
```
Error: ANTHROPIC_API_KEY not found in environment variables.
```

**Solutions:**
- Create a `.env` file with your API key
- Or set the environment variable directly: `export ANTHROPIC_API_KEY=your_key_here`

#### 3. Module Import Errors
```
ModuleNotFoundError: No module named 'langchain_anthropic'
```

**Solutions:**
- Install missing dependencies: `uv add langchain-anthropic`
- Ensure you're in the correct virtual environment

### Debug Script

Use the included debug script to diagnose API key issues:

```bash
uv run debug_api_key.py
```

This will:
- Check if the API key is loaded correctly
- Test the direct Anthropic client connection
- Verify LangChain integration
- Display detailed error information

## 📚 Understanding the Code

### LangGraph Concepts

- **State**: Maintains conversation history and context
- **Nodes**: Individual processing units (our `chatbot` function)
- **Edges**: Define the flow between nodes
- **Graph**: The complete conversational flow

### Message Flow

1. User input is received
2. Message is added to the state
3. `chatbot` node processes the state
4. Claude generates a response
5. Response is added to the state
6. Final response is displayed

## 🔐 Security Best Practices

- **Never commit your `.env` file** to version control
- Add `.env` to your `.gitignore` file
- Use environment variables for all sensitive data
- Regularly rotate your API keys
- Monitor your API usage in the Anthropic console

## 📈 Extending the Project

### Add Memory/Context
```python
# Extend the State to include more context
class State(TypedDict):
    messages: Annotated[list, add_messages]
    user_name: str
    conversation_summary: str
```

### Add Multiple Nodes
```python
# Add preprocessing or postprocessing nodes
def preprocessor(state: State):
    # Clean or modify input
    return state

def postprocessor(state: State):
    # Format or enhance output
    return state

graph_builder.add_node("preprocessor", preprocessor)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("postprocessor", postprocessor)
```

### Add Conditional Logic
```python
# Add conditional routing based on message content
def should_use_special_mode(state: State) -> str:
    last_message = state["messages"][-1].content
    if "translate" in last_message.lower():
        return "translator"
    return "chatbot"

graph_builder.add_conditional_edges(
    "input_analyzer",
    should_use_special_mode,
    {"translator": "translator", "chatbot": "chatbot"}
)
```

## 📖 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [LangChain Anthropic Integration](https://python.langchain.com/docs/integrations/chat/anthropic)
- [Anthropic Console](https://console.anthropic.com)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Run the debug script to identify the problem
3. Check your API key and environment setup
4. Review the Anthropic API documentation
5. Open an issue with detailed error information

---

**Happy Chatting! 🤖✨**