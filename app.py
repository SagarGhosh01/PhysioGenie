#import necessary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai


from api_key import api_key


# configure the api key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
# safty 
safety_settings = [
  {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
{
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]


system_prompt="""

Geographic Tongue (Benign Migratory Glossitis):

Symptoms: Patchy areas on the tongue with a red and white border, resembling a "map."
Cause: Unknown; potentially linked to stress, allergies, or vitamin deficiencies.
Treatment:
Avoid triggers like spicy, acidic, or salty foods.
Use soothing oral rinses (e.g., antiseptic or saltwater rinses).
Rarely requires medication unless discomfort is significant.
Oral Thrush (Candidiasis):

Symptoms: Yellowish or white patches on the tongue that may scrape off, leaving red areas.
Cause: Fungal infection (Candida albicans), often due to antibiotics, poor oral hygiene, or a weakened immune system.
Treatment:
Use antifungal medications like Nystatin or Fluconazole.
Maintain good oral hygiene and avoid sugary foods.

Vitamin Deficiency:

Symptoms: A swollen, smooth, or discolored tongue, often with cracks or sores.
Cause: Deficiencies in B12, iron, or folate.
Treatment:
Address the deficiency with dietary changes or supplements (as prescribed by a doctor).
Foods rich in vitamins: leafy greens, nuts, seeds, eggs, and fish.
Allergic or Traumatic Lesions:

Symptoms: Red or ulcerated areas, possibly from irritation.
Cause: Allergies, sharp teeth, or accidental biting.
Treatment:
Use soothing gels or ointments.
Avoid the irritant if identified (e.g., certain foods or dental appliances).
Leukoplakia or Oral Cancer:

Symptoms: Persistent white or red patches that do not heal after 2 weeks.
Cause: Chronic irritation (e.g., smoking, alcohol), immune dysfunction, or cancer.
Action:
Seek immediate medical evaluation, including a biopsy if necessary.
Steps to Follow
1. Immediate Care
Rinse the mouth with warm saltwater (1 teaspoon of salt in 1 cup of water) 2–3 times daily.
Avoid hot, spicy, or acidic foods to reduce irritation.
Brush teeth gently with a soft toothbrush.
2. Diet and Nutrition
Stay hydrated and consume a balanced diet rich in vitamins and minerals.
Incorporate foods high in B12, iron, and zinc, such as:
Eggs, dairy, lean meat, fish.
Leafy greens, beans, and fortified cereals.

3. Visit a Healthcare Professional
When to consult:
If lesions persist for more than 2 weeks.
If pain is severe or affects eating and speaking.
If there is unusual growth or persistent white/red patches.
4. Professional Treatments
Your doctor may prescribe:
Antifungals: If a fungal infection is suspected.
Antivirals: If viral lesions (e.g., herpes) are involved.
Vitamin supplements: If deficiencies are confirmed.
Biopsy: If there is suspicion of precancerous or cancerous growth.
Preventive Measures

Oral Hygiene:
Brush twice daily and floss regularly.
Use antiseptic mouthwash to prevent infection.

Avoid Irritants:
Stop smoking and reduce alcohol intake.
Avoid sharp or hard foods that might injure the tongue.

please provide me an output response with these 4 headings detailed analysis,findings reports,recommendationsand next steps, treatment suggestions and conclusion.

"""

# MODEL CONFIG
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
    safety_settings=safety_settings
)
# set the page configuration

st.set_page_config(
    page_title="VirtualImage Analyist", page_icon=":robot:")

# set the logo
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNLm6zDXx0ouheoaDPduyuSCmCPrXF1VpHoQ&s", width=150)

# set the title
st.title("👩‍⚕️Virtual👾Image Analyist🧑‍⚕️❤️")

# set the subtitle
st.subheader("An AI Application That Can Help Users To Identify Medical Images.")
uploaded_file = st.file_uploader("Upload the medical image for analysis..", type=["jpg", "png", "jpeg"] )
if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Medical Image.', width=250)


submit_button = st.button("Generate the Analysis")

if submit_button:
    # process the uplod image
    image_data = uploaded_file.getvalue()


# making our image
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]


# making our prompt ready
    prompt_parts = [
        image_parts [0],
        system_prompt,
    ]

# generate the response


    response = model.generate_content(system_prompt)
    if response:
            st.title("Here is the Analysis based on your image.")
            st.write(response.text)