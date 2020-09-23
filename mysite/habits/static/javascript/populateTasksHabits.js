let tasksListDisplay = document.querySelector('#tasklist');
let habitListDisplay = document.querySelector('#habitlist');

//Get Tasks from Server and populate them
fetch('http://127.0.0.1:8000/api/getTasks:' + userID)
.then(res => res.json())
.then(data => populateTasks(data.tasks))
.catch(err => console.log(err));

//Get Habits from Server and populate them
fetch('http://127.0.0.1:8000/api/getHabits:' + userID)
.then(res => res.json())
.then(data => populateHabits(data.habits))
.catch(err => console.log(err));

//Aux Functions that get called above
function populateTasks(taskList){
    taskList.forEach(taskText => {
        let taskHTML = document.createElement('div');
        let colDiv = document.createElement('div');
        let checkmark = document.createElement('input');
        let trashBtn = document.createElement('button');
        let img = document.createElement('img');
        let task = document.createTextNode(taskText);
    
        checkmark.type = 'checkbox';
        checkmark.className = 'mr-2';
    
        colDiv.className = 'col';
    
        img.src = '/static/images/trash.svg';
        img.alt = 'image loading failed';
    
        trashBtn.className = 'btn btn-secondary btn-sm mt-2 float-right';
        trashBtn.id = 'trashBtn';
        trashBtn.appendChild(img);
        trashBtn.addEventListener('click', (e) =>{
            e.preventDefault();
            taskHTML.remove();
        })
    
        taskHTML.className = 'input-group-text text-wrap text-left my-3 mx-1';
        taskHTML.appendChild(colDiv);
        
        colDiv.appendChild(checkmark);
        colDiv.appendChild(task);
        colDiv.appendChild(trashBtn);
    
        tasksListDisplay.appendChild(taskHTML);
    })
}

function populateHabits(habitList){
    habitList.forEach(habitText => {
        let habitHTML = document.createElement('div');
        let colDiv = document.createElement('div');
        let checkmark = document.createElement('input');
        let trashBtn = document.createElement('button');
        let img = document.createElement('img');
        let habit = document.createTextNode(habitText);
    
        checkmark.type = 'checkbox';
        checkmark.className = 'mr-2';
    
        colDiv.className = 'col';
    
        img.src = '/static/images/trash.svg';
        img.alt = 'failed';
    
        trashBtn.className = 'btn btn-secondary btn-sm mt-2 float-right';
        trashBtn.id = 'trashBtn';
        trashBtn.appendChild(img);
        trashBtn.addEventListener('click', (e) =>{
            e.preventDefault();
            habitHTML.remove();
        })
    
        habitHTML.className = 'input-group-text text-wrap text-left my-3 mx-1';
        habitHTML.appendChild(colDiv);
        
        colDiv.appendChild(checkmark);
        colDiv.appendChild(habit);
        colDiv.appendChild(trashBtn);
    
        habitListDisplay.appendChild(habitHTML);
    })
}
