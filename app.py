from flask import Flask, render_template, request
import google.generativeai as genai
import os
import re 
import markdown 

app = Flask(__name__)

os.environ["GEMINI_API_KEY"] = "AIzaSyCzQL9IW0F0PsbiGusPt8V4Hnh5JniX5wI"

#function to strip markdown from gemini

def strip_markdown(text):
   return re.sub(r"[\*\#<>~`]", "", text)
 
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Pre-configure the model
generation_config = {
  "temperature": 0.4,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#global chat history

chat_history = []

#Chatbot modes 

def get_mode(instructions = None):
  
  therapist= """As a virtual therapist, you provide comprehensive answers using simple and clear language about mental health challenges. 
  Be empathetic, and friendly. Ask follow up questions. Use Cognitive Behavioral Therapy techniques to help the person. This can include exercises, mood tracking, and coping strategies.
  Start the conversation by introducing yourself as Michael and your job title."""
  researcher = """
  You are a resarch assistant. You provide detailed comprehensive answers using simple and clear language about mental health challenges. 
  At the end of each response show 3 links to resources that the person can check out."""
  

  
  if instructions == "therapist":
    model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=therapist,)
    return model
  elif instructions == "researcher":
     model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction= researcher,)
     return model
  else:
    model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction= therapist,)
    return model


    
 







@app.route("/")
def index():
  return render_template("homepage.html")


@app.route("/chat", methods=["POST"])
def chat():
  global chat_history
  user_input = request.form["user_input"]
  
  #Check the system mode selection
  system_mode = request.form.get("mode")
  
  #update the model with the appropriate system mode
  model = get_mode(system_mode)
  
  #Set up the chat session     
  chat_session = model.start_chat(history=chat_history)
  
  #Generate the response basd on user question  
  response = chat_session.send_message(user_input)
  
  #convert response from markdown to html 
  formated_respose = markdown.markdown(response.text, extensions=['extra'])
  


  #Update global chat history  
  chat_history = chat_session.history
  
  return render_template("chat.html", conversation=chat_session.history, markdown=markdown.markdown )

@app.route("/reset", methods=["POST"])
def reset_chat():
  global chat_session
  user_input = request.form["user_input"]
  system_mode = request.form.get("mode")
  
 #update the model with the appropriate system mode
  model = get_mode(system_mode)
  
  chat_session = model.start_chat(history=[ ])
  response = chat_session.send_message(user_input)
  return render_template("reset.html", conversation=chat_session.history, markdown=markdown.markdown )

if __name__ == "__main__":
  app.run()
