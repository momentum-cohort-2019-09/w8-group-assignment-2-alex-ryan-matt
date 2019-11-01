// let prompt = document.querySelector('#id_prompt').value
// let description = document.querySelector('#id_description').value


console.log('i am working')


document.querySelector('#actual_thing_we_want').addEventListener('submit', function (event) {
  event.preventDefault()
  console.log('clicked')
  fetch('/api/1/artisanal_card_create', {
    method: "POST",
    body: JSON.stringify({ prompt: 'strang', description: 'iddescription', })
  })
    .then(response => { response.json() })
    .then(response => { console.log(response) })
})