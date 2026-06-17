from pydantic import BaseModel, Field


class ReviewResultModel(BaseModel):

    sentiment: str = Field(
        description="Detected sentiment of the review."
    )

    response: str = Field(
        description="Response generated for the customer."
    )

    category: list[str] | str | None = Field(
        default=None,
        description="Issue category."
    )

    reason: list[str] | str | None = Field(
        default=None,
        description="Reason behind the detected sentiment."
    )

    requires_human_support: bool | None = Field(
        default=None,
        description="Whether human intervention is recommended."
    )