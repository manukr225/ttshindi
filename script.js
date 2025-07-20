let voices = [];

function loadVoices() {
  voices = speechSynthesis.getVoices();

  const voiceSelect = document.getElementById('voiceSelect');
  voiceSelect.innerHTML = '';

  voices.forEach((voice, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.text = `${voice.name} (${voice.lang})`;
    voiceSelect.appendChild(option);
  });
}

// Load voices automatically when available
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = loadVoices;
}

function speak() {
  const text = document.getElementById('textInput').value;
  const rate = document.getElementById('rateControl').value;
  const selectedIndex = document.getElementById('voiceSelect').value;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = voices[selectedIndex];
  utterance.rate = parseFloat(rate);
  speechSynthesis.speak(utterance);
}

function stop() {
  speechSynthesis.cancel();
}
