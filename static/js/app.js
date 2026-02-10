(function () {
  const path = window.location.pathname || "/";
  document.querySelectorAll(".sidebar a.nav-item").forEach((a) => {
    const href = a.getAttribute("href");
    if (!href) return;
    if (href === path) a.classList.add("active");
  });

  const healthEl = document.querySelector("[data-health]");
  if (healthEl) {
    fetch("/health")
      .then((r) => r.json())
      .then((j) => (healthEl.textContent = j.ok ? "Health: OK" : "Health: FAIL"))
      .catch(() => (healthEl.textContent = "Health: ?"));
  }
})();