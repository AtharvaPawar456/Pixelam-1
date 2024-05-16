function toggleMenu() {
    let list = document.querySelector('#navbar-default');
    let closeBtn = document.querySelector('#closeBtn');
    let menuBtn = document.querySelector('#menuBtn');
  
    list.classList.toggle('hidden');
    closeBtn.classList.toggle('hidden');
    menuBtn.classList.toggle('hidden');
  }