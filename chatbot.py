import openai
import gradio

openai.api_key = "###"  #Add your API key here

messages = [{"role": "system", "content": "You are a personal assitant where people can randomly share their thoughts and ask about daily activitites"}]  #Customize it accordingly 

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Personal Assitant")

demo.launch(share=True)