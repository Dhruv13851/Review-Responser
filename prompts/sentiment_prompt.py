from langchain_core.prompts import ChatPromptTemplate


class SentimentPrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an expert sentiment analysis assistant.

Your job is to classify the customer's review into ONLY ONE category.

Categories:
- positive
- neutral
- negative

Do not explain.

Return structured output only.
"""
                ),
                (
                    "human",
                    """
Review:

{review}
"""
                )
            ]
        )