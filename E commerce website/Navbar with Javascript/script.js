const menuBtn = document.querySelector('.menu');
const sidebar = document.querySelector('.sidebar');
//adding event listener menu//
menuBtn.addEventListener('click', ()=>{
    sidebar.classList.add('showSidebar');
});



//adding event lister to ducument//
document
.addEventListener('mouseup', (e)=>{
    if(!sidebar.contains(e.target)){
    sidebar.classList.remove('showSidebar');
    }
});

