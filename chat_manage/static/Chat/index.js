document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function (e) {
    if (e, keyCode === 13) {
        document.querySelector('#room-name-submit').click();
    }
};
document.querySelector('#room-name-submit').onclik = function (e) {
    var roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/chat/' + roomName + '/';
};