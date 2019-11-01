

function post_card() {
  console.log('post_card')
  // let prompt = form.get('prompt');
  // let description = form.get('description');
  fetch('api/card', {

    method: 'POST',
    body: JSON.stringify({
      prompt: 'whatever', description: 'im tired', owner: 'alex_is_cool', deck: 'http://127.0.0.1:8000/api/deck/1/'
    }),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
  })
    .then(console.log('fetching!'))
    .then(response => response.json())
  console.log(response.json())

}

function createCardButton() {
  let createButton = document.querySelector('.create_button_foreal');
  createButton.addEventListener('click', function (event) {
    event.preventDefault();
    post_card()
  })

}

createCardButton()