from google import genai
from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()

# # Instantiate the Gemini client.
# It automatically retrieves GEMINI_API_KEY from the environment.
client = genai.Client()


def auto_categorize(note):
    """
    Categorizes a raw expense note into a predefined list of categories
    using the Gemini LLM.
    """
    prompt = f"""
    You are an automated financial categorizer. 
    Look at this expense note: '{note}'.
    You must strictly categorize it into exactly one of these five categories:
    Food, Subscriptions, Transportation, Entertainment, Other.
    
    Reply with ONLY the category name. No punctuation. No explanation.
    """

    try:
        # Sent the prompt to the Gemini API
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )

        # Extract the text and remove leading/trailing whitespace
        return response.text.strip()  # type: ignore

    except Exception as e:
        # Fallback category if the API call fails or times out
        print(f"API Error: {e}")
        return "Other"


# Execution tests
if __name__ == "__main__":
    print("Testing 'Shawarma':", auto_categorize("Shawarma"))
    print(
        "Testing 'Uber ride to the airport':",
        auto_categorize("Uber ride to the airport"),
    )
    print("Testing 'Spotify':", auto_categorize("Spotify"))
