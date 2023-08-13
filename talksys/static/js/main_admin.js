
// Variables
 
const chatRoom = document.querySelector('#room_uuid').textContent.replace('"','')

let chatSocket = null 

// Elements 

const chatLogElement = document.querySelector('#chat_log')
const chatInputElement = document.querySelector('#chat_message_input')
const chatSubmitlement = document.querySelector('#chat_message_submit')
 
// Setup the web socket 

chatSocket = new WebSocket(`ws://${window.location.host}/ws/${chatRoom}/`) 

// Adding an event listener

chatSocket.onmessage = function(e) {
    console.log('on message')
} 

chatSocket.onopen = function(e) {
    console.log('on open')
} 

chatSocket.onclose = function(e) {
    console.log('Sorry the chat socket closed unexpectedly ')
}