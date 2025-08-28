import reflex as rx
from typing import TypedDict


class Article(TypedDict):
    id: str
    title: str
    date: str
    content: str

a1 = """  <article>
    <p>At Simptech, innovation never stops. Beyond our current product lines, we are investing in <strong>smart accessories</strong>, <strong>modular upgrades</strong>, and a <strong>dedicated mobile app</strong> that brings every feature to your fingertips — from real-time GPS tracking to remote locking.</p>
    
    <p>Our future roadmap focuses on:</p>
    <ul>
      <li><strong>App-enabled travel management</strong> with personalized packing checklists.</li>
      <li><strong>Upgradable smart modules</strong>, allowing customers to keep their bags future-proof.</li>
      <li><strong>Sustainable materials</strong> that balance durability with environmental responsibility.</li>
    </ul>
    
    <p>We believe the future of mobility lies in <em>seamless integration between technology and human experience</em>. With Simptech, you’re not just buying a bag — you’re embracing a smarter way of moving through the world.</p>
  </article>"""

a2 = """  <article>
    <p>As commuting and business travel evolve, so do the needs of professionals. Simptech is excited to expand beyond luggage into <strong>Smart Backpacks</strong>, <strong>Commuter Bags</strong>, and <strong>Modular Multi-Functional Bags</strong>.</p>
    
    <p>Our Smart Backpacks come with <strong>integrated charging systems</strong>, <strong>cable management</strong>, <strong>RFID-blocking pockets</strong>, and <strong>anti-theft locks</strong>, all crafted from water-resistant <em>Codura fabric</em>. For those who demand flexibility, our Modular Bags feature <strong>magnetic quick-release buckles</strong>, <strong>detachable compartments</strong>, and <strong>customizable dividers</strong> — a single bag that adapts to business meetings, weekend getaways, or leisure travel.</p>
    
    <p>This expansion reflects our vision: to empower every journey, whether across the globe or across the city, with <em>intelligent simplicity</em>.</p>
  </article>"""

a3 = """<head>
  <meta charset="UTF-8">
  <style>
    body {font-family: Arial, Helvetica, sans-serif; line-height: 1.6; margin: 40px; background-color: #f9f9f9; color: #333;}
    article {max-width: 800px; margin: auto; background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
    h2 {color: #222; margin-bottom: 20px;}
    p {margin-bottom: 15px;}
    ul {margin: 15px 0; padding-left: 20px;}
    li {margin-bottom: 8px;}
    strong {color: #000;}
  </style>
</head>
<body>
  <article>
    <p>We are proud to unveil our flagship line: <strong>Simptech Smart Luggage</strong>. Designed for frequent flyers and global explorers, this suitcase integrates the essential tools every traveler needs:</p>
    
    <ul>
      <li><strong>Built-in power bank (USB/USB-C)</strong> for on-the-go charging.</li>
      <li><strong>Global GPS tracker</strong> to ensure your luggage is always within reach.</li>
      <li><strong>Smart scale</strong> to prevent overweight surprises at the airport.</li>
      <li><strong>Anti-loss alarm</strong> for peace of mind in crowded terminals.</li>
    </ul>
    
    <p>Built with durability and style in mind, Simptech Smart Luggage embodies our mission to merge <strong>cutting-edge technology with timeless design</strong>. Travel smarter. Travel simpler. Travel with Simptech.</p>
  </article>
</body>"""


a4 = """<head>
  <meta charset="UTF-8">
  <style>
    body {font-family: Arial, Helvetica, sans-serif; line-height: 1.6; margin: 40px; background-color: #f9f9f9; color: #333;}
    article {max-width: 800px; margin: auto; background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
    h2 {color: #222; margin-bottom: 20px;}
    p {margin-bottom: 15px;}
    strong {color: #000;}
    em {color: #666;}
  </style>
</head>
<body>
  <article>
    <p>At Simptech, our journey began with a simple question: <em>why should travel feel complicated?</em> We saw modern professionals and travelers struggling with heavy bags, misplaced items, dead batteries, and chaotic packing systems. Instead of creating just another bag, we set out to design <strong>a travel companion that blends innovation, intelligent functions, and minimalist aesthetics</strong>.</p>
    
    <p>From our very first <strong>Smart Luggage</strong>, equipped with a built-in power bank, GPS tracker, anti-loss alarm, and smart scale, we made a promise: <em>technology should simplify, not complicate</em>. This philosophy continues to guide us as we expand into smart backpacks, modular bags, and high-tech organizers.</p>
    
    <p>With Simptech, every product is more than just a bag — it’s a reflection of our belief that <strong>smart mobility leads to a simpler, more efficient lifestyle</strong>.</p>
  </article>
</body>"""

class ArticleState(rx.State):
    """State for a single news article."""

    articles_db: dict[str, Article] = {
        "Looking Ahead: Simptech’s Vision for the Future of Travel": {
            "id": "Looking Ahead: Simptech’s Vision for the Future of Travel",
            "title": "Looking Ahead: Simptech’s Vision for the Future of Travel",
            "date": "November 12, 2024",
            "content": a1,
        },
        "Smart Backpacks & Modular Bags: Simptech Expands Its Core Collection":{
            "id": "Smart Backpacks & Modular Bags: Simptech Expands Its Core Collection",
            "title": "Smart Backpacks & Modular Bags: Simptech Expands Its Core Collection",
            "date": "October 26, 2024",
            "content": a2,
        },
        "Introducing Simptech Smart Luggage: A New Era of Intelligent Travel":{
            "id": "Introducing Simptech Smart Luggage: A New Era of Intelligent Travel",
            "title": "Introducing Simptech Smart Luggage: A New Era of Intelligent Travel",
            "date": "May 15, 2024",
            "content": a3,
        },
        "Simptech’s Origin: Redefining Travel with Simplified Technology":{
            "id": "Simptech’s Origin: Redefining Travel with Simplified Technology",
            "title": "Simptech’s Origin: Redefining Travel with Simplified Technology",
            "date": "March 28, 2024",
            "content": a4,
        }
    }
    article: Article | None = None

    async def get_article(self):
        """Get the article from the database based on the article_id param."""
        article_id = self.router.page.params.get(
            "article_id", "no-id"
        )
        self.article = self.articles_db.get(article_id)