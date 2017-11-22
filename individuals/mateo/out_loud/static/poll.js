﻿var request = window.superagent;
var voice;

function setup() {
    noCanvas();
    voice = new p5.Speech(0, setRandomVoice);
}

function setRandomVoice() {
    let nVoices = window.speechSynthesis.getVoices().length;
    let n = Math.floor(Math.random() * nVoices)
    this.setVoice(n);
}

function getOptions(callback) {
    request.get('/api/poll/')
        .end((err, res) => {
            console.log(res.body);
            let button1 = document.getElementById("choice-1");
            let button2 = document.getElementById("choice-2");

            button1.word = res.body[0];
            button2.word = res.body[1];

            button1.innerText = button1.word;
            button2.innerText = button2.word;

            if (callback) {
                callback(button1, button2);
            }
        });
}

function sendVote(i) {
    let button = document.getElementById('choice-' + (i + 1));
    if (!button) {
        console.error('NO BUTTON OOP');
        return;
    }

    voice.speak(button.word);

    request.post('/api/poll/')
        .type('form')
        .send({ word: button.word })
        .send({ index: i })
        .end(getOptions);
}

document.addEventListener('DOMContentLoaded', () => {
    getOptions((b1, b2) => {
        b1.addEventListener('click', () => { sendVote(0); });
        b2.addEventListener('click', () => { sendVote(1); });

        //b1.addEventListener('touchstart', () => { sendVote(0); });
        //b2.addEventListener('touchstart', () => { sendVote(1); });
    })
}, false);

