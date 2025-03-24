from pydantic import BaseModel
from typing import Optional
from typing_extensions import Literal

# Pydantic model for incoming lead data (Lead Input)
class LeadInput(BaseModel):
    nome: str
    email: str
    telefone: str
    empresa: str
    cargo: str
    mensagem: Optional[str]


# Pydantic model for the lead output (Lead Output)
class LeadOutput(BaseModel):
    nome: str
    classificacao: Literal["quente", "morno", "frio"]
    mensagem_formatada: str
