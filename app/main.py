from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import uvicorn


app = FastAPI(title="AI Lead Classification API", description="API for classifying leads using an AI model.", version="1.0.0")

# Home route to test if the API is up
@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    Returns a simple hello world message.
    """
    return {"message": "Welcome to the AI Lead Classification API!"}

# Route to get a simple response (for debugging/testing)
@app.get("/response")
def response():
    """
    A simple endpoint returning a 'Hello World!' response.
    Useful for basic health checks or testing.
    """
    return JSONResponse(content={"response": "Hello, World!"})


# Route to classify leads based on incoming data
@app.post("/classify", response_model=LeadOutput)
def classify_lead(lead: LeadInput):
    """
    Classifies a lead based on its details. 
    Takes input data as a JSON body, processes it, 
    and classifies the lead into hot, warm, or cold.
    
    Arguments:
    - lead (LeadInput): A dictionary containing the lead's information.

    Returns:
    - A JSON response with the classification result.
    """
    
    # Example of a simple classification logic (this can be replaced with a real AI/ML model)
    if "sale" in lead.mensagem.lower() if lead.mensagem else "":
        classificacao = "quente"
    elif "interest" in lead.mensagem.lower() if lead.mensagem else "":
        classificacao = "morno"
    else:
        classificacao = "frio"

    # Create the LeadOutput instance
    mensagem_formatada = f"Lead {lead.nome} from {lead.empresa} is classified as {classificacao}."
    
    # Return the classification result as a JSON response
    return LeadOutput(
        nome=lead.nome,
        classificacao=classificacao,
        mensagem_formatada=mensagem_formatada
    )

# If this script is being run directly (e.g., python main.py), start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

