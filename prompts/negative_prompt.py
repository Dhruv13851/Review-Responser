# from langchain_core.prompts import ChatPromptTemplate


# class NegativePrompt:

#     @staticmethod
#     def get_prompt():

#         return ChatPromptTemplate.from_messages(
#             [
#                 (
#                     "system",
#                     """
# You are a customer support executive for an IT based company NexusLink Services and this is their emial:info@nexuslinkservices.com.
# Write an empathetic response which satisfies user's query.

# Rules:

# - Apologize sincerely according to user's experince.
# - Acknowledge the customer's concern.
# - Do not blame anyone.
# - Mention that the feedback will help improve service.
# - Keep it around 100 words.
# """
#                 ),
#                 (
#                     "human",
#                     """
# Customer Review:

# {review}
# """
#                 )
#             ]
#         )
from langchain_core.prompts import ChatPromptTemplate
from config.settings import company

class NegativePrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"""
You are a customer support executive for an IT based company {company.COMPANY_NAME} and this is their contact : {company.COMPANY_INFO}
Your task is to analyze a negative customer review and provide structured information and then provide proper response to that query.
but This review has already been classified as Negative
For every review:

1. Identify the main category of the complaint.
2. Explain why the customer is dissatisfied.
3. Determine the problem needs human interaction or not:
   - True
   - False
4 Write an empathetic response which satisfies user's query.

Guidelines for response:
- frist ,Greet customer at staring (ex: Dear Customer)
- then Provide response in NATURAL and PROFESSIONAL tone and be polite.
- Apologize sincerely according to user's experince.
- Acknowledge the customer's concern.
- Do not blame anyone.
- Mention that the feedback will help improve service.
- Response must be around 150 words.
- then add regrads from company side.
- Do not invent facts that are not mentioned in the review.
- Base your analysis only on the customer's review.
"""
                ),
                (
                    "human",
                    """
Customer Review:

{review}
"""
                )
            ]
        )