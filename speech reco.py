import cv2
import pytesseract
from deep_translator import GoogleTranslator, single_detection


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract\\tesseract.exe'

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera



# Prompt the user for their preference
user_input = input("Select translation option:\n1. English to Japanese ('ej')\n2. Japanese to English ('je')\n3. English to Tagalog ('et')\n4. Tagalog to English ('te')\n5. Japanese to Tagalog ('jt')\n6. Tagalog to Japanese ('tj')\nPress Enter for default (English to Japanese): ")

while True:
    # Prompt the user to choose input type
    input_type = input("Choose input type:\n1. Image ('i')\n2. Speech ('s')\n")

    if input_type.lower() == 'i':
        while True:
            # Capture a single frame
            ret, frame = cap.read()

            # Check if the frame was captured successfully
            if not ret:
                print("Error: Unable to capture frame.")
                break

            # Display the captured frame
            cv2.imshow('Captured Frame', frame)

            # Break the loop if 's' key is pressed
            if cv2.waitKey(1) == ord('s'):
                break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to extract text from the image
        if user_input.lower() == 'je':
            text = pytesseract.image_to_string(gray, lang='jpn')
        elif user_input.lower() == 'jt':
            text = pytesseract.image_to_string(gray, lang='jpn')
        else:
            text = pytesseract.image_to_string(gray)

    
    else:
        print("Invalid input type. Please choose 'i' for image or 's' for speech.")
        continue

    # Print extracted text for debugging
    print("Extracted Text:", text)

    # Check if the text is not empty before language detection
    if text.strip():  # Check if text is non-empty after stripping whitespaces
        # Detect the language of the extracted text
        lang = single_detection(text, api_key="5cf53df6b39a3b76fca8e091ab3229f2")

        # Translate the text based on user input
        if user_input.lower() == 'ej':
            # English to Japanese translation
            translated_text = GoogleTranslator(source='en', target='ja').translate(text)
        elif user_input.lower() == 'je':
            # Japanese to English translation
            translated_text = GoogleTranslator(source='ja', target='en').translate(text)
        elif user_input.lower() == 'et':
            # English to Tagalog translation
            translated_text = GoogleTranslator(source='en', target='tl').translate(text)
        elif user_input.lower() == 'te':
            # Tagalog to English translation
            translated_text = GoogleTranslator(source='tl', target='en').translate(text)
        elif user_input.lower() == 'jt':
            # Japanese to Tagalog
            translated_text = GoogleTranslator(source='ja', target='tl').translate(text)
        elif user_input.lower() == 'tj':
            # Tagalog to Japanese
            translated_text = GoogleTranslator(source='tl', target='ja').translate(text)
        else:
            # Default to English to Japanese translation
            translated_text = GoogleTranslator(source='en', target='ja').translate(text)

        # Print translated text for debugging
        print("Translated Text:", translated_text)

    # Ask the user if they want to continue
    while True:
        user_choice = input("Do you want to continue? (yes/no): ")
        if user_choice.lower() == 'yes':
            break
        elif user_choice.lower() == 'no':
            cap.release()
            cv2.destroyAllWindows()
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    
    # Ask the user if they want to change their preferred language
    while True:
        change_language = input("Do you want to change your preferred language? (yes/no): ")
        if change_language.lower() == 'yes':
            user_input = input("Select new translation option:\n1. English to Japanese ('ej')\n2. Japanese to English ('je')\n3. English to Tagalog ('et')\n4. Tagalog to English ('te')\n5. Japanese to Tagalog ('jt')\n6. Tagalog to Japanese ('tj')\nPress Enter for default (English to Japanese): ")
            break
        elif change_language.lower() == 'no':
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
