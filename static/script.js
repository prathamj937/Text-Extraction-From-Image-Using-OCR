async function extractText() {
  const input = document.getElementById('imageInput');
  const file = input.files[0];

  if (!file) {
    alert("⚠️ Please upload an image first.");
    return;
  }

  const formData = new FormData();
  formData.append('image', file);

  const response = await fetch('/extract-text', {
    method: 'POST',
    body: formData
  });

  const result = await response.json();

  const outputDiv = document.getElementById('output');
  if (result.text) {
    outputDiv.innerText = result.text;
  } else {
    outputDiv.innerText = "❌ Could not extract text.";
  }
}
