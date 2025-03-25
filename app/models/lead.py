from pydantic import BaseModel
from typing import Optional
from typing_extensions import Literal

# Pydantic model for incoming lead data (Lead Input)
class LeadInput(BaseModel):
     # Informações da Empresa
    company_name: str  # Nome completo da empresa
    industry: str  # Setor de atuação (ex: Tecnologia, Saúde)
    company_size: str  # Número aproximado de funcionários (faixa)

    # Informações do Contato
    contact_name: str  # Nome completo do contato principal
    contact_role: str  # Cargo ocupado pelo contato (ex: CEO, Gerente)

    # Capacidade de Aquisição
    tech_investment : str  # Quanto a empresa investe em soluções de tecnologia


# Pydantic model for the lead output (Lead Output)
class LeadOutput(BaseModel):
    name: str
    classification: Literal["Low", "Medium", "High"]
    formatted_message: str
