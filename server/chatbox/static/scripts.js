function create_user_message(message){
  new_message_row = document.createElement("div");
  new_message_row.className = "row p-3 justify-content-end";

  new_message_col = document.createElement("div");
  new_message_col.className = "col-8 p-3 shadow rounded bg-white";
  new_message_col.innerHTML = message;

  new_message_row.appendChild(new_message_col);

  return new_message_row;
}

function create_bot_message(message){
  new_message_row = document.createElement("div");
  new_message_row.className = "row p-3 justify-content-start";

  new_message_col = document.createElement("div");
  new_message_col.className = "col-8 p-3 shadow rounded bg-light";
  new_message_col.innerHTML = message;

  new_message_row.appendChild(new_message_col);

  return new_message_row;
}

function create_bot_placeholder(){
  new_message_row = document.createElement("div");
  new_message_row.className = "row p-3 justify-content-start";

  new_message_col = document.createElement("div");
  new_message_col.className = "col-1 p-3 shadow rounded bg-light";
  
  new_message_spinner = document.createElement("div");
  new_message_spinner.className = "spinner-border text-success";

  new_message_col.appendChild(new_message_spinner);
  new_message_row.appendChild(new_message_col);

  return new_message_row;
}

// Django provided function to get security token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

async function chat_button_onclick(){
  // Getting chat field and value
  chat_input = document.getElementById("chat-message-input");
  text_input = chat_input.value;

  if (text_input.length == 0){
    return;
  }

  // Resetting and disabling input till output comes
  chat_input.value = null;
  chat_input.placeholder = 'Write your message here.';
  chat_input.disabled = true;

  // Get chat area
  chat_log = document.getElementById("chat-log");

  // Input users message and bots loading placeholder
  chat_log.appendChild(create_user_message(text_input));

  placeholder = create_bot_placeholder() //Holding for later
  chat_log.appendChild(placeholder)

  // Get message from ollama
  // TODO
  var url = '/chat/generate_response';

  fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({"query": text_input})
  })
  .then(response => response.json())
  .then(data => {
    // Replace loader with message
    placeholder.children[0].className = "col-8 p-3 shadow rounded bg-light";
    placeholder.children[0].innerHTML = data['response'];
  });

  
  // Release text input to user
  chat_input.disabled = false;
}