let addTaskButton = document.querySelector('#addTaskButton');
let tasksContainer = document.querySelector('#tasksContainer');

addTaskButton.addEventListener('click', (e) =>{
    e.preventDefault();
    addTaskButton.remove();

    let inputGroup = document.createElement('div');
    let input = document.createElement('input');
    let button = document.createElement('button');

    inputGroup.className = 'input-group mt-4';

    input.className = 'form-control';
    input.type = 'text';
    input.placeholder = 'Write your task here';
    input.setAttribute('aria-label', 'Write your task here');
    input.setAttribute('aria-describedby', 'basic-addon1');

    button.className = 'btn btn-secondary ml-2';
    button.id = 'submitTask';
    button.type = 'submit';
    button.innerHTML = 'Submit Task';

    button.addEventListener('click', (e) =>{
        e.preventDefault();

        //POST to backend
        //TODO

        //TEMPORARY
        taskList.push('test');
        window.location.replace(window.location.href);
    })

    tasksContainer.appendChild(inputGroup);
    inputGroup.appendChild(input);
    inputGroup.appendChild(button);
})