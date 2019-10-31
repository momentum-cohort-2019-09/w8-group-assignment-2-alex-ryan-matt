let deleteButtons = [...document.querySelectorAll(".deck-delete")]
for (let button of deleteButtons){
  button.addEventListener('click', (event)=>{
    console.log('click')
  })
}
