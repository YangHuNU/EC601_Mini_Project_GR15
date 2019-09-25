from google.cloud import language_v1
from google.cloud.language_v1 import enums


def sample_analyze_entity_sentiment(gcs_content_uri):
    """
    Analyzing Entity Sentiment in text file stored in Cloud Storage
    Args:
      gcs_content_uri Google Cloud Storage URI where the file content is located.
      e.g. gs://[Your Bucket]/[Path to File]
    """

    client = language_v1.LanguageServiceClient()
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    for entity in response.entities:
        # Only output the entities with 'CONSUMER_GOOD' type  
        if format(enums.Entity.Type(entity.type).name) == 'CONSUMER_GOOD':
            print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type
            print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
            print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
            sentiment = entity.sentiment
            print(u"Entity sentiment score: {}".format(sentiment.score))
            print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{} = {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
                print(
                    u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
                )
            print(' ')

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    print('')


    # Output the total Score and Magnitude of the text
    sentiment = client.analyze_sentiment(document).document_sentiment

    print('The total SCORE of the text: {}'.format(sentiment.score))
    print('The total MAGNITUDE of the text: {}'.format(sentiment.magnitude))

if __name__ == '__main__':
    sample_analyze_entity_sentiment('gs://juul_project/juul.txt')


