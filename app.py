from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    members = [
        {
            'name': 'Riki Indra Putra',
            'nim': '22.83.0875',
            'prodi': 'Teknik Komputer',
            'hobby': 'Billiard',
            'description': 'Ganteng',
            'photo': 'images/riki-photo.jpg'  # Adjust the path to your static images
        },
        {
            'name': 'Safira Nur Hidayah',
            'nim': '22.83.0924',
            'prodi': 'Teknik Komputer',
            'hobby': 'Memasak',
            'description': 'Cantik',
            'photo': 'images/safira-photo.jpg'  # Adjust the path to your static images
        },
        {
            'name': 'Tiara Citra Mustika',
            'nim': '22.83.0864',
            'prodi': 'Teknik Komputer',
            'hobby': 'Belajar',
            'description': 'Cantik',
            'photo': 'images/tiara-photo.jpg'  # Adjust the path to your static images
        }
    ]
    
    return render_template('index.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
