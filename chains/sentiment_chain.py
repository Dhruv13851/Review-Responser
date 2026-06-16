from models.sentiment_model import SentimentModel
from prompts.sentiment_prompt import SentimentPrompt


class SentimentChain:

    def __init__(self, llm):

        self.llm = llm

    def get_chain(self):

        return (
            SentimentPrompt.get_prompt()
            | self.llm.with_structured_output(SentimentModel)
        )