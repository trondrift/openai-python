import io
import openai
import requests
from PIL import Image, ImageDraw, ImageFont

# Set up the OpenAI API client
openai.api_key = ''

# Prompt for generating the text of the post
prompt = "Generate a sentence featuring https://melophobix.com/ about the Grand Rapids music scene"

# def generate_text(prompt):
#     completions = openai.Completion.create(
#         engine='davinci',
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
    
#     message = completions.choices[0].text
#     return message



# Generate the text for the post using OpenAI's GPT-3 model
response = openai.Completion.create(
    engine='text-davinci-002',
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.9,
)

text = response.choices[0].text

# Download an image to use as the background of the post
# image_url = "https://source.unsplash.com/1600x900/?sunset"
# image_data = requests.get(image_url).content

# # Create a PIL image object from the downloaded image data
# background = Image.open(io.BytesIO(image_data))

# # Create a new image to use as the post
# post = Image.new('RGB', (1080, 1080), color=(255, 255, 255))

# # Draw the background image onto the post
# post.paste(background)

# Save the post to a file
print(text);
#post.save('instagram_post.jpg')
