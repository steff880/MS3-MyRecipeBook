// jQuery

$(document).ready(function(){
    $('.sidenav').sidenav({ edge: "right" });
  });






// Vanilla JS

document.addEventListener('DOMContentLoaded', function() {

  let password = document.getElementById('password');
  let confirmPassword = document.getElementById('confirm_password');

  const checkIfPasswordsMatch = () => {
   
    let messageText = document.querySelector('.message-text');
    let regButton = document.querySelector('.btn-register');

    // Check if passwords match

    if (password.value !== confirmPassword.value) {
      messageText.innerHTML = 'Passwords do not match!';
      messageText.style.color = 'red';

      regButton.setAttribute('disabled', true);
      regButton.classList.add('btn-disabled');
    } else if( password.value === confirmPassword.value) {
      messageText.innerHTML = 'Passwords match!';
      messageText.style.color = 'green';
      regButton.removeAttribute('disabled', true);
      regButton.classList.remove('btn-disabled');
    }
  }

  // Event Listeners

  [password, confirmPassword].forEach(item => {
    item.addEventListener('keyup', checkIfPasswordsMatch);
  })
  
})