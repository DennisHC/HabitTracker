let tasksListDisplay = document.querySelector('#tasklist');
let habitListDisplay = document.querySelector('#habitlist');

//Get Tasks from Server and populate them
fetch('/api/getTasks/1')
.then(res => res.json())
.then(data => {
    populateTasks(data);
    console.log(data);
})
.catch(err => console.log(err));

//Updating Task Code (MOVE)
fetch('/api/updateTask/10/', {
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({
        difficulty_level: 3,
        task_name: "Very Long Task Testing aojshd aisdh aiuwhd ashbdf ihwedf aiusgd aibd ashbd ajhwbd ajwbd awhdbaksjdbnaklsjbdakls dbkalbsd jalkshbdajhsbd ajkshdb ajskdajhsbd ajshbd als dauwh d"
    })
})
.then(res => {}/*window.location.replace(window.location.href)*/)
.then(data => {})
.catch(err => console.log(err));

//Get Habits from Server and populate them
/*fetch('/api/getHabits/1')
.then(res => res.json())
.then(data => populateHabits(data.habits))
.catch(err => console.log(err));*/

//Aux Functions that get called above
function populateTasks(taskList){
    taskList.forEach(taskObject => {
        let taskText = taskObject.task_name;
        let taskHTML = document.createElement('div');
        let row = document.createElement('div');
        let checkmark = document.createElement('input');
        let trashBtn = document.createElement('button');
        let completeBtn = document.createElement('button');
        let editBtn = document.createElement('button');
        let img = document.createElement('img');
        let img2 = document.createElement('img');
        let task = document.createElement('div');
        let difficultyIcon = document.createElement('span');
        let separator = document.createElement('hr');

        separator.className = 'mb-2 mt-3';

        row.className = 'row';

        difficultyIcon.className = 'ml-4 mr-5 px-2';
        difficultyIcon.style = 'background-color: CornflowerBlue; height: 25px; border-radius: 10px;';
        difficultyIcon.innerHTML = 'Difficulty: ' + taskObject.difficulty_level;
    
        checkmark.type = 'checkbox';
        checkmark.className = 'mr-2 col-1';

        task.innerHTML = taskText;
        task.className = 'my-2 col-auto mr-auto';
    
        img.src = '/static/images/trash.svg';
        img.alt = 'image loading failed';

        img2.src = '/static/images/edit.svg';
        img2.alt = 'image loading failed';

        //add event listener
        editBtn.className = 'btn btn-secondary btn-sm mb-2 ml-5 shadow';
        editBtn.appendChild(img2);

        //add event listener
        completeBtn.className = 'btn btn-secondary btn-sm shadow ml-5 mr-4 mb-2 font-weight-bold';
        completeBtn.style = 'color: black;';
        completeBtn.innerHTML = 'Completed';
    
        trashBtn.className = 'btn btn-secondary btn-sm shadow ml-auto mr-4 mb-2';
        trashBtn.appendChild(img);
        trashBtn.addEventListener('click', (e) =>{
            e.preventDefault();

            //POST Delete Task
            /*fetch('/api/deleteTask/' + taskObject.id + '/', {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "POST"
            })
            .then(res => window.location.replace(window.location.href))//Refresh Page
            .then(data => {})
            .catch(err => console.log(err));*/
        })
    
        taskHTML.className = 'shadow my-3 mx-1';
        taskHTML.style = 'background-color:rgba(233,236,239); border: 1px solid rgb(206,212,218); border-radius: 10px;';
        taskHTML.appendChild(task);
        taskHTML.appendChild(separator);
        taskHTML.appendChild(row);
        
        row.appendChild(difficultyIcon);
        row.appendChild(completeBtn);
        row.appendChild(editBtn);
        row.appendChild(trashBtn);
    
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
