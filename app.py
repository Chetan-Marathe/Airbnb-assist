from praisonaiagents import Agent , MCP
import gradio as gr

def search_airbnb(query):
   agent = Agent(    
    instructions="""You help book apartment on Airbnb.""",
    llm="ollama/llama3.2",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
   )
   result = agent.start(query)
   return f"## Airbnb Search Results\n\n{result}"

demo = gr.Interface(
   fn=search_airbnb,
   inputs=gr.Textbox(placeholder = "I want to book an apartment....."),
   outputs=gr.Markdown(),
   title="Airbnb Booking Assistant",
   description="Enter your booking requirements below:"
)

if __name__ == "__main__":
   demo.launch()
