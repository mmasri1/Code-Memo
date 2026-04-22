---
title: Code-Memo
---

<p id="random-page-cta" style="display:none;">
  <a href="#" onclick="randomPage(); return false;" style="text-decoration:none;">
    <button style="padding:10px 15px; font-size:14px; color:white; background-color:#007BFF; border:none; border-radius:5px; cursor:pointer;">
      Take Me to a Random Page &nbsp; 🎲
    </button>
  </a>
</p>

<script>
  async function randomPage() {
    try {
      const response = await fetch('pages.json');
      const data = await response.json();

      if (data.pages.length > 0) {
        let randomPage = data.pages[Math.floor(Math.random() * data.pages.length)];
        randomPage = randomPage.replace(/\.md$/, '');
        window.location.href = randomPage;
      } else {
        console.error("No pages found");
      }
    } catch (error) {
      console.error("Error fetching pages:", error);
    }
  }
</script>

<br>

{% include_relative README.md %}

<script>
  (function moveRandomButtonAboveNote() {
    const cta = document.getElementById("random-page-cta");
    if (!cta) return;

    const paragraphs = Array.from(document.querySelectorAll("p"));
    const note = paragraphs.find((p) =>
      (p.textContent || "").trim().startsWith("Note: This project")
    );

    if (note && note.parentNode) {
      cta.style.display = "";
      note.parentNode.insertBefore(cta, note);
    } else {
      // Fallback: show it at the top if note paragraph isn't found
      cta.style.display = "";
    }
  })();
</script>