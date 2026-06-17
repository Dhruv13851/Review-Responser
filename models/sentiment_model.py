# from typing import Literal

# from pydantic import BaseModel, Field


# class SentimentModel(BaseModel):

#     sentiment: Literal[
#         "positive",
#         "neutral",
#         "negative"
#     ] = Field(
#         description="Detected sentiment of the customer review."
#     )

from typing import Literal, Optional

from pydantic import BaseModel, Field


class SentimentModel(BaseModel):

    status: Literal[
        "success",
        "rejected"
    ] = Field(
        description="Whether the input is a valid customer review."
    )

    sentiment: Optional[
        Literal[
            "positive",
            "neutral",
            "negative"
        ]
    ] = Field(
        default=None,
        description="Detected sentiment for a valid customer review."
    )

    message: Optional[str] = Field(
        default=None,
        description="Reason for rejection when the input is not a customer review."
    )