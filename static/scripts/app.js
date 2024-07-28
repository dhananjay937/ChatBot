document.addEventListener('DOMContentLoaded', () => {
  const msgerForm = get('.msger-inputarea');
  const msgerInput = get('.msger-input');
  const msgerChat = get('.msger-chat');

  const scriptTag = document.querySelector('script[data-bot-img]');
  const BOT_IMG = scriptTag.dataset.botImg;
  const PERSON_IMG = scriptTag.dataset.personImg;
  const BOT_NAME = "NeoBot";
  const PERSON_NAME = "You";

  msgerForm.addEventListener('submit', onFormSubmit);

  function onFormSubmit(event) {
    event.preventDefault();

    const msgText = msgerInput.value.trim();
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";
    botResponse(msgText);
  }

  function appendMessage(name, img, side, text) {
    const msgHTML = `
      <div class="msg ${side}-msg">
        <div class="msg-img" style="background-image: url(${img});" alt="${name} Avatar"></div>
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">${name}</div>
            <div class="msg-info-time">${formatDate(new Date())}</div>
          </div>
          <div class="msg-text">${text}</div>
        </div>
      </div>
    `;

    msgerChat.insertAdjacentHTML('beforeend', msgHTML);
    msgerChat.scrollTop += 500;
  }

  function botResponse(rawText) {
    $.get('/get', { msg: rawText })
      .done(data => {
        appendMessage(BOT_NAME, BOT_IMG, 'left', data);
      })
      .fail(() => {
        appendMessage(BOT_NAME, BOT_IMG, 'left', 'Sorry, I encountered an error. Please try again.');
      });
  }

  function get(selector, root = document) {
    return root.querySelector(selector);
  }

  function formatDate(date) {
    const h = `0${date.getHours()}`.slice(-2);
    const m = `0${date.getMinutes()}`.slice(-2);

    return `${h}:${m}`;
  }
});
