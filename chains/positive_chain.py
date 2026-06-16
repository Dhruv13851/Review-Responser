from chains.base_response_chain import BaseResponseChain
from prompts.positive_prompt import PositivePrompt


class PositiveChain(BaseResponseChain):

    def get_prompt(self):

        return PositivePrompt.get_prompt()