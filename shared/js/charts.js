/* Minimal chart/geometry helpers shared across module demos. No
   external charting library is used (keeps every module a single
   portable file) -- modules build inline <svg> and use these small
   utilities for scales, axes, and coordinate-grid math. */
(function (global) {
  "use strict";

  function scaleLinear(domain, range) {
    var d0 = domain[0], d1 = domain[1], r0 = range[0], r1 = range[1];
    var m = (r1 - r0) / (d1 - d0);
    var fn = function (v) { return r0 + (v - d0) * m; };
    fn.invert = function (v) { return d0 + (v - r0) / m; };
    return fn;
  }

  // Builds an SVG path `d` string for a polyline through [x,y] points
  // already in screen space.
  function linePath(points) {
    return points.map(function (p, i) {
      return (i === 0 ? "M" : "L") + p[0].toFixed(2) + "," + p[1].toFixed(2);
    }).join(" ");
  }

  // Draws a simple centered cartesian grid (axes through the origin,
  // faint gridlines) into an existing <svg> element. Returns the x/y
  // scale functions so callers can plot points/vectors on top.
  function cartesianGrid(svg, opts) {
    opts = opts || {};
    var w = opts.width || svg.viewBox.baseVal.width || 400;
    var h = opts.height || svg.viewBox.baseVal.height || 400;
    var domain = opts.domain || [-5, 5];
    var pad = opts.pad || 24;

    var x = scaleLinear(domain, [pad, w - pad]);
    var y = scaleLinear(domain, [h - pad, pad]); // flip y

    var ns = "http://www.w3.org/2000/svg";
    var grid = document.createElementNS(ns, "g");
    grid.setAttribute("class", "chart-grid");

    var gridColor = getComputedStyle(document.documentElement).getPropertyValue("--gridline").trim() || "#e1e0d9";
    var baseColor = getComputedStyle(document.documentElement).getPropertyValue("--baseline").trim() || "#c3c2b7";

    for (var t = Math.ceil(domain[0]); t <= Math.floor(domain[1]); t++) {
      if (t === 0) continue;
      var vLine = document.createElementNS(ns, "line");
      vLine.setAttribute("x1", x(t)); vLine.setAttribute("x2", x(t));
      vLine.setAttribute("y1", y(domain[0])); vLine.setAttribute("y2", y(domain[1]));
      vLine.setAttribute("stroke", gridColor); vLine.setAttribute("stroke-width", "1");
      grid.appendChild(vLine);

      var hLine = document.createElementNS(ns, "line");
      hLine.setAttribute("y1", y(t)); hLine.setAttribute("y2", y(t));
      hLine.setAttribute("x1", x(domain[0])); hLine.setAttribute("x2", x(domain[1]));
      hLine.setAttribute("stroke", gridColor); hLine.setAttribute("stroke-width", "1");
      grid.appendChild(hLine);
    }

    var xAxis = document.createElementNS(ns, "line");
    xAxis.setAttribute("x1", x(domain[0])); xAxis.setAttribute("x2", x(domain[1]));
    xAxis.setAttribute("y1", y(0)); xAxis.setAttribute("y2", y(0));
    xAxis.setAttribute("stroke", baseColor); xAxis.setAttribute("stroke-width", "1.5");
    grid.appendChild(xAxis);

    var yAxis = document.createElementNS(ns, "line");
    yAxis.setAttribute("y1", y(domain[0])); yAxis.setAttribute("y2", y(domain[1]));
    yAxis.setAttribute("x1", x(0)); yAxis.setAttribute("x2", x(0));
    yAxis.setAttribute("stroke", baseColor); yAxis.setAttribute("stroke-width", "1.5");
    grid.appendChild(yAxis);

    svg.appendChild(grid);
    return { x: x, y: y };
  }

  // Draws an arrow (vector) from the origin (or `from`) to `to`, in
  // domain units, using the scales returned by cartesianGrid.
  function drawVector(svg, scales, to, opts) {
    opts = opts || {};
    var from = opts.from || [0, 0];
    var ns = "http://www.w3.org/2000/svg";
    var color = opts.color || "var(--phase-0)";
    var id = opts.markerId || ("arrow-" + Math.random().toString(36).slice(2));

    var defs = svg.querySelector("defs") || svg.insertBefore(document.createElementNS(ns, "defs"), svg.firstChild);
    var marker = document.createElementNS(ns, "marker");
    marker.setAttribute("id", id);
    marker.setAttribute("markerWidth", "8");
    marker.setAttribute("markerHeight", "8");
    marker.setAttribute("refX", "6");
    marker.setAttribute("refY", "3");
    marker.setAttribute("orient", "auto");
    var arrowPath = document.createElementNS(ns, "path");
    arrowPath.setAttribute("d", "M0,0 L0,6 L7,3 z");
    arrowPath.setAttribute("fill", color);
    marker.appendChild(arrowPath);
    defs.appendChild(marker);

    var line = document.createElementNS(ns, "line");
    line.setAttribute("x1", scales.x(from[0]));
    line.setAttribute("y1", scales.y(from[1]));
    line.setAttribute("x2", scales.x(to[0]));
    line.setAttribute("y2", scales.y(to[1]));
    line.setAttribute("stroke", color);
    line.setAttribute("stroke-width", opts.width || 2.5);
    line.setAttribute("marker-end", "url(#" + id + ")");
    svg.appendChild(line);
    return line;
  }

  global.CourseCharts = {
    scaleLinear: scaleLinear,
    linePath: linePath,
    cartesianGrid: cartesianGrid,
    drawVector: drawVector
  };
})(window);
