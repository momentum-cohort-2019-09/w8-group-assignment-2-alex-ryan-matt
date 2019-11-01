let deck = JSON.parse(document.getElementById('data').textContent)
let cards = []
let current_card_index = 0


let cardsCorrect = [];
let cardsIncorrect = [];



function flipCard(deck) {
    console.log(deck)
    let card = document.getElementById('card');
    if (card.innerHTML === deck.cards[current_card_index].prompt) {
        card.innerHTML = deck.cards[current_card_index].description
    } else {
        card.innerHTML = deck.cards[current_card_index].prompt;
    }
    document.getElementById('button').classList.toggle("hidden")

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

document.getElementById('card').innerHTML = deck.cards[current_card_index].prompt