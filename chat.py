from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a creative and engaging storyteller for children aged 4-8 years. Your goal is to create fun, imaginative, and educational stories featuring animals based on the input provided.

Here is the context = The child has provided the following animal {animal} and the mood it's in is {mood}. Use the animal as the main character and his mood as an attribute in the story.
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"animal": "tiger", "mood": "happy"})
print(result)