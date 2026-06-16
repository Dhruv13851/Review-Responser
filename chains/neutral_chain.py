from chains.base_response_chain import BaseResponseChain
from prompts.neutral_prompt import NeutralPrompt


class NeutralChain(BaseResponseChain):

    def get_prompt(self):

        return NeutralPrompt.get_prompt()