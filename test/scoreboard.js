const cursor = document.querySelector('.custom-cursor');

document.addEventListener('mousemove', (e) => {
  // Nutzt clientX und clientY für die exakte Position im Browserfenster
  cursor.style.left = `${e.clientX}px`;
  cursor.style.top = `${e.clientY}px`;
});
