// Minimal client-side form handling: submit via fetch, show status
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const status = document.getElementById('formStatus');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    status.textContent = 'Sending…';
    const data = new FormData(form);
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: data
      });
      const json = await res.json();
      if (json.success) {
        status.textContent = 'Message sent — thank you!';
        form.reset();
      } else {
        status.textContent = 'Could not send message. Try again later.';
      }
    } catch (err) {
      console.error(err);
      status.textContent = 'Network error. Try again later.';
    }

    setTimeout(() => {
      status.textContent = '';
    }, 5000);
  });
});
