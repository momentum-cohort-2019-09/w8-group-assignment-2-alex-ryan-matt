

console.log('i am working')


document.querySelector('#actual_thing_we_want').addEventListener('submit', function (event) {
  event.preventDefault()

  let prompt = document.querySelector('#id_prompt').value
  let description = document.querySelector('#id_description').value

  let deckId = document.querySelector('#actual_thing_we_want').dataset.deck_id


  console.log('clicked', prompt, description)

  fetch(`/api/deck/${deckId}/artisanal_card_create`, {
    method: "POST",
    body: JSON.stringify({ prompt: prompt, description: description })
  })
    .then(response => { return response.json() })
    .then(response => { console.log(response) })
})