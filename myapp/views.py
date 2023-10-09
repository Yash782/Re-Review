from django.shortcuts import render
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# Create your views here.

def index(request):
    return render(request, 'input.html')

def sentiment_analysis(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text')  
        # Get the input from the user
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(user_input)
        compound_score = sentiment_scores['compound']  
        # Extract the compound sentiment score

        # Determine the sentiment label based on the compound score
        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        return render(request, 'input.html', {'sentiment': sentiment, 'score': compound_score})
    
    else:
        return render(request, 'input.html')
