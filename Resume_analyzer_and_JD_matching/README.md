# Resume Analyzer
🚨🚨 You can use this chatbot for analize your resume "Resume Analyzer system".

## Features 🌟
submit1 = st.button("Summary About Resume")
submit2 = st.button("How Can I Improvise Skills")
submit3 = st.button("What are the Missing Keywords")
submit4 = st.button("Percentage match")
- **Summary**: Summary About Resume like what is Strenth and weekness of candidate.
- **Skills Imporvement**: How Can I Improvise Skills
- **Missing Ketywortds**: What are the Missing Keywords or skills which is not matching with your JD.
- **Percentage match**: This will give you  a percentage how much your resume is matching with Job Description (JD).

## Dive Deeper with code 🎥


## Technical Details 🛠️
- Set google cloud crendential from GCP console.
Create a Service Account:

- Go to the Google Cloud Console.
- Open the "IAM & Admin" section.
- Click on "Service accounts" and then "Create Service Account".
- Enter a name and description for the service account.
- Assign the necessary roles to the service account (e.g.,Cloud Vision API User if you are using Vision API).
- Click "Continue" and then "Done".
- Generate and Download JSON Key File:
- The key file will be downloaded to your computer.
- Set GOOGLE_APPLICATION_CREDENTIALS Environment Variable:
- Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the downloaded JSON key file. You can do this in your Streamlit application or set it in your system environment.
- Copy API key for your Google Gemini account and paste it in .env
- Create new enviroment with python==10 or greator.
- Install Requirement.txt
- Run app.py


## Getting started

```
cd existing_repo
git remote add origin 
git branch -M main
git push -uf origin main
```
