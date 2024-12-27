document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way

    const formData = new FormData();
    const imageFile = document.getElementById('imageInput').files[0];
    formData.append('file', imageFile);

    fetch('http://127.0.0.1:5000/predict', {  // URL to your Flask backend
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_class) {
            document.getElementById('result').innerText = 'Predicted class: ' + data.predicted_class;
        } else {
            document.getElementById('result').innerText = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = 'An error occurred: ' + error;
    });
});



