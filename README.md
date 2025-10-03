
This repository demonstrates how to build a chatbot named SuperBot using LangGraph and LLMs (Large Language Models) like OpenAI GPT or Groq.

Key concepts covered:

	•	Using graph structures to design chatbot workflows.

	•	Managing conversation history with reducers (add_messages).

	•	Connecting to OpenAI GPT or Groq models.

	•	Running and streaming chatbot responses.

    By the end, you will have a working chatbot capable of handling back-and-forth conversations while maintaining memory of past interactions.

⸻

🛠️ Setup & Installation

	1.	Create and activate a virtual environment:

        python -m venv venv
        

	2.	Install dependencies:

         pip install -r requirements.txt


	3.	Create a .env file in the project root with your API keys:

        OPENAI_API_KEY=your_openai_api_key
        GROQ_API_KEY=your_groq_api_key


⸻

📚 Concepts

    1. Graph Structure

        The chatbot is represented as a graph:

    Start → SuperBot Node → End

        •	Start: Entry point.
        •	SuperBot Node: Where the LLM is invoked.
        •	End: Conversation completion.

    2. Reducers (add_messages)

        Reducers are used to maintain conversation history.
            •	add_messages appends each new user/AI message instead of overwriting.
            •	This allows the chatbot to remember past interactions.

    3. State Class

     The chatbot’s memory is defined using TypedDict.

        •	messages stores the full conversation as a list.
        •	Each new message (user or AI) gets appended.

    4. LLMs Used
        •	OpenAI GPT Models → via ChatOpenAI (paid).
        •	Groq Models → via ChatGroq (some free).

    Both can be invoked with a simple call:

    model.invoke("Hello")


⸻

🚀 Building the Chatbot

	1.	Define State

                Store conversation messages in the state.

	2.	Load Environment Variables

                Securely load API keys from .env.

	3.	Set up LLM Models

                Connect to GPT or Groq.

	4.	Define SuperBot Function

                Handles message processing by calling the LLM.

	5.	Build Graph

                Add nodes and edges

	6.	Compile Graph

⸻

▶️ Execution

    Direct Invocation

    Run the chatbot with one input:

    result.invoke({"messages": "Hi, my name is Karthik and I am an AI Engineer"})

    Streaming Responses

    ⸻

📊 Visualizing the Graph

    You can generate a graph visualization of the chatbot pipeline

⸻

✅ Key Takeaways

	•	LangGraph provides a graph-based approach for building AI apps.

	•	Reducers like add_messages help maintain conversation memory.

	•	LLMs such as GPT or Groq can be easily integrated.

	•	Supports both direct execution and streaming responses.
    
	•	The chatbot is modular, making it easy to expand with more nodes.

⸻

📂 Repository Structure

    ├── superbot.ipynb       # Notebook version with examples
    ├── superbot.py          # Python program file
    ├── requirements.txt     # Dependencies
    ├── README.md            # Documentation


⸻

🎯 Conclusion

    SuperBot demonstrates the power of combining LangGraph with LLMs to create flexible, memory-enabled chatbots. The modular graph-based design makes it easy to scale, customize, and deploy in real-world applications.
