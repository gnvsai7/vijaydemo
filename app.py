
import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Get the color from the environment variable, default to lightblue
    background_color = os.environ.get('APP_COLOR', 'lightblue')
    app_name = os.environ.get('APP_NAME', 'My Docker App')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{app_name}</title>
        <style>
            body {{
                background-color: {background_color};
                font-family: sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #333;
                text-align: center;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 0.5em;
            }}
            p {{
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>Hello from {app_name}!</h1>
        <p>This page's background color is: <strong>{background_color}</strong></p>
        <p>It's dynamically set by the 'APP_COLOR' environment variable.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Listen on 0.0.0.0 for Docker access