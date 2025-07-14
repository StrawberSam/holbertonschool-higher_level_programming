const header = document.querySelector('header');
const toogleHeader = document.querySelector('#toggle_header');

toogleHeader.addEventListener('click', () => {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
