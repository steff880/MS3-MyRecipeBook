// jQuery

$(document).ready(function () {
  $('.sidenav').sidenav({
    edge: "right"
  });

  $('select').formSelect();
});






// Vanilla JS

// When the user tries to register, check if passwords match

const checkIfPasswordsMatch = () => {
  let password = document.getElementById('password');
  let confirmPassword = document.getElementById('confirm_password');

  let messageText = document.querySelector('.message-text');
  let regButton = document.querySelector('.btn-register');

  // Check if passwords match

  if (password.value !== confirmPassword.value) {
    messageText.innerHTML = 'Passwords do not match!';
    messageText.style.color = 'red';

    regButton.setAttribute('disabled', true);
    regButton.classList.add('btn-disabled');
  } else if (password.value === confirmPassword.value) {
    messageText.innerHTML = 'Passwords match!';
    messageText.style.color = 'green';
    
    regButton.removeAttribute('disabled', true);
    regButton.classList.remove('btn-disabled');
  }
}

