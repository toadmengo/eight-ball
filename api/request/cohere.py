import random
import cohere
from .secrets import apiKey

error_resp = "That's a stupid question, I don't fucking know."

def cleanQuestion(question):
  if question[len(question)-1] != "?":
      question += "?"
  return question

def cleanResponse(response):
  if response[len(response)-1] != ".":
    response = response[:response.rfind('\n')]
  answers = response.split("\n")[1:]
  answer = random.choice(answers)
  return answer.replace("Answer: ", "")

def predict(question):
  if question == "":
    return error_resp
  try:
    f = open("./api/request/prompts.txt", "r")
    prompt = f.read()
    f.close()
    co = cohere.Client(apiKey)
    question = cleanQuestion(question)
    response = co.generate(
      model='xlarge',
      prompt=prompt + "Question: " + question,
      temperature=0.95,
      k=0,
      p=0.75,
      frequency_penalty=0,
      presence_penalty=0,
      stop_sequences=[],
      return_likelihoods='NONE')
    r = cleanResponse(response.generations[0].text)
    return r
  except:
    return error_resp
