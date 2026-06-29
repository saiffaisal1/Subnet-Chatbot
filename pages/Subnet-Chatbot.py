import os
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

class ResearchResponse(BaseModel):
    summary: str
    source: list[str]
    tools_used: list[str]

st.title("Subnet Chatbot")
st.caption("An expert AI assistant for IP addressing & subnetting")

@st.cache_resource

def build_parser():
    parser = PydanticOutputParser(pydantic_object=ResearchResponse)
    return parser


def build_agent():
    parser = build_parser()

    llm = ChatOpenAI(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        openai_api_key=st.secrets["OPENROUTER_API_KEY"],
        openai_api_base="https://openrouter.ai/api/v1"
    )

    agent = create_agent(
        model=llm,
        tools=[],
        system_prompt=f"""
        You are a Subnetting Chatbot, an expert teaching assistant for university students
        learning computer networking. Your specialty is IP addressing and subnetting,
        including Fixed Length Subnet Masking (FLSM) and Variable Length Subnet Masking (VLSM),
        CIDR notation and supernetting.
        Wrap your final output in this exact JSON format and provide no other text:
        {parser.get_format_instructions()}
        """,
    )

    return agent

agent = build_agent()
parser = build_parser()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.messages = []  
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if query := st.chat_input("Ask me about subnetting, VLSM, CIDR..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    response_text = "" 

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                history = [
                    ("human" if m["role"] == "user" else "assistant", m["content"])
                    for m in st.session_state.messages
                ]

                result = agent.invoke({"messages": history})
                raw_output = result["messages"][-1].content
                structured_response = parser.parse(raw_output)

                response_text = structured_response.summary  
                st.markdown(response_text)

                with st.expander("Sources"):
                    for src in structured_response.source:
                        st.write(f"- {src}")

                with st.expander("Tools Used"):
                    for tool in structured_response.tools_used:
                        st.write(f"- {tool}")

            except Exception as e:
                response_text = f"Error: {e}"
                st.error(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})  