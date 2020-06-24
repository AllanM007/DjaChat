# DjaChat

This chatbot uses python,django,vuejs,html and css to provide a responsive chatbot that allows you to interact in real time with the bot and get quick responses.

The vuejs,html and css render a page that allows for user input that loads data as a json dictionary,sends the data to django backend for processing and a reply.

The django backend initializes a chatbot class  containing the corpus trainer which trains the bot based on the english corpus,the listrainer is initialized to process the custom questions the chatbot might be prompted to answer.

After the get-response function processes the data and returns a reply in form of a json dictionary,the vue app then stringifies the message.text and dishes out a reply processed by the chatbot trainer.
