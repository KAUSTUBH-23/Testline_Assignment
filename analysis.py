import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --------------------
# Fetch Data from APIs (with SSL verification disabled)
# --------------------
def fetch_data(url, verify_ssl=True):
    try:
        response = requests.get(url, verify=verify_ssl)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# URLs (ensure these are correct)
current_quiz_url = "https://jsonkeeper.com/b/LLQT"
historical_quiz_url = "https://api.jsonserve.com/XgAgFJ"

# Fetch data with SSL verification disabled
current_data = fetch_data(current_quiz_url, verify_ssl=False)
historical_data = fetch_data(historical_quiz_url, verify_ssl=False)

# Check data availability
if current_data is None or historical_data is None:
    raise ValueError("Failed to fetch data. Check URLs or network connection.")



print("Current Quiz Data Structure:", current_data.keys())

# --------------------
# Process Data (Corrected)
# --------------------
def process_current_data(data):
    if 'quiz' not in data or 'questions' not in data['quiz']:
        raise KeyError("API response missing expected keys: 'quiz' or 'questions'")

    # Extract questions and rename 'id' to 'question_id' for consistency
    df = pd.DataFrame(data['quiz']['questions']).rename(columns={'id': 'question_id'})

    # Check if 'topic' is available or assign default
    if 'topic' not in df.columns:
        df['topic'] = data['quiz'].get('topic', 'Unknown')

    # Compute 'is_correct' based on options (existing logic)
    if 'options' in df.columns:
        df['is_correct'] = df['options'].apply(
            lambda opts: any(option.get('is_correct', False) for option in opts)
            if isinstance(opts, list) else False
        )
    else:
        print("⚠️ Warning: 'options' column missing. Setting 'is_correct' to False.")
        df['is_correct'] = False

    return df


print("Current DataFrame Columns:", current_df.columns)
print(current_df.head())

current_df = process_current_data(current_data)
print(current_df.columns)  # Ensure 'is_correct' is now present

print(current_data['quiz']['questions'][0])  # Print one question to check



print("Historical Data Structure:", historical_data)

def process_historical_data(data):
    if not isinstance(data, list):
        raise ValueError("Expected a list from the API response but got something else.")

    records = []
    for quiz in data:  # Iterate through the list
        if 'response_map' not in quiz:
            continue  # Skip entries without response_map

        topic = quiz['quiz'].get('topic', 'Unknown')
        for q_id, selected in quiz['response_map'].items():
            records.append({
                'quiz_id': quiz.get('quiz_id', 'N/A'),
                'question_id': q_id,
                'selected_option': selected,
                'is_correct': np.random.choice([True, False]),  # Replace with real logic
                'topic' : topic
            })

    return pd.DataFrame(records)

print("Historical DataFrame Columns:", historical_df.columns)


# Apply the function to the fetched data
historical_df = process_historical_data(historical_data)

# Debugging output
print("Processed Historical DataFrame:")
print(historical_df.head())


# historical_df = process_historical_data(historical_data)


if 'options' in current_df.columns:
    current_df['is_correct'] = current_df['options'].apply(
        lambda opts: any(option.get('is_correct', False) for option in opts) if isinstance(opts, list) else False
    )






# --------------------
# Analyze Data
# --------------------
def analyze_performance(df):
    analysis = {}

    # Check required columns
    required_columns = ['topic', 'is_correct', 'question_id']
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise KeyError(f"Missing columns: {missing}")

    # By Topic
    topic_analysis = df.groupby('topic').agg(
        total_questions=('question_id', 'count'),  # Now uses 'question_id'
        accuracy=('is_correct', 'mean')
    ).reset_index()
    analysis['topic'] = topic_analysis

    # By Difficulty (if applicable)
    if 'difficulty_level' in df.columns:
        difficulty_analysis = df.groupby('difficulty_level').agg(
            accuracy=('is_correct', 'mean')
        ).reset_index()
        analysis['difficulty'] = difficulty_analysis

    return analysis



current_analysis = analyze_performance(current_df)
historical_analysis = analyze_performance(historical_df)

# --------------------
# Generate Insights
# --------------------
def get_weak_topics(analysis, threshold=0.5):
    weak = analysis['topic'][analysis['topic']['accuracy'] < threshold]
    return weak.sort_values(by='accuracy').head(3)

def get_improvement_trend(historical_df):
    historical_df['quiz_id'] = historical_df['quiz_id'].astype(int)
    trend = historical_df.groupby('quiz_id')['is_correct'].mean().reset_index()
    trend['improvement'] = trend['is_correct'].diff().fillna(0)
    return trend

weak_topics = get_weak_topics(current_analysis)
improvement_trend = get_improvement_trend(historical_df)

# --------------------
# Create Recommendations
# --------------------
def generate_recommendations(weak_topics, improvement_trend):
    recommendations = []
    # Focus on weak topics
    for _, row in weak_topics.iterrows():
        recommendations.append(
            f"Practice more questions on {row['topic']} (Current Accuracy: {row['accuracy']:.0%})."
        )
    # Check if accuracy is improving
    last_trend = improvement_trend['improvement'].iloc[-1]
    if last_trend > 0:
        recommendations.append("You're improving! Keep up the consistent practice.")
    else:
        recommendations.append("Focus on consistent practice to see improvement.")
    return recommendations

recommendations = generate_recommendations(weak_topics, improvement_trend)

# --------------------
# Bonus: Student Persona
# --------------------
def define_student_persona(analysis):
    best_topic = analysis['topic'].loc[analysis['topic']['accuracy'].idxmax()]
    worst_topic = analysis['topic'].loc[analysis['topic']['accuracy'].idxmin()]
    return {
        'persona': f"Strong in {best_topic['topic']} ({best_topic['accuracy']:.0%}) but needs work in {worst_topic['topic']} ({worst_topic['accuracy']:.0%})",
        'strengths': [best_topic['topic']],
        'weaknesses': [worst_topic['topic']]
    }

student_persona = define_student_persona(current_analysis)

# --------------------
# Bonus: NEET Rank Prediction (Simplified)
# --------------------
def predict_neet_rank(historical_scores):
    # Mock data: Assume historical NEET scores and quiz scores
    X = np.array([70, 75, 80, 85, 90]).reshape(-1, 1)  # Quiz scores (last 5)
    y = np.array([5000, 4500, 4000, 3500, 3000])       # Corresponding NEET ranks

    model = LinearRegression()
    model.fit(X, y)
    latest_score = historical_scores[-1]  # Use the latest quiz score
    predicted_rank = model.predict([[latest_score]])
    return int(predicted_rank[0])

# Mock historical quiz scores (replace with actual data)
historical_scores = [70, 75, 80, 85, 90]
predicted_rank = predict_neet_rank(historical_scores)

# --------------------
# Output Results
# --------------------
print("\nWeak Areas:")
print(weak_topics[['topic', 'accuracy']])

print("\nRecommendations:")
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec}")

print(f"\nStudent Persona: {student_persona['persona']}")
print(f"Predicted NEET Rank: {predicted_rank} (Based on mock data)")

# Plotting
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(current_analysis['topic']['topic'], current_analysis['topic']['accuracy'])
plt.title('Accuracy by Topic')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(improvement_trend['quiz_id'], improvement_trend['is_correct'], marker='o')
plt.title('Improvement Trend Over Quizzes')
plt.xlabel('Quiz Attempt')
plt.ylabel('Accuracy')
plt.tight_layout()
plt.show()