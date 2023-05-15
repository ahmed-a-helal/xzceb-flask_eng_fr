""" This is the main file for deploying a traslation webpage using python flask
"""
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """ this method is used to transilate text from english to french when called 
    Returns:
        str: translated Text
    """
    text_to_translate = request.args.get('textToTranslate')
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    """ 
    this method is used to transilate text from french to english when called 
    Returns:
        str: translated Text
    """
    text_to_translate = request.args.get('textToTranslate')
    return translator.french_to_english(text_to_translate)

@app.route("/")
def render_index_page():
    """
    this method is called when accessing the website homepage URL
    and renders the "index.html" webpage
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
