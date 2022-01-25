from speech_to_text import *
from text_to_speech import *
import os
import openai

#add your api key below, it needs to be within the double quotation marks.
openai.api_key = ""

#you can edit the below
#end the below sentencess with full stops
#######################
#define a few characteristics of the AI
name = "Jim" #only type the name
personality = "Jim is very polite and well mannered. He is very intelligent and has knowledge of many diverse topics." #describe the personality of the AI
purpose = "Jim helps users by providing knowledge and fun facts to the user." #if you want the AI to help the user in anything then specify here in detail.
personal_interests = "Jim likes reading a lot of books and likes geography a lot." #This helps in making the AI more unique 
rules = "Jim should not use abusive language and should be very polite and friendly to the users." #Specify the rules the AI should follow while speaking to users
#######################

#Do not edit the below
#This helps in intializing the chatbot, this helps the language model in understanding 
# that we want it simulate a conversation between a chatbot and a person.
#######################
part1 = "This is a conversation with a conversational AI. The name of the AI is "
part2 = "\n\nUser1: Hello, who are you?\n"
part3 = ": Hello my name is "
part4 = ".I am a conversational AI. How can I help you today?\nUser1: I would like to ask you a question.\n"
part5 = ": Sure, please ask your question.\nUser1: Which fruit is rich in vitamin c?\n"
part6 = ": Citrus fruits like oranges and lemons are rich in vitamin c."
#######################

text = part1 + name +". "+personality+purpose+personal_interests+rules+part2+name+part3+name+part4+name+part5+name+part6

def gen_response(text):
  response = openai.Completion.create(
  engine="davinci",
  prompt= text,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n"] )
  return response 

starting_response = "Hello my name is " + name
print(starting_response)
text_to_speech(starting_response)
user_input = ""
while user_input != "bye"  : 
  text = text + "\nUser1: "
  user_input = speech_to_text()
  #user_input = input()
  print(user_input)
  text = text + user_input + "\n" + name + ": "
  response = gen_response(text)
  response = response['choices'][0]['text']
  text = text + response 
  #print(text)
  print(name + ": " + response)
  text_to_speech(response)


