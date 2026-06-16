from config.llm import LLMFactory

from chains.sentiment_chain import SentimentChain
from chains.positive_chain import PositiveChain
from chains.neutral_chain import NeutralChain
from chains.negative_chain import NegativeChain


class ReviewService:
    """
    Creates and manages all LangChain chains.

    Responsibility:
    - Create the LLM
    - Initialize all chains
    - Expose them through getter methods
    """

    def __init__(self):

        llm = LLMFactory.get_llm()

        self._sentiment_chain = SentimentChain(llm).get_chain()

        self._positive_chain = PositiveChain(llm).get_chain()

        self._neutral_chain = NeutralChain(llm).get_chain()

        self._negative_chain = NegativeChain(llm).get_chain()

    def get_sentiment_chain(self):
        return self._sentiment_chain

    def get_positive_chain(self):
        return self._positive_chain

    def get_neutral_chain(self):
        return self._neutral_chain

    def get_negative_chain(self):
        return self._negative_chain