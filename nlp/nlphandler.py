import logging
import threading

import stanza


class NLPHandler(threading.Thread):
    """Starts the pipeline in a thread. Resulting process
    can be called once the language module is downloaded and the
    pipeline is ready.

    Process output is logged using the provided logger."""

    def __init__(self, logger: logging.Logger):
        super().__init__()

        self.nlp = None
        self.ready = False

        self.logger = logger

    def run(self) -> None:
        self.start_pipeline()

    def start_pipeline(self) -> None:
        stanza.download('zh')

        self.nlp = stanza.Pipeline(
            lang = 'zh',
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
