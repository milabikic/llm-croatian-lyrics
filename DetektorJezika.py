import os
import langid
import shutil

def detektiraj_jezik(text):
    """Input: text. Output: language of the text."""
    language, confidence = langid.classify(text)
    return language

def citanje_datoteke(file_path, alternative_encodings):
    """Read file content using alternative encodings."""
    for encoding in alternative_encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as input_file:
                return input_file.read()
        except UnicodeDecodeError:
            continue
    return None

def sortiraj_hrvatski(source_folder, destination_folder):
    """Move files with Croatian content to a separate folder."""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    alternative_encodings = ['utf-8', 'iso-8859-1', 'cp1252']

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        print(filename)

        if os.path.isfile(file_path):
            # Read the content of the file using alternative encodings
            content = citanje_datoteke(file_path, alternative_encodings)

            if content is not None:
                # Detect the language of the content
                language = detektiraj_jezik(content)

                # Check if the detected language is Croatian
                if language == 'hr':
                    # Copy the file to the Croatian folder
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.copy(file_path, destination_path)
                    print(f"File '{filename}' copied to the 'hrvatski' folder.")

