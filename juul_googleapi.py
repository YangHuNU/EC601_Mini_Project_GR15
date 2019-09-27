
from google.cloud import language_v1
from google.cloud.language_v1 import enums


def sample_analyze_entity_sentiment(gcs_content_uri):
    """
    Analyzing Entity Sentiment in text containing twitters with the keyword '#Juul'

    """
   
    client = language_v1.LanguageServiceClient()
    
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
    
    for entity in response.entities:
        # Only output the entities with 'CONSUMER_GOOD' type  
        if format(enums.Entity.Type(entity.type).name) == 'CONSUMER_GOOD':
            print(u"Representative name for the entity: {}".format(entity.name))
            print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
            print(u"Salience score: {}".format(entity.salience))
            sentiment = entity.sentiment
            print(u"Entity sentiment score: {}".format(sentiment.score))
            print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        
            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{} = {}".format(metadata_name, metadata_value))

            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
                print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
                )
            print(' ')

    # Get the language of the text
    print(u"Language of the text: {}".format(response.language))
    print('')


    # Output the total Score and Magnitude of the text
    sentiment = client.analyze_sentiment(document).document_sentiment

    print('The total SCORE of the text: {}'.format(sentiment.score))
    print('The total MAGNITUDE of the text: {}'.format(sentiment.magnitude))

if __name__ == '__main__':
    sample_analyze_entity_sentiment('gs://juul_project/juul.txt')


