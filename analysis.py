




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


file_path = "Search in Transition_final versione.xlsx"

# The actual data are in this sheet
df = pd.read_excel(
    file_path,
    sheet_name="Form responses 1"
)

print("Original dataset shape:", df.shape)


df.columns = (
    df.columns
    .astype(str)
    .str.replace("\n", " ", regex=False)
    .str.strip()
)

print("\nColumn names:")
for column in df.columns:
    print(column)

consent_column = "I voluntarily agree to participate in this study."

df = df[
    df[consent_column]
    .astype(str)
    .str.strip()
    .eq("Yes, I agree")
].copy()

print("\nClean dataset shape:", df.shape)


age_col = "What is your birth year range? (e.g., 18–20)"

gender_col = "What is your gender?"

cgpa_col = (
    "Please select your current CGPA range "
    "(on a 4.00 scale)."
)

test_col = (
    "Which English language test are you preparing for?"
)

llm_frequency_col = (
    "How often do you use LLMs "
    "(e.g., ChatGPT) for English test preparation?"
)

search_frequency_col = (
    "How often do you use Google or other search engines "
    "for English test preparation?"
)

llm_satisfaction_col = (
    "How satisfied are you with the accuracy of LLMs "
    "in solving English test problems?"
)

search_satisfaction_col = (
    "How satisfied are you with the accuracy of search engines "
    "in solving English test problems?"
)

llm_efficiency_col = (
    "How efficient are LLMs in helping you complete "
    "English test tasks?"
)

search_efficiency_col = (
    "How efficient are search engines in helping you complete "
    "English test tasks?"
)

llm_ease_col = (
    "How easy is it to use LLMs for English test problem solving?"
)

search_ease_col = (
    "How easy is it to use search engines for English test problem solving?"
)

preference_col = (
    "Which tool do you prefer overall for English test preparation?"
)




frequency_mapping = {

    "Never": 1,

    "Occasionally": 2,

    "Sometimes": 3,

    "Often": 4,

    "Always": 5

}




satisfaction_mapping = {

    "Very Dissatisfied": 1,

    "Dissatisfied": 2,

    "Neutral": 3,

    "Satisfied": 4,

    "Very Satisfied": 5

}



efficiency_mapping = {

    "Not Efficient at All": 1,

    "Slightly Efficient": 2,

    "Moderately Efficient": 3,

    "Very Efficient": 4,

    "Extremely Efficient": 5

}




ease_mapping = {

    "Very Difficult": 1,

    "Difficult": 2,

    "Neutral": 3,

    "Easy": 4,

    "Very Easy": 5

}




df["LLM_Use_Frequency"] = (
    df[llm_frequency_col]
    .map(frequency_mapping)
)

df["Search_Use_Frequency"] = (
    df[search_frequency_col]
    .map(frequency_mapping)
)

df["LLM_Satisfaction"] = (
    df[llm_satisfaction_col]
    .map(satisfaction_mapping)
)

df["Search_Satisfaction"] = (
    df[search_satisfaction_col]
    .map(satisfaction_mapping)
)

df["LLM_Efficiency"] = (
    df[llm_efficiency_col]
    .map(efficiency_mapping)
)

df["Search_Efficiency"] = (
    df[search_efficiency_col]
    .map(efficiency_mapping)
)

df["LLM_Ease"] = (
    df[llm_ease_col]
    .map(ease_mapping)
)

df["Search_Ease"] = (
    df[search_ease_col]
    .map(ease_mapping)
)




print("\nNumeric Likert Data:")
print(
    df[
        [
            "LLM_Use_Frequency",
            "Search_Use_Frequency",
            "LLM_Satisfaction",
            "Search_Satisfaction",
            "LLM_Efficiency",
            "Search_Efficiency",
            "LLM_Ease",
            "Search_Ease"
        ]
    ].head()
)




department_data = {
    "Department": [
        "Computer Science & Engineering (CSE)",
        "Electrical & Electronics Engineering (EEE)",
        "Business Administration (BBA)",
        "Data Science",
        "English",
        "Other"
    ],
    "Count": [
        72,
        24,
        18,
        12,
        10,
        4
    ]
}

department_df = pd.DataFrame(department_data)




cgpa_df = (
    df[cgpa_col]
    .value_counts()
    .reindex(
        [
            "3.81–4.00",
            "3.51–3.80",
            "3.01–3.50",
            "2.50–3.00"
        ],
        fill_value=0
    )
    .reset_index()
)

cgpa_df.columns = [
    "CGPA Range",
    "Count"
]




gender_df = (
    df[gender_col]
    .value_counts()
    .reindex(
        [
            "Male",
            "Female",
            "Prefer not to say",
            "Other"
        ],
        fill_value=0
    )
    .reset_index()
)

gender_df.columns = [
    "Gender",
    "Count"
]




