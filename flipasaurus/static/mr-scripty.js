let prompt = document.querySelector('#id_prompt').value
let description = document.querySelector('#id_description').value


console.log('i am working')


document.getElementById('actual_thing_we_want').addEventListener('submit', function (event) {
  event.preventDefault()
  console.log('clicked')
  fetch('/api/deck/{{pk}}/artisanal_card_create', {
    method: "POST",
    body: JSON.stringify({ prompt: prompt, description: description })
  })
    .then(response => { response.json() })
    .then(response => { console.log(response) })
})