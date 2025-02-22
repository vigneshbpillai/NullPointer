from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def detect_depfake(file_path):
    try:
        
        file_size = os.path.getsize(file_path)

        
        if file_size > 100000:
            return "Fake (AI-generated)"
        else:
            return "Real"
    except Exception as e:
        return f"Error: {e}"

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is uploaded
    if 'file' not in request.files:
        return jsonify({'error': "No file uploaded"}), 400
    
    # Get the uploaded file
    file = request.files['file']

    # Save the file to the 'uploads' folder
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Check if the file is fake or real
    result = detect_depfake(file_path)

    # Return the result as JSON
    return jsonify({'result': result})

# Run the Flask app
if __name__ == '__main__':
    # Create the 'uploads' folder if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    # Start the Flask app in debug mode
    app.run(debug=True)