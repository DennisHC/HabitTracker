let addHabitButton = document.querySelector('#addHabitButton');
let habitsContainer = document.querySelector('#habitsContainer');

addHabitButton.addEventListener('click', (e) =>{
    e.preventDefault();
    addHabitButton.remove();

    let inputGroup = document.createElement('div');
    let input = document.createElement('input');
    let button = document.createElement('button');

    inputGroup.className = 'input-group mt-4';

    input.className = 'form-control';
    input.type = 'text';
    input.placeholder = 'Write your habit here';
    input.setAttribute('aria-label', 'Write your habit here');
    input.setAttribute('aria-describedby', 'basic-addon1');

    button.className = 'btn btn-secondary ml-2';
    button.id = 'submitHabit';
    button.type = 'submit';
    button.innerHTML = 'Submit Habit';

    button.addEventListener('click', (e) =>{
        e.preventDefault();

        //POST to backend
        fetch('http://127.0.0.1:8000/api/addHabit', {
            method: 'POST',
            body: JSON.stringify({habit: 'input.value'})
        })
        .then(res => {
            if(res.status === 200)
                window.location.replace(window.location.href);
            else
                alert("Server did not receive the Habit!");
        })
        .then(data => {})
        .catch(err => console.log(err));
    })

    habitsContainer.appendChild(inputGroup);
    inputGroup.appendChild(input);
    inputGroup.appendChild(button);
})