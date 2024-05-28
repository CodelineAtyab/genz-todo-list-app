# Import necessary libraries
import nltk
from resume_parser import resumeparse

# Download necessary NLTK models and corpora
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')


def reading_files():
    # Since the CV is in the same directory, just use the filename
    cv_path = 'abbas_cv.pdf'

    # Try to parse the CV using the resumeparse library
    try:
        # Parse the CV and store the data
        data = resumeparse.read_file(cv_path)

        # Print the parsed data
        print(data)
    except FileNotFoundError:
        print(f"Error: The file {cv_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while parsing the CV: {e}")


# Call the function to parse the CV
reading_files()
