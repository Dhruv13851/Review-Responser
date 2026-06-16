from abc import ABC, abstractmethod

from langchain_core.output_parsers import StrOutputParser


class BaseResponseChain(ABC):
    """
    Base class for all response generation chains.
    """

    def __init__(self, llm):
        self.llm = llm

    @abstractmethod
    def get_prompt(self):
        """
        Returns the ChatPromptTemplate.
        """
        pass

    def get_chain(self):
        """
        Builds and returns the RunnableSequence.
        """

        return (
            self.get_prompt()
            | self.llm
            | StrOutputParser()
        )