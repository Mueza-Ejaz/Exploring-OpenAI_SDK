import os
import asyncio
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AgentHooks,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled
)

# Load environment variables
load_dotenv()
set_tracing_disabled(True)

# Get GEMINI API key 
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Set up the API client and model 
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  
    openai_client=client
)




# Create custom hooks class
class MyHooks(AgentHooks):
    async def on_start(self, _agent, _context):
        print(" Agent started working.")

    async def on_complete(self, _agent, _context, output):
        print(f" Agent completed. Final output:\n{output}")

    async def on_error(self, _agent, _context, error):
        print(f" Agent error: {error}")




# Create an agent with hooks
agent = Agent(
    name="Friendly Agent",
    instructions="Help the user in a friendly way.",
    model=model,
    hooks=MyHooks()  #  Hooks connected here!
)



# Run the agent
async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Hi, can you give me tips for job interviews?"
    )
    print("\n=== Final Output ===")
    print(result.final_output)



#  Run it
if __name__ == "__main__":
    asyncio.run(main())


# output:
#  Agent started working.

# === Final Output ===
# Hey there! I'd be happy to help you with some job interview tips. Here's a breakdown of things to focus on, broken down into before, during, and after the interview:

# **I. Before the Interview: Preparation is Key!**

# *   **Understand the Job Description:**
#     *   **Read it carefully:** Identify the key skills, experiences, and qualifications the employer is seeking.
#     *   **Highlight keywords:** These will be useful when tailoring your resume and crafting your answers.
#     *   **Identify the core responsibilities:** What will you be doing day-to-day?
# *   **Research the Company:**
#     *   **Website:** Explore their "About Us," "Mission," "Values," "Products/Services," and "News" sections.
#     *   **Social Media:** Check their LinkedIn, Twitter, Facebook, and other relevant platforms to understand their culture and current activities.
#     *   **Industry News:** Look for recent articles or press releases about the company to stay updated on their performance and any challenges they might be facing.
#     *   **Glassdoor/Indeed:** Read employee reviews to get insights into the company's work environment.
# *   **Prepare Answers to Common Interview Questions:**
#     *   **"Tell me about yourself":** This is your elevator pitch. Focus on relevant experience and skills that align with the job description. (Keep it concise - 2-3 minutes max.)
#     *   **"Why are you interested in this role/company?":** Show genuine enthusiasm and explain how the role aligns with your career goals.
#     *   **"What are your strengths and weaknesses?":** Be honest and provide specific examples. For weaknesses, focus on areas you are actively working to improve.
#     *   **"Describe a time when you failed and how you handled it":** Focus on what you learned from the experience and how it made you a better professional. 
#     *   **"Tell me about a time you had to overcome a challenge/conflict":** Use the STAR method (Situation, Task, Action, Result) to provide a clear and concise response.
#     *   **"Where do you see yourself in 5 years?":** Show ambition and demonstrate how this role will contribute to your long-term career goals.
#     *    **"Why should we hire you?":** Summarize your key skills and experiences and explain how you can contribute to the company's success.
# *   **Prepare Questions to Ask the Interviewer:**
#     *   This shows your interest and engagement. Good questions include:
#         *   "What are the biggest challenges facing the team/company right now?"
#         *   "What does a typical day/week look like in this role?"
#         *   "What opportunities are there for professional development and growth within the company?"
#         *   "What is the company culture like?"
#         *   "How will my performance be evaluated?"
# *   **Practice, Practice, Practice!**
#     *   **Mock Interviews:** Ask a friend, family member, or career counselor to conduct mock interviews with you. This will help you get comfortable answering questions and identify areas for improvement.
#     *   **Record Yourself:** Use your phone or computer to record yourself answering common interview questions. This will allow you to analyze your body language, tone of voice, and overall presentation.
#     *   **Mirror Practice:** Practice in front of a mirror to observe your facial expressions and body language.
# *   **Plan Your Outfit:**
#     *   Choose professional attire that is appropriate for the company's culture. When in doubt, business casual is a safe bet.
#     *   Make sure your clothes are clean, wrinkle-free, and fit well.
#     *   Pay attention to details such as shoes, accessories, and grooming.
# *   **Logistics:**
#     *   **Confirm the interview details:** Double-check the date, time, location (physical or virtual), and interviewer's name and contact information.        
#     *   **Plan your route/test your technology:** If it's an in-person interview, plan your route and factor in potential traffic delays. If it's a virtual interview, test your internet connection, camera, and microphone beforehand.
#     *   **Prepare necessary documents:** Bring copies of your resume, cover letter, portfolio (if applicable), and any other relevant materials.

