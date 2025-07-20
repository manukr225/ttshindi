function speak() {
  const text = document.getElementById('textInput').value;
  const rate = document.getElementById('rateControl').value;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'hi-IN';
  utterance.rate = parseFloat(rate);
  speechSynthesis.speak(utterance);
}

function stop() {
  speechSynthesis.cancel();
}