age_df = (
    df[age_col]
    .value_counts()
    .reindex(
        [
            "18–20 years",
            "21–25 years",
            "26–30 years"
        ],
        fill_value=0
    )
    .reset_index()
)

age_df.columns = [
    "Age Range",
    "Count"
]




print("\n==============================")
print("CGPA DISTRIBUTION")
print("==============================")

print(cgpa_df)


print("\n==============================")
print("GENDER DISTRIBUTION")
print("==============================")

print(gender_df)


print("\n==============================")
print("AGE DISTRIBUTION")
print("==============================")

print(age_df)




department_df.to_csv(
    "department_distribution.csv",
    index=False
)

cgpa_df.to_csv(
    "cgpa_distribution.csv",
    index=False
)

gender_df.to_csv(
    "gender_distribution.csv",
    index=False
)

age_df.to_csv(
    "age_distribution.csv",
    index=False
)




boxplot_columns = [

    "LLM_Ease",

    "LLM_Efficiency",

    "LLM_Satisfaction",

    "LLM_Use_Frequency",

    "Search_Ease",

    "Search_Efficiency",

    "Search_Satisfaction",

    "Search_Use_Frequency"

]


boxplot_df = df[boxplot_columns].copy()


# Rename labels for publication-quality figure

boxplot_labels = [

    "LLM Ease",

    "LLM Efficiency",

    "LLM Satisfaction",

    "LLM Use Frequency",

    "Search Ease",

    "Search Efficiency",

    "Search Satisfaction",

    "Search Use Frequency"

]


# ------------------------------------------------------------
# CREATE BOXPLOT
# ------------------------------------------------------------

plt.figure(
    figsize=(11, 7)
)


plt.boxplot(

    boxplot_df.values,

    vert=False,

    labels=boxplot_labels,

    patch_artist=True,

    showmeans=True,

    meanline=True

)


plt.title(

    "Distribution of Survey Measures for LLMs and Search Engines",

    fontsize=14,

    fontweight="bold"

)


plt.xlabel(

    "Likert Score (1 = Lowest, 5 = Highest)",

    fontsize=11

)


plt.xlim(

    0.8,

    5.2

)


plt.xticks(

    [1, 2, 3, 4, 5],

    [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]

)


plt.grid(

    axis="x",

    linestyle="--",

    alpha=0.5

)


plt.tight_layout()


plt.savefig(

    "boxplot_quantitative_features_actual_data.png",

    dpi=300,

    bbox_inches="tight"

)


plt.show()




preferred_df = (

    df[preference_col]

    .value_counts()

    .reindex(

        [

            "Both (Hybrid use)",

            "LLMs (e.g., ChatGPT)",

            "Search engines (e.g., Google)"

        ],

        fill_value=0

    )

    .reset_index()

)


preferred_df.columns = [

    "Tool",

    "Students"

]


print("\n==============================")
print("OVERALL TOOL PREFERENCE")
print("==============================")

print(preferred_df)




plt.figure(

    figsize=(10, 6)

)


bars = plt.bar(

    preferred_df["Tool"],

    preferred_df["Students"]

)


plt.title(

    "Overall Tool Preference Among Survey Participants",

    fontsize=14,

    fontweight="bold"

)


plt.ylabel(

    "Number of Students",

    fontsize=11

)


plt.xlabel(

    "Preferred Tool",

    fontsize=11

)


plt.xticks(

    rotation=20,

    ha="right"

)


plt.grid(

    axis="y",

    linestyle="--",

    alpha=0.5

)


# Add values above bars

for bar in bars:

    height = bar.get_height()

    plt.text(

        bar.get_x()
        +
        bar.get_width()
        /
        2,

        height + 1,

        str(int(height)),

        ha="center",

        va="bottom",

        fontsize=11

    )


plt.tight_layout()


plt.savefig(

    "preferred_tool_usage_actual_data.png",

    dpi=300,

    bbox_inches="tight"

)


plt.show()




descriptive_statistics = (

    df[boxplot_columns]

    .describe()

    .T

)


descriptive_statistics.to_csv(

    "descriptive_statistics.csv"

)


print("\n==============================")
print("DESCRIPTIVE STATISTICS")
print("==============================")

print(

    descriptive_statistics

)


# ============================================================
# 16. SAVE CLEANED ANALYSIS DATA
# ============================================================

analysis_columns = [

    age_col,

    gender_col,

    cgpa_col,

    test_col,

    preference_col,

    "LLM_Use_Frequency",

    "Search_Use_Frequency",

    "LLM_Satisfaction",

    "Search_Satisfaction",

    "LLM_Efficiency",

    "Search_Efficiency",

    "LLM_Ease",

    "Search_Ease"

]


analysis_df = df[analysis_columns].copy()


analysis_df.to_csv(

    "cleaned_analysis_data.csv",

    index=False

)


print("\n========================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("========================================")

print(

    "All figures and CSV files have been generated."

)
