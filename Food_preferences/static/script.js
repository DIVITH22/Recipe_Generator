let step = 0;
let userResponses = {
    ingredients: "",
    preference: "",
    style: "",
    age: ""
};

const questions = [
    "What ingredients do you have?",
    "Do you prefer veg or non-veg?",
    "What style of food do you want? (eg: Tamil Nadu/Kerala)",
    "Please provide your age."
];

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${sender.toLowerCase()}`;
    messageElement.innerHTML = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
function displayLoadingAnimation() {
    const chatBox = document.getElementById("chat-box");
    const loadingElement = document.createElement("div");
    loadingElement.className = "message bot loading";
    loadingElement.innerHTML = "<div class='dot-animation'><span>.</span><span>.</span><span>.</span></div>";
    chatBox.appendChild(loadingElement);
    chatBox.scrollTop = chatBox.scrollHeight;
    return loadingElement;
}

function removeLoadingAnimation(loadingElement) {
    loadingElement.remove();
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    displayMessage(message, "User");
    input.value = "";

    if (step < questions.length) {
        userResponses[Object.keys(userResponses)[step]] = message;
        step++;
        
        if (step < questions.length) {
            displayMessage(questions[step], "Bot");
        } else {
            const loadingElement = displayLoadingAnimation();
            
            fetch("/get_food_recommendations", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(userResponses)
            })
            .then(response => response.json())
            .then(data => {
                removeLoadingAnimation(loadingElement);
                if (data.error) {
                    displayMessage("Oops! Something went wrong: " + data.error, "Bot");
                } else {
                    displayMessage("Here are four food items based on your preferences:", "Bot");
                    displayMessage(`<p>${data.foodItems}</p>`, "Bot");
                }
            })
            .catch(error => {
                removeLoadingAnimation(loadingElement);
                displayMessage("An error occurred while fetching recommendations. Please try again.", "Bot");
                console.error("Error:", error);
            });
        }
    }
}

window.onload = function() {
    displayMessage(questions[0], "Bot");
};

document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});