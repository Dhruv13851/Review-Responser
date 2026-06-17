# from chains.base_response_chain import BaseResponseChain
# from prompts.negative_prompt import NegativePrompt


# class NegativeChain(BaseResponseChain):

#     def get_prompt(self):

#         return NegativePrompt.get_prompt()
from chains.base_response_chain import BaseResponseChain

from models.review_response_model import ReviewResultModel

from prompts.negative_prompt import NegativePrompt


class NegativeChain(BaseResponseChain):

    def get_prompt(self):
        return NegativePrompt.get_prompt()

    def get_output_model(self):
        return ReviewResultModel