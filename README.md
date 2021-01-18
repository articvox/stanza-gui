## Installation
1. `pip install -r requirements.txt`

## Running
1. Execute the script by typing in the command line: `py start.py`.
1. Click `Start NLP`.  
This will download the Chinese language model (if missing) and start stanza's language processing pipeline.
Wait until stanza has completed loading the language processor. This is indicated by the following information in the
GUI's output console:
    ```
    "zh" is an alias for "zh-hans"  
    Downloading default packages for language: zh-hans (Simplified_Chinese)...
    File exists: C:\Users\user\stanza_resources\zh-hans\default.zip.
    Finished downloading models and saved to C:\Users\user\stanza_resources.
    "zh" is an alias for "zh-hans"
    Loading these models for language: zh-hans (Simplified_Chinese):
    =======================
    | Processor | Package |
    -----------------------
    | tokenize  | gsdsimp |
    =======================
    
    Use device: cpu
    Loading: tokenize
    Done loading processors!
    ```
1. Paste the input into the left-side text area.
1. Click `Analyze`.
1. Copy the text processing output from the output console.