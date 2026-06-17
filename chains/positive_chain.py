from chains.base_response_chain import BaseResponseChain
from prompts.positive_prompt import PositivePrompt
from models.review_response_model import ReviewResultModel


class PositiveChain(BaseResponseChain):

    def get_prompt(self):
        return PositivePrompt.get_prompt()

    def get_output_model(self):
        return ReviewResultModel