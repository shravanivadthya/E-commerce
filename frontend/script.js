function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value;

  if (!message.trim()) return;

  chatBox.innerHTML += `<div class="user"><strong>You:</strong> ${message}</div>`;
  input.value = "";

  q=${encodeURIComponent(message)}`)
    .then(res => res.json())
    .then(data => {
      if (data.length === 0) {
        chatBox.innerHTML += `<div class="bot"><strong>Bot:</strong> No matching products found.</div>`;
      } else {
        let results = data.map(
          p => `<div><strong>${p.name}</strong><br>₹${p.price}<br>${p.description}</div><hr>`
        ).join("");
        chatBox.innerHTML += `<div class="bot"><strong>Bot:</strong><br>${results}</div>`;
      }
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
      chatBox.innerHTML += `<div class="bot"><strong>Bot:</strong> Server error. Try again later.</div>`;
    });
}
