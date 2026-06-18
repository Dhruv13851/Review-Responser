# from langchain_core.runnables import RunnableBranch, RunnablePassthrough

# from services.review_service import ReviewService


# def main():

#     service = ReviewService()

#     sentiment_chain = service.get_sentiment_chain()

#     positive_chain = service.get_positive_chain()

#     neutral_chain = service.get_neutral_chain()

#     negative_chain = service.get_negative_chain()

#     print("=" * 60)
#     print("     AI Review Response System")
#     print("=" * 60)

#     review = input("\nEnter Customer Review:\n\n")

#     # STEP 1: detect sentiment
#     sentiment_result = sentiment_chain.invoke(
#         {"review": review}
#     )

#     sentiment = sentiment_result.sentiment

#     print("\n" + "=" * 60)
#     print(f"Detected Sentiment: {sentiment.upper()}")
#     print("=" * 60)

#     # STEP 2: routing logic
#     workflow = RunnableBranch(

#         (
#             lambda x: sentiment == "positive",
#             positive_chain
#         ),

#         (
#             lambda x: sentiment == "negative",
#             negative_chain
#         ),

#         neutral_chain
#     )

#     # STEP 3: generate response
#     result = workflow.invoke(
#         {"review": review}
#     )

#     # STEP 4: unified output (because everything is ReviewResultModel)
#     print("\n" + "=" * 60)

#     print(f"Sentiment : {result.sentiment}")

#     if result.category:
#         print(f"Category  : {result.category}")

#     if result.reason:
#         print(f"Reason    : {result.reason}")

#     if result.requires_human_support is not None:
#         print(f"Human Support Required : {result.requires_human_support}")

#     print("\nAI Response:\n")
#     print(result.response)


# if __name__ == "__main__":
#     main()
from datetime import datetime, UTC

from database.review_repository import ReviewRepository
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
)

from services.review_service import ReviewService


def main():

    service = ReviewService()

    sentiment_chain = service.get_sentiment_chain()
    positive_chain = service.get_positive_chain()
    neutral_chain = service.get_neutral_chain()
    negative_chain = service.get_negative_chain()

    print("=" * 60)
    print("     AI Review Response System")
    print("=" * 60)

    review = input("\nEnter Customer Review:\n\n")

    # STEP 1: Detect sentiment / validate review
    sentiment_result = sentiment_chain.invoke(
        {"review": review}
    )

    # Reject non-review inputs
    if sentiment_result.status == "rejected":

        print("\n" + "=" * 60)
        print("INPUT REJECTED")
        print("=" * 60)

        print(f"\n{sentiment_result.message}")

        return

    print("\n" + "=" * 60)
    print(
        f"Detected Sentiment: "
        f"{sentiment_result.sentiment.upper()}"
    )
    print("=" * 60)
    
    # STEP 2: Build routing workflow
    workflow = RunnableBranch(

        (
            lambda x: x["sentiment"] == "positive",
            RunnableLambda(
                lambda x: {"review": x["review"]}
            )
            | positive_chain,
        ),

        (
            lambda x: x["sentiment"] == "negative",
            RunnableLambda(
                lambda x: {"review": x["review"]}
            )
            | negative_chain,
        ),

        RunnableLambda(
            lambda x: {"review": x["review"]}
        )
        | neutral_chain,
    )

    # STEP 3: Generate response
    result = workflow.invoke(
        {
            "review": review,
            "sentiment": sentiment_result.sentiment,
        }
    )
    document = result.model_dump()

    document["review"] = review
    document["created_at"] = datetime.now(UTC)

    ReviewRepository.save(document)

    # STEP 4: Display output
    print("\n" + "=" * 60)

    print(f"Sentiment : {result.sentiment}")

    if result.category:
        print(f"Category  : {result.category}")

    if result.reason:
        print(f"Reason    : {result.reason}")

    if result.requires_human_support is not None:
        print(
            "Human Support Required : "
            f"{result.requires_human_support}"
        )

    print("\nAI Response:\n")
    print(result.response)


if __name__ == "__main__":
    main()