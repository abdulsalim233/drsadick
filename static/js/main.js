/* Main Client JavaScript */
document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle (Dark / Light Mode)
  const themeToggleBtn = document.getElementById('theme-toggle');
  const htmlElement = document.documentElement;

  // Load saved theme preference
  const savedTheme = localStorage.getItem('site-theme') || 'dark';
  htmlElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('site-theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }

  function updateThemeIcon(theme) {
    if (!themeToggleBtn) return;
    if (theme === 'light') {
      themeToggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
      themeToggleBtn.setAttribute('title', 'Switch to Dark Mode');
    } else {
      themeToggleBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
      themeToggleBtn.setAttribute('title', 'Switch to Light Mode');
    }
  }

  // Mobile Navigation Toggle
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const navLinks = document.getElementById('nav-links-menu');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = navLinks.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', isExpanded);
    });

    // Automatically close mobile menu when a navigation link is clicked
    navLinks.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // AJAX Contact Form Submission
  const contactForm = document.getElementById('contact-form');
  const formFeedback = document.getElementById('form-feedback');

  if (contactForm && formFeedback) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalBtnText = submitBtn.innerHTML;

      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending Message...';
      formFeedback.style.display = 'none';

      const formData = new FormData(contactForm);

      try {
        const response = await fetch(contactForm.action, {
          method: 'POST',
          body: formData,
          headers: {
            'X-Requested-With': 'XMLHttpRequest'
          }
        });

        const data = await response.json();

        if (response.ok && data.success) {
          formFeedback.className = 'form-feedback-alert success';
          formFeedback.innerHTML = `<strong>Success!</strong> ${data.message}`;
          formFeedback.style.display = 'block';
          contactForm.reset();
        } else {
          formFeedback.className = 'form-feedback-alert error';
          formFeedback.innerHTML = `<strong>Error:</strong> ${data.error || 'Failed to send message.'}`;
          formFeedback.style.display = 'block';
        }
      } catch (err) {
        formFeedback.className = 'form-feedback-alert error';
        formFeedback.innerHTML = '<strong>Error:</strong> An unexpected network error occurred. Please try again.';
        formFeedback.style.display = 'block';
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnText;
      }
    });
  }
});

// Copy Citation Helper Function
function copyCitation(title, authors, year, journal) {
  const citationText = `${authors} (${year}). "${title}". ${journal}.`;
  navigator.clipboard.writeText(citationText).then(() => {
    alert('Citation copied to clipboard:\n\n' + citationText);
  }).catch(err => {
    console.error('Copy failed', err);
  });
}
