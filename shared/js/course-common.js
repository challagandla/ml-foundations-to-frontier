/* Shared behavior for every module page: theme toggle, deep-dive
   accordion polish, and quiz grading. Include after components.css. */
(function () {
  "use strict";

  function initThemeToggle() {
    var root = document.documentElement;
    var stored = null;
    try {
      stored = localStorage.getItem("ml-course-theme");
    } catch (error) {
      // Some browsers or privacy modes block local storage.
    }
    if (stored) root.setAttribute("data-theme", stored);

    var btn = document.querySelector("[data-theme-toggle]");
    if (!btn) return;
    var setLabel = function () {
      var mode = root.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      btn.textContent = mode === "dark" ? "Light mode" : "Dark mode";
    };
    setLabel();
    btn.addEventListener("click", function () {
      var current = root.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var next = current === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try {
        localStorage.setItem("ml-course-theme", next);
      } catch (error) {
        // The theme still changes for this page even when it cannot be saved.
      }
      setLabel();
    });
  }

  // Quiz: each .quiz__q has data-answer="<index>" on itself and
  // .quiz__option buttons in document order. Clicking grades instantly.
  function initQuizzes() {
    document.querySelectorAll(".quiz__q").forEach(function (q) {
      if (q.closest("[data-custom-quiz]")) return;
      var correctIdx = parseInt(q.getAttribute("data-answer"), 10);
      var options = Array.prototype.slice.call(q.querySelectorAll(".quiz__option"));
      var feedback = q.querySelector(".quiz__feedback");
      var answered = false;
      options.forEach(function (opt, idx) {
        opt.addEventListener("click", function () {
          if (answered) return;
          answered = true;
          options.forEach(function (o, i) {
            o.classList.add(i === correctIdx ? "is-correct" : (i === idx ? "is-incorrect" : ""));
          });
          if (feedback) {
            feedback.textContent = idx === correctIdx
              ? "Correct. " + (q.getAttribute("data-explain") || "")
              : "Not quite. " + (q.getAttribute("data-explain") || "");
          }
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initThemeToggle();
    initQuizzes();
  });
})();
