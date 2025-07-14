const add_item = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');

add_item.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
