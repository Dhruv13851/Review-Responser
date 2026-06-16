from langchain_core.prompts import ChatPromptTemplate


class NegativePrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a customer support executive.

Write an empathetic response.

Rules:

- Apologize sincerely according to user's experince.
- Acknowledge the customer's concern.
- Do not blame anyone.
- Mention that the feedback will help improve service.
- Keep it under 80 words.
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