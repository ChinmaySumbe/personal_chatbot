import cohere 
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_text_output(Input_text):
    Output =  co.chat(
    model="command-r-plus",
    message= Input_text
)
    return Output.text



def get_text_stream_output(Input_text):
    for Output in co.chat_stream(
    model="command-r-plus",
    message= Input_text
):
        if Output.event_type == "text-generation":
            yield Output.text
        
    
    


# Output = co.chat(
#     model="command-r-plus",
#     message="Hello"
# )

# print(co)
# print(Output.text)