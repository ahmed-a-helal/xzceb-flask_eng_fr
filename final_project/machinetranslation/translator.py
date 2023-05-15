"""
this library is used to translate text into different languages using IBM WAtSON Transilator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException
from dotenv import load_dotenv
load_dotenv()
def translator(text_to_translate:str,
                lang_id: str='en-fr',
                version: str='2021-05-01',
                apikey: str=os.environ['apikey'],
                url:    str=os.environ['url']):
    """this function transilates text using ibm_language_transilator service on the cloud

    Args:
        text_to_translate (str): the text you want to transilate.
        
        lang_id (str, optional): the language model id "from-to" syntax 
        for example "fr-en" transilates english text to french.
        Defaults to 'en-fr'.
        
        version (str, optional): the version of the model IBM watson transilator model used. 
        Defaults to '2021-05-01'.
        
        apikey (str, optional): the api key given through ibmcloud cloud for IAMAuthentication.
        Defaults to os.environ['apikey'] using enviromental variable.
        
        url (str, optional): the url given of the instance of the language model deployed 
        through ibm cloud account for authentication.
        Defaults to os.environ['url']using enviromental variable.

    Returns:
        str: returns the transilated text output of the model deployed on the cloud
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(
    text=text_to_translate,
    model_id=lang_id).get_result()
    return str(json.loads(json.dumps(translation))["translations"][0]["translation"])


def english_to_french(english_text:str):
    """translates english text to french 

    Args:
        english_text (str): the english text to translate to french 
        if this variable is not passed this method will "please input text to translate"

    Returns:
        str: the french text output of the translation
    """
    if english_text is None or english_text == "" :
        output = "please input text to translate"
    else:
        try:
            output = translator(english_text,lang_id='en-fr')
        except ApiException:
            output = "The Service is unavailable or the service \
            Authentication is missing or missmatched"
    return output

def french_to_english(french_text:str):
    """translates french text to english 

    Args:
        french_text (str): the french text to translate to french 
        if this variable is not passed this method will "please input text to translate"

    Returns:
        str: the english text output of the translation
    """
    if french_text is None or french_text == "" :
        output = "please input text to translate"
    else:
        try:
            output = translator(french_text,lang_id='fr-en')
        except ApiException:
            output = "The Service is unavailable or the service \
                Authentication is missing or missmatched"
    return output
