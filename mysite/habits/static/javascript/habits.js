let tasklist = [
    'Do Homework',
    'Do Chores',
    'Do Something 1',
    'Do Something 2',
    'Do Something 3',
    'Do Something 4',
    'Do Something 5'
]

let habitlist = [
    'Habit 1',
    'Habit 2',
    'Habit 3'
]

let tasksListDisplay = document.querySelector('#tasklist');
let habitListDisplay = document.querySelector('#habitlist');

tasklist.forEach(taskText => {
    let taskHTML = document.createElement('div');
    let checkmark = document.createElement('input');
    let task = document.createTextNode(taskText);

    checkmark.setAttribute('type', 'checkbox');
    checkmark.className = 'mx-2';

    taskHTML.className = 'input-group-text text-wrap text-left my-3 mx-1';
    taskHTML.appendChild(checkmark);
    taskHTML.appendChild(task);

    tasksListDisplay.appendChild(taskHTML);
})

habitlist.forEach(habitText => {
    let habitHTML = document.createElement('div');
    let checkmark = document.createElement('input');
    let habit = document.createTextNode(habitText);

    checkmark.setAttribute('type', 'checkbox');
    checkmark.className = 'mx-2';

    habitHTML.className = 'input-group-text text-wrap text-left my-3 mx-1';
    habitHTML.appendChild(checkmark);
    habitHTML.appendChild(habit);

    habitListDisplay.appendChild(habitHTML);
})