from database.mongo_client import review_collection


class ReviewRepository:

    @staticmethod
    def save(document):
        review_collection.insert_one(document)