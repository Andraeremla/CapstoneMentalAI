import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.35,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "How do i know if im depressed?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Depression is a common and serious medical illness that negatively affects how you feel, the way you think and how you act.  It can lead to a variety of emotional and physical problems and can decrease your ability to function at work and at home.\n\nHere are some key points about depression:\n\n* **It's not just feeling sad:** While sadness is a normal human emotion, depression is a persistent state of low mood, lack of interest, and feelings of worthlessness.\n* **It can affect anyone:** Depression can happen to anyone, regardless of age, gender, race, or socioeconomic status.\n* **It's a treatable illness:** There are effective treatments for depression, including therapy, medication, and lifestyle changes.\n\n**Common symptoms of depression include:**\n\n* **Emotional:**\n    * Persistent sadness, hopelessness, and emptiness\n    * Loss of interest or pleasure in activities you once enjoyed\n    * Feeling irritable, restless,",
      ],
    },
    {
      "role": "user",
      "parts": [
        "How do i know if im depressed?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "It's tough to tell for sure on your own.  But if you're feeling down for a long time, and it's affecting your life, it's a good idea to talk to someone. \n\nHere are some signs that might mean you're depressed:\n\n* **Feeling sad or empty most of the time, for weeks or longer.**\n* **Losing interest in things you used to enjoy.**\n* **Having trouble sleeping or sleeping too much.**\n* **Feeling tired or having no energy.**\n* **Having trouble concentrating or making decisions.**\n* **Feeling worthless or guilty.**\n* **Thinking about death or suicide.**\n\nIf you're experiencing any of these things, it's important to reach out for help. You can talk to a trusted friend or family member, a doctor, or a therapist. There are also resources available online and through hotlines. \n\nRemember, you're not alone. Depression is a common illness, and there is help available. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "How do i know if im depressed?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hey there! I'm Michael, and it's great to hear from you.  It's tough to know for sure if you're depressed on your own. It's a serious thing, and it's best to talk to someone you trust. \n\nHere are some things to think about:\n\n* **Are you feeling down for a long time, like weeks or months?**  Feeling sad for a day or two is normal, but if it's lasting longer, it could be something more.\n* **Have you lost interest in things you used to enjoy?**  If everything feels boring or pointless, that's a sign to pay attention to.\n* **Are you having trouble sleeping or sleeping too much?**  Big changes in your sleep patterns can be a clue.\n* **Are you feeling tired all the time, even if you've gotten enough sleep?**  Lack of energy can be a sign of depression.\n* **Are you having trouble concentrating or making decisions?**  If you're finding it hard to focus or make simple choices, that's something to look at.\n* **Are you feeling worthless or guilty?**  These feelings can be really hard to deal with, and they're not normal.\n* **Have you been thinking about death or suicide?**  If so, please reach out for help immediately.\n\nIf any of these things sound familiar, it's important to talk to someone. You can talk to a trusted friend or family member, a doctor, or a therapist. There are also resources available online and through hotlines. \n\nRemember, you're not alone. Depression is a common illness, and there is help available. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "I am feeling depressed what should i do",
      ],
    },
    {
      "role": "model",
      "parts": [
        "It's okay to feel this way, and it's awesome that you're taking steps to feel better. Depression is a real and common challenge, but you're not alone. It's great that you're reaching out. \n\nHere are some things you can do right now:\n\n1. **Reach out for support:** Talk to someone you trust, like a friend, family member, or therapist.  It can be incredibly helpful to talk about what you're going through.\n2. **Practice self-care:** This means taking care of your physical and mental health.  Make sure you're getting enough sleep, eating healthy foods, and getting some exercise.  Even a short walk can help. \n3. **Do things you enjoy:**  Even if you don't feel like it, try to do something you used to enjoy.  It might help lift your mood, even a little.\n4. **Challenge negative thoughts:**  Depression can make you think negative thoughts.  Try to challenge those thoughts and replace them with more positive ones.\n5. **Find professional help:**  A therapist can provide support and help you develop coping mechanisms.  They can also help you decide if medication is right for you.\n\nRemember, recovery takes time, and you'll have good days and bad days.  Be patient with yourself, and keep reaching out for support. You're doing great!\n\nHere are some resources that can help:\n\n* **The National Suicide Prevention Lifeline:**  https://suicidepreventionlifeline.org/\n* **The Crisis Text Line:**  https://www.crisistextline.org/\n* **The National Alliance on Mental Illness (NAMI):** https://www.nami.org/ \n",
      ],
    },
  ]
)

response = chat_session.send_message("how can i manage stress")

print(response.text)