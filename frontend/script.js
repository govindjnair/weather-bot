async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    // Display user message
    const chatBox = document.getElementById('chat-box');
    const userDiv = document.createElement('div');
    userDiv.className = 'message user-message';
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.textContent = 'Typing...';
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = '';

    // Send message to FastAPI
    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message, sender_id: 'user' })
        });
        typingDiv.remove(); // Remove typing indicator
        const data = await response.json();
        if (data.response && data.response.responses) {
            data.response.responses.forEach(resp => {
                if (resp.text) {
                    const botDiv = document.createElement('div');
                    botDiv.className = 'message bot-message';
                    botDiv.textContent = resp.text;
                    chatBox.appendChild(botDiv);
                }
            });
            chatBox.scrollTop = chatBox.scrollHeight;
        } else {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'message bot-message';
            errorDiv.textContent = `Error: ${data.error || 'No response'}`;
            chatBox.appendChild(errorDiv);
        }
    } catch (error) {
        typingDiv.remove();
        const errorDiv = document.createElement('div');
        errorDiv.className = 'message bot-message';
        errorDiv.textContent = `Error: ${error.message}`;
        chatBox.appendChild(errorDiv);
    }
    chatBox.scrollTop = chatBox.scrollHeight;
}

function clearChat() {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';
}

// Allow sending message with Enter key
document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});