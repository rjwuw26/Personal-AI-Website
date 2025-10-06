/* 
    File: script.js
    Author: Ryan Wilkerson
    Version: 10/3/2025
    Description: JavaScript for handling chat interactions and animations.
*/

// DOM elements for chat and animations
const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const cards = document.querySelectorAll('.about-card');

// Animate cards when they enter the viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target); // Stop observing once visible
        }
    });
}, { threshold: 0.2 });

cards.forEach(card => observer.observe(card));

// Function to add messages to the chat container
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.classList.add(sender === "user" ? "user-message" : "ai-message");
    messageDiv.textContent = message;
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Send user message to backend and display response
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return; // <-- check the right variable

    // Display user message
    addMessage(message, 'user');
    userInput.value = "";

    try {
        // Send POST request to Flask backend
        const response = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: message }) // <-- send as 'question'
        });

        const data = await response.json();
        addMessage(data.answer, 'ai');
    } catch (error) {
        addMessage("Sorry, there was an error processing your request.", 'ai');
        console.error(error);
    }
}

// Event listeners for sending messages and Enter key
sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

