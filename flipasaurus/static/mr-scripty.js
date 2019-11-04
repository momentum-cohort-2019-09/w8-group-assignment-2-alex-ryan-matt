

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


  const div = document.querySelector('.cards_wrapper');
  // div.innerHTML = '';
  div.innerHTML += `
  <button class="edit" type="button">Edit</button>

  <p class="cardPrompt" data-prompt="${prompt}">${prompt}</p>

  <p class= "cardDescription" data-description="${description}" > ${description}</p>

    <button class="delete" type="button">Delete</button>
  </div >
      `;


  document.querySelector('#actual_thing_we_want').reset()

  console.log("i'm done!")

})