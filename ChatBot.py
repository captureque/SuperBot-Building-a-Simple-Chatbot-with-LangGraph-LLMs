# SuperBot: Building a Simple Chatbot with LangGraph + LLMs

from typing_extensions import TypedDict
from langgraph.graph import StateGraph,START,END

#Reducers
from typing import Annotated
from langgraph.graph.message import add_messages # library for message handling, Merges two lists of messages, updating existing messages by ID.

class State(TypedDict):
    messages: Annotated[list, add_messages]  # List of messages in the conversation
    
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQL_API_KEY"] = os.getenv("GROQ_API_KEY")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-5-nano")
model.invoke("Hello")

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.1-8b-instant")
llm.invoke("Hello my name is Karthik , I like to take photos")

def superbot(state:State):
    return {"messages":[llm.invoke(state['messages'])]} # Invokes the language model with the current messages and returns the response.

graph = StateGraph(State)
# Add nodes to the graph
graph.add_node("Superbot",superbot)
# Add edges to the graph
graph.add_edge(START,"Superbot")
graph.add_edge("Superbot",END)
# Execute the graph
result = graph.compile()

#Display the graph
from IPython.display import display,Image
display(Image(result.get_graph().draw_mermaid_png()))


#Invocation  
result.invoke({"messages":"Hi My name is Karthik and i am an AI Engineer"})
#Streaming  the Responses
update = result.stream({"messages":"Hi My name is Karthik and i am an AI Engineer"},stream_mode="values")
for message in update:
    print(message)
