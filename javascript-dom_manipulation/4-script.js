document.querySelector('#add_item').addEventListener('click', () => {
    const newElement = document.createElement('li');
    newElement.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newElement);
  });