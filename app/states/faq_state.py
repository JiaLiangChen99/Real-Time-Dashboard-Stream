import reflex as rx
from typing import TypedDict
from collections import defaultdict


class FAQItem(TypedDict):
    id: int
    category: str
    question: str
    answer: str


class FAQState(rx.State):
    """State for the FAQ page."""

    faq_items: list[FAQItem] = [
        {
            "id": 1,
            "category": "Product Related",
            "question": "What's the difference between Simptech luggage and regular luggage?",
            "answer": 'Our core philosophy is "Simplifying travel with technology." Simptech products not only feature minimalist aesthetics but also integrate smart functions like built-in power banks, GPS tracking, anti-theft systems, and modular storage, making travel more efficient, secure, and convenient.',
        },
        {
            "id": 2,
            "category": "Product Related",
            "question": "How does the smart luggage's GPS tracking work?",
            "answer": "The GPS module connects to our companion mobile app, allowing you to view your luggage's real-time location on your phone. If your luggage is lost or misplaced during your journey, you can quickly locate and retrieve it.",
        },
        {
            "id": 3,
            "category": "Product Related",
            "question": "Is the charging function safe? What devices does it support?",
            "answer": "All smart luggage and backpacks are safety certified and feature a removable battery design, compliant with most airline regulations for carry-on luggage. The USB and USB-C ports can charge mainstream devices such as phones, tablets, and laptops.",
        },
        {
            "id": 4,
            "category": "Product Related",
            "question": 'How do the modular bags achieve "multi-scenario use"?',
            "answer": "Simptech's modular system uses magnetic quick-release buckles and detachable liners, allowing users to customize combinations based on different needs. For example, add a laptop compartment for business trips, or switch to a clothing storage compartment for weekend getaways—one bag, multiple uses.",
        },
        {
            "id": 5,
            "category": "Usage and Maintenance",
            "question": "Can the battery be checked in on a flight?",
            "answer": "According to International Air Transport Association (IATA) regulations, luggage containing lithium batteries must be carried on. Simptech's battery is designed to be removable, so you can easily take it out and bring it into the cabin, ensuring a worry-free boarding experience.",
        },
        {
            "id": 6,
            "category": "Usage and Maintenance",
            "question": "Is the luggage waterproof?",
            "answer": "Yes, we use high-strength, waterproof, and scratch-resistant materials like Cordura fabric, which can effectively prevent rain or liquid splashes. However, prolonged immersion should still be avoided.",
        },
        {
            "id": 7,
            "category": "Usage and Maintenance",
            "question": "How to clean and maintain it?",
            "answer": "We recommend gently wiping with a damp cloth or a neutral detergent. Avoid using corrosive cleaning liquids. Please do not machine wash or soak for extended periods to prevent damage to the smart modules.",
        },
        {
            "id": 8,
            "category": "Shopping and After-sales",
            "question": "Where can I buy Simptech products?",
            "answer": "You can purchase directly from our official website. We are also available on online channels like Amazon and Best Buy, as well as in select travel goods stores and electronics retailers.",
        },
        {
            "id": 9,
            "category": "Shopping and After-sales",
            "question": "Do you support international shipping?",
            "answer": "Yes, Simptech offers global shipping. Shipping costs and estimated delivery times will be calculated automatically at checkout.",
        },
        {
            "id": 10,
            "category": "Shopping and After-sales",
            "question": "What is your warranty policy?",
            "answer": "All Simptech products come with a 1-year limited warranty covering manufacturing defects and functional failures. For non-man-made damage, we will provide repair or replacement services.",
        },
        {
            "id": 11,
            "category": "Shopping and After-sales",
            "question": "If the product is damaged, can the smart module be replaced separately?",
            "answer": "Yes. We offer separate sales and upgrade services for smart modules. You don't need to replace the entire piece of luggage; simply replace the corresponding module to restore its functionality.",
        },
        {
            "id": 12,
            "category": "App and Smart Features",
            "question": "Do I need to download an app to use the smart features?",
            "answer": "Yes. Our companion app allows you to check battery levels, use GPS positioning, remotely lock your luggage, and manage your travel checklists. The app is available for both iOS and Android systems.",
        },
        {
            "id": 13,
            "category": "App and Smart Features",
            "question": "If I change my phone, can I still use my luggage?",
            "answer": "Yes. Just re-download the Simptech app on your new phone and log in to your account to reconnect and sync with your luggage.",
        },
    ]
    open_items: dict[int, bool] = {}

    def toggle_item(self, item_id: int):
        if item_id in self.open_items:
            self.open_items[item_id] = not self.open_items[
                item_id
            ]
        else:
            self.open_items[item_id] = True

    @rx.var
    def faq_by_category(self) -> dict[str, list[FAQItem]]:
        """Group FAQs by category."""
        categorized = defaultdict(list)
        for item in self.faq_items:
            categorized[item["category"]].append(item)
        return categorized

    @rx.var
    def categories(self) -> list[str]:
        """Get a list of unique category names."""
        return list(self.faq_by_category.keys())  # pyright: ignore[reportAttributeAccessIssue]