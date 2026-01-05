from flask import Flask, render_template_string

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #2c3e50;
            color: white;
            padding: 16px;
            text-align: center;
        }
        main {
            padding: 40px;
            text-align: center;
        }
        a.button {
            display: inline-block;
            padding: 12px 20px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 20px;
        }
        a.button:hover {
            background-color: #2980b9;
        }
        footer {
            margin-top: 40px;
            color: #777;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Flask App</h1>
    </header>

    <main>
        <p>This is a simple Flask application using only HTML and CSS.</p>
        <a class="button" href="/health">Check Health</a>
        <footer>
            <p>© 2026 My Flask App</p>
        </footer>
    </main>
</body>
</html>
"""

HEALTH_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Health Check</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eafaf1;
            text-align: center;
            padding-top: 100px;
        }
        .status {
            display: inline-block;
            padding: 20px 40px;
            background-color: #2ecc71;
            color: white;
            font-size: 24px;
            border-radius: 8px;
        }
        a {
            display: block;
            margin-top: 30px;
            color: #2c3e50;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="status">OK</div>
    <a href="/">← Back to Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/health")
def health():
    return render_template_string(HEALTH_HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # nosec B104
