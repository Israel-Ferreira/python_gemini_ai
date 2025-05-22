from google import genai

import os

from dotenv import load_dotenv


load_dotenv()


GEMMA_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_text(prompt, api_key):
    client =  genai.Client(
        api_key=api_key
    )

    response =  client.models.generate_content_stream(
        model="gemma-3-12b-it",
        contents=prompt,
        config={
            "response_mime_type": "text/plain",
        }
    )


    for chunk in response:
        print(chunk.text, end="")

    

if __name__ == "__main__":

    print(
        """                                         
            #####  ###  #   # ####   ###      # # #  ###   #### 
            #  # #   #  # #  #   # #   #      ###  #   # #     
            #  # #   #   #   ####  #   #       #   #   # #     
            #  # #   #  #    #     #   #      ###  #   # #     
            #   #  ###  #     #      ###      # # #  ###   #### 
        """
    )

    prompt = """
        Gere uma receita de sobremesa envolvendo chocolate meio amargo.
        Não devem  ser geradas receitas que tenham frutas como por exemplo: banana, morango e kiwi.
    """


    generate_text(prompt, GEMMA_API_KEY)
    print()







