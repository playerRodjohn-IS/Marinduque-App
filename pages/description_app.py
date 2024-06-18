import streamlit as st

# Page title and configuration
st.set_page_config(layout="wide", page_title="Streamlit App Features Description")

# Feature 1: Emotion Analyzer
st.header('Feature 1: Emotion Analyzer')
st.write('''
The Emotion Analyzer feature assesses emotions such as fear, anger, and joy based on textual inputs or interactions. Originally designed for analyzing sentiment from social media posts, comments, or text messages, this tool employs natural language processing (NLP) techniques to discern the underlying emotional tone. Users can input text to understand how their written communication might be perceived emotionally by others. Whether you're gauging the sentiment of online discussions, evaluating the emotional impact of marketing campaigns, or simply curious about the emotional content of text, this feature provides valuable insights into emotional expression in digital communications.
''')

# Feature 2: Image Classifier for Weapons
st.header('Feature 2: Image Classifier for Weapons')
st.write('''
The Image Classifier for Weapons categorizes images based on the presence of guns, swords, or bombs. Leveraging machine learning models trained on a diverse dataset of weapon-related images, this feature allows users to upload images or use predefined examples for classification. Whether you're concerned with monitoring security risks, analyzing historical artifacts, or exploring the visual representation of weaponry in media and art, this classifier accurately identifies and categorizes images containing various types of weapons. This tool is useful for security personnel, researchers, historians, and anyone interested in the visual depiction of arms and armaments.
''')

# Feature 3: Prediction of Emotion from Internet and Social Media Interaction
st.header('Feature 3: Prediction of Emotion from Internet and Social Media Interaction')
st.write('''
The Prediction of Emotion feature forecasts emotional responses such as happiness, sadness, excitement, and more based on user interactions across internet and social media platforms. By analyzing patterns in online behavior and communication styles, this predictive model offers insights into how digital interactions influence emotional well-being. Users can input their interaction data to receive predictions about their emotional reactions in digital environments. This feature is beneficial for understanding the emotional impact of online interactions, evaluating sentiment trends, and gaining deeper insights into personal emotional experiences online.
''')

# Footer
st.write("Explore these features to gain insights and enjoy interactive experiences with the Streamlit app!")
