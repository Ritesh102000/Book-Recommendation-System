from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # You can use other email services like SendGrid, etc.
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "royaldelhi11@gmail.com"  # Your email
app.config['MAIL_PASSWORD'] = 'jpoq obqr fcmj cwce'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'royaldelhi77@gmail.com'  # Your email
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

df = pd.read_csv("Books.csv")

@app.route('/')
def index():
    # Get the page number from the query parameter (default to 1)
    page = int(request.args.get('page', 1))
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    
    # Paginate the books
    books = df.iloc[start:end].to_dict('records')
    
    # Total pages
    total_pages = (len(df) + per_page - 1) // per_page
    
    # Pass max to the template
    return render_template('index.html', books=books, page=page, total_pages=total_pages, max=max, min=min)

@app.route('/book/<title>')
def book_detail(title):
    try:
        # Get the book details from Books.csv
        book = df[df['Book-Title'] == title]
        if book.empty:
            return f"Book with title '{title}' not found.", 404
        book = book.iloc[0].to_dict()

        # Load recommendations
        try:
            recommendations_df = pd.read_csv("recommendations.csv")
        except Exception as e:
            print(f"Error reading recommendations.csv: {e}")
            recommendations_df = pd.DataFrame()

        # Fetch recommendations
        recommendation_row = recommendations_df[recommendations_df['Book'] == title]
        if not recommendation_row.empty:
            # Get recommended books
            recommended_titles = recommendation_row.iloc[0]['Recommendations'].split("@")
            recommended_titles = [item.strip() for item in recommended_titles]
            recommended_books = df[df['Book-Title'].isin(recommended_titles)].to_dict('records')
        else:
            # Fallback to popular books if no specific recommendations exist
            try:
                popular_df = pd.read_csv("popular_books.csv")
                popular_titles = popular_df['Book-Title'].head(6).tolist()
                recommended_books = df[df['Book-Title'].isin(popular_titles)].to_dict('records')
            except Exception as e:
                print(f"Error reading popular.csv: {e}")
                recommended_books = []

        return render_template("book_detail.html", book=book, recommended_books=recommended_books)

    except Exception as e:
        # Catch all unexpected errors
        print(f"Error processing book detail page for '{title}': {e}")
        return f"An error occurred while fetching book details. Please try again later.", 500


    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Check if all fields are filled
        if name and email and message:
            # Try sending the email
            try:
                msg = Message(
                    subject="Contact Form Submission",
                    recipients=["ritesh23075@iiitd.ac.in"],  # Replace with your email
                    body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
                )
                mail.send(msg)
                return render_template("index.html")
            except Exception as e:
                return render_template("contact.html")
        else:
            return render_template("contact.html", error="All fields are required. Please fill out the form.")
    
    # For GET request
    return render_template("contact.html")


@app.route('/developer')
def developer():
    return render_template('developer.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')




if __name__ == "__main__":
    app.run(debug=True)





