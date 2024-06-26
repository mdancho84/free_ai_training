# BUSINESS SCIENCE UNIVERSITY
# AI CRM DEALS ANALYSIS
# PANDAS AGENT: CHAT WITH YOUR DATA

# AI COURSE LAUNCH ON THURSDAY, MAY 30TH AT 2PM EST:
#  👉 REGISTER HERE: https://learn.business-science.io/python-generative-ai-apps

# GOALS:
# 1. SHOW HOW AI CAN BE USED FOR DATA SCIENCE
# 2. SHOW SOME OF THE LOW-LEVEL DATA SCIENCE TASKS THAT CAN BE AUTOMATED WITH AI

# LIBRARIES

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

import pandas as pd
import yaml

# OPENAI SETUP:
OPENAI_API_KEY = yaml.safe_load(open('../credentials.yml'))['openai']

# PANDAS DATA FRAME:

df = pd.read_csv("data/sales_pipeline.csv")
df

# 1.0 CREATE A PANDAS AI AGENT:

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,  
    api_key=OPENAI_API_KEY
)

pandas_agent = create_pandas_dataframe_agent(
    model,
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# 2.0 NATURAL LANGUAGE QUESTIONS AND INVOKING OUR AGENT

pandas_agent.invoke("What are the column names in the data?")


pandas_agent.invoke("How many deals were won?")


pandas_agent.invoke("What is the average value for deals that were won?")
