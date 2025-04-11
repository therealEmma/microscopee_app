from flask import Flask, request, render_template
import sqlite3

# Custom function to calculate the real-life size
def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

# Initialize Flask app
app = Flask(__name__)

# Route to handle form + display
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            username = request.form["username"].strip()
            microscope = float(request.form["microscope_size"])  # ✅ matches form field
            magnification = float(request.form["magnification"])

            if not username:
                raise ValueError("Username cannot be empty")

            actual = calculate_real_size(microscope, magnification)

            # Save to database
            conn = sqlite3.connect("specimen_data.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS specimen (
                    username TEXT,
                    microscope_size REAL,
                    magnification REAL,
                    actual_size REAL
                )
            """)
            cursor.execute("INSERT INTO specimen VALUES (?, ?, ?, ?)", 
                        (username, microscope, magnification, actual))
            conn.commit()
            conn.close()

            result = f"{actual:.2f} µm"
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
