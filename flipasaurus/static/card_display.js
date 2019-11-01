let deck = JSON.parse(document.getElementById('data').textContent)
let cards = []
let currentIndex = 0
let container = document.querySelector('.test-div')

function listCards(deck) {
  for(let card of deck.cards){
    cards.push(card)
  }
  console.log(cards)
}



function render(card){
  container.innerHTML = `
  
  `
}