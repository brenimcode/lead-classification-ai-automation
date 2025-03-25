import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')


def classifier():
    model = ChatGroq()

    classify_prompt = ChatPromptTemplate.from_template("""
    <Lead Quality Classification>
    You are a lead classification model for a technology consulting company. Your function is to classify the lead into one of three quality levels: "High", "Medium", or "Low".

    <General Rules>
    - Always return only one word: "High", "Medium", or "Low"
    - Base your response exclusively on the provided form fields

    <Classification Criteria>

    High:
    - Company: Large corporation or rapidly expanding
    - Contact: Decision-maker with high influence
    - Engagement: Consistent interactions (events, downloads, meetings) and clear urgency
    - Resources: Approved budget and defined timeline for decision

    Medium:
    - Company: Medium-sized with moderate growth
    - Contact: Influencer, but not the final decision-maker
    - Engagement: Demonstrated initial interest, but without evident budget or urgency
    - Resources: Needs identified, but pending authorization or timelines

    Low:
    - Company: Small business or with limited financial capacity
    - Contact: Incomplete data or operational contact (non-strategic)
    - Engagement: Few interactions and no concrete actions
    - Resources: No identified budget or non-priority need

    <Example>

    Input:
    Company: "TechCorp Ltd." - startup in technology sector
    Contact: "Carlos Oliveira", CTO
    Engagement: ["Cloud Migration Workshop", "AI Solutions Webinar", "Cybersecurity Masterclass"]
    Content Downloads: ["Enterprise Cloud Strategy Whitepaper", "AI Implementation Guide"]
    Tech Investment: "Budget approved for Q3/2024 ($500k+)"
    Company Size: "50-200 employees"

    Expected Output:
    High

    Input:
    {lead_data}

    Output:
    """,
    )

    classify_chain = classify_prompt | model | StrOutputParser()
    return classify_chain
