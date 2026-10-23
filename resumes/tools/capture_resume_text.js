// Copy an online resume (Wanted, Saramin, JobKorea) as plain text for check_resume_text.py.
// Read-only: it reads the open page and changes nothing. How to run it: resumes/tools/README.md.
//
// It returns a one-line summary and leaves the text in window.__resumeChunks, in pieces under
// 900 characters, because the Chrome extension's JavaScript tool cuts its output near 1,000.
// To capture another part of the page, set window.__resumeRoot to a CSS selector first.
//
// What it keeps, in page order, one visual row per line:
// - visible text, with section titles (large bold text or headings) on their own "## " line;
// - the values of inputs, textareas, and selects: the Wanted editor keeps company names, titles,
//   and descriptions in fields, which page text leaves out;
// - the chosen value of each custom dropdown. Wanted marks an empty dropdown with
//   data-placeholder="true" and draws chosen values in dark text and placeholders in grey, so
//   faint text (an empty "YYYY.MM") and unticked checkboxes with their labels are dropped.
// Email addresses and phone numbers become [email] and [phone], so a saved copy never holds them.
(() => {
  const root = document.querySelector(window.__resumeRoot || '[class*="ResumeDetail_ResumeDetail__wrapper"]')
    || document.querySelector('main') || document.body;
  const redact = (s) => s
    .replace(/[\w.+-]+@[\w-]+(?:\.[\w-]+)+/g, '[email]')
    .replace(/(?:\+?82[\s.()-]*0?|\b0)1[016789][\s.()-]*\d{3,4}[\s.()-]*\d{4}/g, '[phone]')
    .replace(/\+\d{1,3}(?:[\s.()-]*\d{2,4}){3,4}/g, '[phone]')
    .replace(/(https?:\/\/[^\s?#]+)[?#]\S*/g, '$1');  // the JS tool blocks key=value-like output

  const unticked = new Set();
  root.querySelectorAll('input[type="checkbox"], input[type="radio"], [role="checkbox"], [role="radio"], [role="switch"]')
    .forEach((box) => {
      const ticked = box.matches('input') ? box.checked : box.getAttribute('aria-checked') === 'true';
      if (ticked) return;
      unticked.add(box);
      // Wanted wraps its "신입" checkbox and label in one button, so a short parent is the label.
      [...(box.labels || []), box.closest('label'), box.parentElement].forEach((label) => {
        if (label && label !== root && label.textContent.trim().length < 30) unticked.add(label);
      });
    });

  const SKIP_TAGS = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'svg']);
  const FIELD_TYPES = new Set(['text', 'search', 'url', 'number', 'date', 'month']);  // never tel or email
  const faint = (el) => {
    const alpha = getComputedStyle(el).color.match(/rgba\([^)]*,\s*([\d.]+)\)/);
    return alpha !== null && Number(alpha[1]) < 0.5;
  };
  const isHeading = (el) => {
    const style = getComputedStyle(el);
    return el.closest('h1, h2, h3, h4, h5, h6, [role="heading"]') !== null
      || (parseFloat(style.fontSize) >= 18 && Number(style.fontWeight) >= 600);
  };

  const pieces = [];
  const add = (text, box, kind) => {
    text = redact(text.replace(/\s+/g, ' ').trim());
    if (text) pieces.push({ text, box, kind });
  };
  const walk = (node) => {
    if (node.nodeType === Node.TEXT_NODE) {
      const el = node.parentElement;
      if (node.textContent.trim() && !faint(el)) {
        const range = document.createRange();
        range.selectNodeContents(node);
        add(node.textContent, range.getBoundingClientRect(), isHeading(el) ? 'heading' : 'text');
      }
      return;
    }
    if (node.nodeType !== Node.ELEMENT_NODE || SKIP_TAGS.has(node.tagName) || unticked.has(node)) return;
    if (node.dataset && node.dataset.placeholder === 'true') return;
    if (node.checkVisibility && !node.checkVisibility({ visibilityProperty: true })) return;
    if (node.tagName === 'INPUT') {
      if (FIELD_TYPES.has(node.type)) add(node.value, node.getBoundingClientRect(), 'field');
      return;
    }
    if (node.tagName === 'TEXTAREA') {
      node.value.split('\n').forEach((line) => add(line, null, 'block'));
      return;
    }
    if (node.tagName === 'SELECT') {
      if (node.value) add(node.selectedOptions[0].text, node.getBoundingClientRect(), 'field');
      return;
    }
    node.childNodes.forEach(walk);
  };
  walk(root);

  // Pieces side by side on screen (a date range, a row of dropdowns) share one line.
  const lines = [];
  let last = null;
  const inline = (piece) => piece && piece.kind !== 'block' && piece.kind !== 'heading';
  for (const piece of pieces) {
    const sameRow = inline(piece) && inline(last)
      && piece.box.top < last.box.bottom - 2 && last.box.top < piece.box.bottom - 2
      && piece.box.left >= last.box.right - 4;
    if (sameRow) lines[lines.length - 1] += ' ' + piece.text;
    else lines.push(piece.kind === 'heading' ? '## ' + piece.text : piece.text);
    last = piece;
  }

  const MAX = 900;
  const parts = lines.flatMap((line) => {
    const out = [];
    while (line.length > MAX) {
      let cut = line.lastIndexOf(' ', MAX);
      if (cut < MAX / 2) cut = MAX;
      out.push(line.slice(0, cut));
      line = line.slice(cut).trim();
    }
    return [...out, line];
  });
  const chunks = [];
  for (const part of parts) {
    if (chunks.length && chunks[chunks.length - 1].length + 1 + part.length <= MAX) {
      chunks[chunks.length - 1] += '\n' + part;
    } else {
      chunks.push(part);
    }
  }
  window.__resumeText = parts.join('\n');
  window.__resumeChunks = chunks;
  // FNV-1a of the UTF-8 bytes. check_resume_text.py prints the same fingerprint for the saved
  // file, so a slip in copying the chunks (such as a "Rex" corrected on the way) shows.
  let hash = 0x811c9dc5;
  for (const byte of new TextEncoder().encode(window.__resumeText)) {
    hash = Math.imul(hash ^ byte, 0x01000193) >>> 0;
  }
  return `${parts.length} lines, ${window.__resumeText.length} characters, fingerprint `
    + `${hash.toString(16).padStart(8, '0')}, ${chunks.length} chunks: `
    + `read window.__resumeChunks[0] to [${chunks.length - 1}] and join them with newlines`;
})();
