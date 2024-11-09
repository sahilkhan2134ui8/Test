const createForm = document.getElementById('create-form');
const logDiv = document.getElementById('log-div');

createForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const fileName = document.getElementById('file-name').value;
    const fileContent = document.getElementById('file-content').value;
    fetch('/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            file_name: fileName,
            file_content: fileContent
        })
    })
    .then((response) => response.json())
    .then((data) => {
        logDiv.innerHTML = `<h2>Log</h2><pre>${data.message}</pre>`;
    })
    .catch((error) => {
        console.error(error);
    });
});
