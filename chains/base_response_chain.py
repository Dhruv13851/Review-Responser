from abc import ABC, abstractmethod


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

    @abstractmethod
    def get_output_model(self):
        """
        Returns the Pydantic model for structured output.
        """
        pass

    def get_chain(self):
        """
        Builds and returns the RunnableSequence.
        """

        return (
            self.get_prompt()
            | self.llm.with_structured_output(
                self.get_output_model()
            )
        )