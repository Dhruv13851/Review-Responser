# from langchain_core.runnables import RunnableBranch, RunnablePassthrough

# from services.review_service import ReviewService


# def main():

#     service = ReviewService()

#     sentiment_chain = service.get_sentiment_chain()

#     positive_chain = service.get_positive_chain()

#     neutral_chain = service.get_neutral_chain()

#     negative_chain = service.get_negative_chain()

#     workflow = (

#         RunnablePassthrough.assign(

#             sentiment=lambda x: sentiment_chain.invoke(
#                 {
#                     "review": x["review"]
#                 }
#             ).sentiment

#         )

#         | RunnableBranch(

#             (

#                 lambda x: x["sentiment"] == "positive",

#                 positive_chain

#             ),

#             (

#                 lambda x: x["sentiment"] == "negative",

#                 negative_chain

#             ),

#             neutral_chain

#         )

#     )

#     print("=" * 60)
#     print("      AI Review Response Generator")
#     print("=" * 60)

#     review = input("\nEnter Customer Review:\n\n")

#     response = workflow.invoke(
#         {
#             "review": review
#         }
#     )

#     print("\nAI Response:\n")

#     print(response)


# if __name__ == "__main__":
#     main()

from langchain_core.runnables import RunnableBranch

from services.review_service import ReviewService


def main():

    service = ReviewService()

    sentiment_chain = service.get_sentiment_chain()

    positive_chain = service.get_positive_chain()

    neutral_chain = service.get_neutral_chain()

    negative_chain = service.get_negative_chain()

    print("=" * 60)
    print("         AI Review Response Generator")
    print("=" * 60)

    review = input("\nEnter Customer Review:\n\n")

    # Step 1: Detect sentiment
    sentiment_result = sentiment_chain.invoke(
        {
            "review": review
        }
    )

    sentiment = sentiment_result.sentiment

    print("\n" + "=" * 60)
    print(f"Detected Sentiment : {sentiment.upper()}")
    print("=" * 60)

    # Step 2: Create workflow
    workflow = RunnableBranch(

        (
            lambda x: sentiment == "positive",
            positive_chain
        ),

        (
            lambda x: sentiment == "negative",
            negative_chain
        ),

        neutral_chain

    )

    # Step 3: Generate response
    response = workflow.invoke(
        {
            "review": review
        }
    )

    print("\nAI Response:\n")

    print(response)


if __name__ == "__main__":
    main()