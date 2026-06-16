from langchain_core.prompts import ChatPromptTemplate


class NeutralPrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a customer support executive.

Write a polite and professional reply.

Rules:

- Thank the customer.
- Acknowledge their feedback.
- Encourage them to visit again.
- Keep it under 70 words.
"""
                ),
                (
                    "human",
                    """
Customer Review:

{review}
"""
                )
            ]
        )