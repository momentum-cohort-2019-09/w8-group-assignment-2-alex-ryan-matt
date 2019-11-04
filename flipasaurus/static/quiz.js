let deck = JSON.parse(document.getElementById('data').textContent)
let cards = []
let current_card_index = 0


let cardsCorrect = [];
let cardsIncorrect = [];

let stack = document.querySelector('.stack')
stack.addEventListener('click', function(){
    stack.classList.toggle('is-flipped')
    back.classList.toggle('hidden')
})

let front = document.querySelector('.prompt')
let back = document.querySelector('.description-text')

front.textContent = deck.cards[current_card_index].prompt
back.textContent = deck.cards[current_card_index].description
function flipCard(deck) {
    console.log(deck)
    front.textContent = deck.cards[current_card_index].prompt
    back.textContent = deck.cards[current_card_index].description

}

function correctCard() {
    deck.cards[current_card_index].correct_flips += 1
    cardsCorrect.push(deck.cards[current_card_index])
    current_card_index += 1;
    flipCard(deck)
    console.log(cardsCorrect, 'correct')
}

function incorrectCard() {
    deck.cards[current_card_index].incorrect_flips += 1
    cardsIncorrect.push(deck.cards[current_card_index])
    current_card_index += 1;
    flipCard(deck)
    console.log(cardsIncorrect, 'incorrect')
}

document.getElementById('correct').addEventListener('click', function(event) {
    event.preventDefault()
    correctCard()
})
document.getElementById('incorrect').addEventListener('click', function(event) {
    event.preventDefault()
    incorrectCard()
})

