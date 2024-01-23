const roomName = JSON.parse(document.getElementById('room-name').textContent);

const cws_protocol = (window.location.protocol === 'https:') ? 'cws://' : 'ws://';

const chatSocket = new WebSocket(
    cws_protocol + window.location.host + '/ws/chat' + roomName + '/'
);

chatSocket.onopen = function (e) {
    document.querySelector('chat-log').value += ('[����] ��ӭ�������������������ƽ�������������������\n');
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringfy({
        'message': message
    }));
    messageInputDom.value = '';
}