async function sendForm() {
  const name = document.getElementById('f-name').value.trim();
  const email = document.getElementById('f-email').value.trim();
  const message = document.getElementById('f-message').value.trim();
  const status = document.getElementById('form-status');

  if (!name || !email || !message) {
    status.textContent = '// заполните все поля';
    status.style.color = '#ff6b6b';
    return;
  }

  status.textContent = '// отправка...';
  status.style.color = '#666';

  try {
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, message })
    });
    const result = await response.json();

    if (response.ok) {
      status.textContent = '// сообщение отправлено, скоро отвечу!';
      status.style.color = '#e8ff47';
      document.getElementById('f-name').value = '';
      document.getElementById('f-email').value = '';
      document.getElementById('f-message').value = '';
    } else {
      status.textContent = '// ошибка: ' + (result.detail || 'попробуйте ещё раз');
      status.style.color = '#ff6b6b';
    }
  } catch (e) {
    status.textContent = '// ошибка соединения';
    status.style.color = '#ff6b6b';
  }
}
