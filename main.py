#from DetektorJezika import sortiraj_hrvatski

#source_folder = "C:\\Users\\milab\\OneDrive - FFUNIZG\\FFZG\\V\\Strojno učenje\\GeneratorHrvatskihTekstova\\tekstovi"

#destination_folder = "./hrvatski"

#sortiraj_hrvatski(source_folder, destination_folder)

import os

def zamijeni_prvi_red(folder_path):
    # Provjeri je li putanja direktorija ispravna
    if not os.path.isdir(folder_path):
        print(f"Putanja '{folder_path}' nije ispravna direktorij.")
        return

    # Prolazi kroz sve datoteke u mapi
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Provjeri je li datoteka TXT
        if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
            # Čita sadržaj datoteke
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Ako datoteka ima barem jedan redak, zamijeni prvi redak
            if lines:
                # Zamijeni prvi redak sa željenim tekstu
                lines[0] = f"[PROMPT] Kako izgleda pjesma izvođača {filename.split(' -')[0]} \n"

                # Piše promijenjeni sadržaj natrag u datoteku
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

                print(f"Prvi redak datoteke '{filename}' je zamijenjen.")
            else:
                print(f"Datoteka '{filename}' je prazna.")

folder_path = './hrvatski_400'
zamijeni_prvi_red(folder_path)

import os

def merge_txt_files(folder_path, output_file):
    # Verify if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Invalid directory path: '{folder_path}'.")
        return

    # Initialize an empty string to accumulate content
    merged_content = ""

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a TXT file
        if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Accumulate the content
            merged_content += content + '\n\n'  # You can adjust the delimiter as needed

    # Write the merged content to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(merged_content)

    print(f"All TXT files in '{folder_path}' merged into '{output_file}'.")

output_file = "./treniranje/400_prompt_answer.txt"

merge_txt_files(folder_path, output_file)

