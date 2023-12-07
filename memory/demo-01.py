"""
written by:   Eugene M.
              https://github.com/apexDev37

date:         dec-2023

demo:         Conversation-Dialogs: dialog and query an LLM on previously discussed
              user experiences.
"""

import os

import openai
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from langchain.memory import ConversationBufferMemory

from utils.constants import Commands

CHATGPT_MODEL: str = "gpt-3.5-turbo"


def setup_openai_model(model: str = CHATGPT_MODEL) -> BaseChatModel:
    """
    Load API key from env file and returns Open AI model.

    Note:
        Defaults to use `gpt-3.5-turbo`.
    """

    # If you don't have one, see:
    # https://platform.openai.com/account/api-keys
    _ = load_dotenv(dotenv_path=".envs/keys.env")
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    return ChatOpenAI(
        temperature=0.0,
        model=CHATGPT_MODEL,
    )


def init_interactive_conversation() -> None:
    """Initiates an interactive user prompt loop."""

    while True:
        user_input = input("[prompt] >>> ")
        if user_input.strip().lower() in Commands.TERMINATE:
            break
        yield user_input


def main() -> None:
    """Script entry-point func."""

    llm = setup_openai_model()
    memory = ConversationBufferMemory()

    # Create a chain to store history of conversations
    # using the `BufferMemory` and pass as context to the LLM.
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False,
    )

    # Launch an interactive conversation in your terminal.
    for user_prompt in init_interactive_conversation():
        ai_response = conversation.predict(input=user_prompt)
        print("[AI] >>>", ai_response)


if __name__ == "__main__":
    main()
