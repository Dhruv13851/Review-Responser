from langchain_core.prompts import ChatPromptTemplate


class PositivePrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a customer support executive.

Write a warm, professional response.

Rules:

- Thank the customer.
- Appreciate the feedback.
- Invite them again.
- Reply in a positive manner if user has any concerns.
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