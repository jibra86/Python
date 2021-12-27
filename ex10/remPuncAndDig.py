import pathlib
import string

# This concatenates the three strings together. Each string is from the string
# module. The result is "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
CHARACTER_TO_DELETE = string.whitespace + string.punctuation + string.digits


def character_not_to_delete(character):
    """
    This function checks if the character is not in the character_to_delete.
    """
    return character not in CHARACTER_TO_DELETE


def clean_file():
    """
    This function recreate the content of the file without any whitespace 
    character, punctuation or digits.
    """
    file_name = pathlib.Path(input("Enter the name of the file: "))

    # This open the file, return the content and close the file, thanks to Path
    file_content = file_name.read_text()

    # Use a comprehension list to create a list of characters that are not in
    # the character_to_delete
    create_list_of_allowed_character = [c for c in file_content
                                        if character_not_to_delete(c)]

    # Concatenate the list of characters to create a string
    new_content = ''.join(create_list_of_allowed_character)

    # This open the file, write the new content and close the file
    file_name.write_text(new_content)

if __name__ == "__main__":
    clean_file()
