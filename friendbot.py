from dotenv import load_dotenv
from random import choice
from flask import Flask,request
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion

start_sequence = "\nFRI(IEND):"
restart_sequence = "\nME: "
session_prompt = "Your virtual friend who seems to always change his interests and life goals, right now he is a tourist guide for the beautiful city Stockholm, Sweden. Please go ahead and ask it about what to visit and do whilst in Stockholm, Sweden.."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature=0.4,
        prompt=prompt_text,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["FR(IE)ND", "ME"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
