from chains.base_response_chain import BaseResponseChain
from prompts.neutral_prompt import NeutralPrompt
from models.review_response_model import ReviewResultModel

class NeutralChain(BaseResponseChain):

    def get_prompt(self):
        return NeutralPrompt.get_prompt()

    def get_output_model(self):
        return ReviewResultModel