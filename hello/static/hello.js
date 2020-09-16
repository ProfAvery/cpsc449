async function postData() {
    const first = document.getElementById('first');
    const last = document.getElementById('last');

    const form_data = {
        first_name: first.value,
        last_name: last.value
    };

    const response = await fetch('/greet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form_data)
    });

    return response.json();
}

function showGreeting() {
    const greeting = document.getElementById('greeting');

    greeting.classList.remove('hidden');
}

function setName(value) {
    const name = document.getElementById('name');

    name.textContent = value;
}


window.addEventListener('load', () => {
    const submit = document.getElementById('submit');

    submit.addEventListener('click', () => {
        postData().then(response => {
            console.log(response);
            setName(response.name);
            showGreeting();
        });
    });
});
