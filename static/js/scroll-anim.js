/* Modern Hardware-Accelerated Scroll Animation Script */
document.addEventListener('DOMContentLoaded', () => {
  // Check user prefers-reduced-motion setting
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return;

  const animateElements = document.querySelectorAll('.animate-on-scroll');

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.15
  };

  const scrollObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        // Unobserve after animating once to save memory & performance
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animateElements.forEach((el, index) => {
    // Add subtle staggered delay for grid items
    if (el.classList.contains('stagger-item')) {
      const delay = (index % 4) * 0.12;
      el.style.transitionDelay = `${delay}s`;
    }
    scrollObserver.observe(el);
  });
});
