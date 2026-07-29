/* Progress tracking, backed by localStorage (no server). Shared by
   every module page (the "mark complete" button) and index.html
   (the dashboard that reads statuses back). Storage is per-browser-
   origin, so progress made by opening files locally will not be
   visible from a published Artifact copy of the same page, and
   vice versa -- see README "How progress tracking works". */
(function (global) {
  "use strict";

  var KEY = "ml-course-progress-v1";

  function readAll() {
    try {
      return JSON.parse(localStorage.getItem(KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function writeAll(map) {
    localStorage.setItem(KEY, JSON.stringify(map));
  }

  var CourseProgress = {
    STATUS: { NOT_STARTED: "not-started", IN_PROGRESS: "in-progress", DONE: "done" },

    get: function (moduleNum) {
      var map = readAll();
      return map[moduleNum] || CourseProgress.STATUS.NOT_STARTED;
    },

    set: function (moduleNum, status) {
      var map = readAll();
      map[moduleNum] = status;
      writeAll(map);
    },

    all: readAll,

    // Wires up a "mark complete" button on a module page, if present.
    initModuleButton: function (moduleNum) {
      var btn = document.querySelector("[data-mark-done]");
      if (!btn) return;
      var render = function () {
        var status = CourseProgress.get(moduleNum);
        btn.textContent = status === CourseProgress.STATUS.DONE
          ? "Completed ✓" : "Mark module complete";
        btn.classList.toggle("btn--mark-done", status === CourseProgress.STATUS.DONE);
      };
      btn.addEventListener("click", function () {
        var next = CourseProgress.get(moduleNum) === CourseProgress.STATUS.DONE
          ? CourseProgress.STATUS.IN_PROGRESS : CourseProgress.STATUS.DONE;
        CourseProgress.set(moduleNum, next);
        render();
      });
      render();
    }
  };

  global.CourseProgress = CourseProgress;
})(window);
