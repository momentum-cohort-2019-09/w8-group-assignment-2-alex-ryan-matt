let deck = JSON.parse(document.getElementById('data').textContent)
let cards = []


let cardsCorrect = [];
let cardsIncorrect = [];

function flipCard(deck) {
    console.log(deck)
    let card = document.getElementById('card');
    if (card.innerHTML === deck.cards[0].prompt) {
        card.innerHTML = deck.cards[0].description
    } else {
        card.innerHTML = deck.cards[0].prompt;
    }
    document.getElementById('button').classList.toggle("hidden")
    correctCard();
    incorrectCard();
}

function correctCard() {
    document.getElementById('correct').addEventListener('click', function(event) {
        event.preventDefault()

        deck.cards[0].correct_flips += 1
        cardsCorrect.push(deck.cards[0])
        console.log(cardsCorrect, 'correct')
    })
}

function incorrectCard() {
    document.getElementById('incorrect').addEventListener('click', function(event) {
        event.preventDefault()

        deck.cards[0].incorrect_flips += 1
        cardsIncorrect.push(deck.cards[0])
        console.log(cardsIncorrect, 'incorrect')
    })
}

document.getElementById('card').innerHTML = deck.cards[0].prompt