import pytesseract


def extract_text(image):

    try:

        text = pytesseract.image_to_string(
            image,
            lang="eng"
        )

        return text.strip()

    except Exception as e:

        return ""
