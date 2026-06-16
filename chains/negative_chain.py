from chains.base_response_chain import BaseResponseChain
from prompts.negative_prompt import NegativePrompt


class NegativeChain(BaseResponseChain):

    def get_prompt(self):

        return NegativePrompt.get_prompt()