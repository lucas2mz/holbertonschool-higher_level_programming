document.querySelector('#toggle_header').addEventListener('click', () => {
    const HtmlHeader = document.querySelector('header');
    if (HtmlHeader.classList.contains('red')) {
      HtmlHeader.classList.remove('red');
      HtmlHeader.classList.add('green');
    } else {
      HtmlHeader.classList.remove('green');
      HtmlHeader.classList.add('red');
    }
  });