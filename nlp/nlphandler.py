import logging
import threading

import stanza


class NLPHandler(threading.Thread):
    """
    Starts the stanza language processing pipeline in a separate thread.

    Resulting language processing can be done after the language module has been downloaded
    and the tokenizing processor has been loaded as indicated by is_ready().

    Language processing output is logged to the provided logger on INFO level.
    """

    LANGUAGE = 'zh'

    def __init__(self, logger: logging.Logger):
        super().__init__()

        self.nlp = None
        self.ready = False

        self.logger = logger

    def run(self) -> None:
        self.__start_pipeline()

    def __start_pipeline(self) -> None:
        stanza.download(self.LANGUAGE)

        self.nlp = stanza.Pipeline(
            lang = self.LANGUAGE,
            processors = 'tokenize'
        )

        self.ready = True

    def process(self, text: str) -> None:
        if not self.ready:
            self.logger.error('Please wait until pipeline preparation has finished')
            return

        doc = self.nlp(text)

        for i, sentence in enumerate(doc.sentences):
            for token in sentence.tokens:
                self.logger.info(token.text)

    def is_ready(self) -> bool:
        return self.ready
