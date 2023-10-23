let helloBtn = document.querySelector('button');
helloBtn.addEventListener('click', inputMsg);

function inputMsg(){
    // alert("WELCOME IN AMAZONE!");
    let name = prompt('Enter Name of Student');
    helloBtn.textContent = 'Roll No. 1: ' + name;

}