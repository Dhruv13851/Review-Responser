from typing import Literal

from pydantic import BaseModel, Field


class SentimentModel(BaseModel):

    sentiment: Literal[
        "positive",
        "neutral",
        "negative"
    ] = Field(
        description="Detected sentiment of the customer review."
    )