# **II. During the Interview: Making a Great Impression**

# *   **First Impressions Matter:**
#     *   **Be on time (or a few minutes early):** Punctuality demonstrates respect for the interviewer's time. For virtual interviews, log in a few minutes early to ensure everything is working correctly.
#     *   **Greet the interviewer with a smile and a firm handshake (if in person):** Make eye contact and introduce yourself confidently.
#     *   **Maintain good posture:** Sit up straight and avoid slouching.
# *   **Communication is Key:**
#     *   **Listen carefully:** Pay close attention to the interviewer's questions and avoid interrupting.
#     *   **Answer thoughtfully:** Take a moment to gather your thoughts before responding. Provide concise and relevant answers.
#     *   **Use the STAR method:** When describing your experiences, use the STAR method (Situation, Task, Action, Result) to provide clear and compelling examples.
#     *   **Be enthusiastic:** Show genuine interest in the role and the company.
#     *   **Speak clearly and confidently:** Project your voice and avoid using filler words such as "um" or "like."
#     *   **Maintain eye contact:** This shows that you are engaged and attentive.
#     *   **Be honest and authentic:** Don't exaggerate your skills or experience. Be yourself and let your personality shine through.
# *   **Body Language:**
#     *   **Maintain good eye contact:** Show that you are engaged and attentive.
#     *   **Smile:** A genuine smile can make you appear more approachable and likable.
#     *   **Nod:** Show that you are listening and understanding.
#     *   **Avoid fidgeting:** This can be distracting and make you appear nervous.
#     *   **Use hand gestures:** Use natural hand gestures to emphasize your points.
# *   **Answering Difficult Questions:**
#     *   **Don't be afraid to take a moment to think:** It's better to pause and gather your thoughts than to blurt out an answer you'll regret.
#     *   **Be honest and transparent:** If you don't know the answer, admit it and offer to find out.
#     *   **Focus on the positive:** Even when discussing failures or challenges, focus on what you learned from the experience.
#     *   **Stay calm and professional:** Even if the interviewer asks a difficult or uncomfortable question, remain calm and maintain a professional demeanor.  
# *   **Asking Questions:**
#     *   **Ask thoughtful questions:** This shows that you are engaged and interested in the role and the company.
#     *   **Avoid asking questions that can be easily answered by researching the company online.**
#     *   **Don't be afraid to ask for clarification:** If you don't understand a question, ask the interviewer to rephrase it.
# *   **Closing the Interview:**
#     *   **Reiterate your interest in the role:** Thank the interviewer for their time and express your enthusiasm for the opportunity.
#     *   **Summarize your key qualifications:** Briefly highlight your skills and experience and explain how you can contribute to the company's success.       
#     *   **Ask about the next steps in the hiring process:** This shows that you are proactive and eager to move forward.
#     *   **Thank the interviewer again and shake their hand (if in person):** Make eye contact and leave a positive lasting impression.

# **III. After the Interview: Following Up and Learning**

# *   **Send a Thank-You Note:**
#     *   **Within 24 hours:** Send a personalized thank-you note (email is fine) to each interviewer.
#     *   **Reiterate your interest:** Briefly mention something specific you discussed in the interview to show you were engaged.
#     *   **Reinforce your qualifications:** Briefly remind them of your key skills and how they align with the role.
#     *   **Proofread carefully:** Ensure there are no typos or grammatical errors.
# *   **Reflect on the Interview:**
#     *   **What went well?** Identify the aspects of the interview that you feel good about.
#     *   **What could be improved?** Identify areas where you could have performed better.
#     *   **What did you learn?** Reflect on the questions you were asked and the information you learned about the company and the role.
# *   **Follow Up (If Necessary):**
#     *   **If you haven't heard back within the timeframe discussed:** Send a brief follow-up email to inquire about the status of your application.
#     *   **Be polite and professional:** Reiterate your interest in the role and thank them for their time.
# *   **Don't Give Up:**
#     *   **Rejection is a part of the job search process.** Don't be discouraged if you don't get the job.
#     *   **Learn from your experiences:** Use each interview as an opportunity to improve your skills and refine your approach.
#     *   **Stay positive and persistent:** Keep applying for jobs and attending interviews until you find the right fit.

# **Key Takeaways:**

# *   **Be Prepared:** Thorough preparation is the foundation of a successful interview.
# *   **Be Yourself:** Authenticity and genuine enthusiasm go a long way.
# *   **Be Professional:** Maintain a professional demeanor throughout the entire process.
# *   **Be Persistent:** Don't give up, even if you face rejection.

# I hope these tips are helpful! Good luck with your job interviews! Let me know if you have any other questions. I am here to help!









