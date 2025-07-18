import os
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# load housing data
data = Path("./data/housing.csv")
df = pd.read_csv(data)

llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))
sdf = SmartDataframe(df, config={"llm": llm})

prompt = "What's the median value of median_house_value?"
result = sdf.chat(prompt)

print(f">> PANDAS AI: {result}")


prompt = "how much is the correlation between population and median house value?"
response = sdf.chat(prompt)
print(f"** PANDAS AI: {response}")

## output
# ** PANDAS AI: The correlation between population and median house value is very weak, with a value of -0.02464967888889502

prompt = "plot the histogram for this dataset for median_income"
response = sdf.chat(prompt)
print(f"** PANDAS AI: {response}")