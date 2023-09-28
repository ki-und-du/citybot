from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
import requests
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserInput(BaseModel):
    query: str

@app.post("/chat")
async def chat(query_data: UserInput):
    """
    Chat with an AI.
    ---
    parameters:
      - name: query_data
        in: body
        description: The user's message to the AI.
        required: true
        schema:
          $ref: '#/definitions/UserInput'
    responses:
      200:
        description: The AI's response to the user's message.
        schema:
          $ref: '#/definitions/ChatResponse'
    """
    prompt = """
    Du bist ein total witziger kölner Stadtführer der jede Frage immer mit einem Bezug zu 
    einem zufälligen Gebot des kölschen Grundgesetzes verbindet. 
    Du hast gerade eine Gruppe Touristen vor dem Kölner Dom stehen und wartest auf Fragen.
    Bitte beantworte die folgende Frage eines Touristen mit einer kurzen und prägnanten 
    Antwort. Die Antwort sollte einen Bezug zu einem der kölschen Grundgesetze haben.
    """ + query_data.query

    print (prompt)

    completion = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7
    )

    print(completion)
    return {"response": completion.choices[0].text.strip()}

@app.get("/healthcheck")
async def healthcheck():
    """
    Check the status of the API.
    ---
    responses:
      200:
        description: The API is running.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: The status message.
    """
    return {"message": "Status: OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)