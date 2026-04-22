---
title: Code-Memo
---

<p>
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