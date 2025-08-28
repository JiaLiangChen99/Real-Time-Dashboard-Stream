import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    img_url: str
    product_id: str
    name: str
    description: str
    price: float


class IndexProduct(TypedDict):
    name: str
    image_url: str


class Testimonial(TypedDict):
    author: str
    role: str
    quote: str
    avatar_seed: str


class HeroSectionContent(TypedDict):
    title: str
    subtitle: str
    button_text: str
    button_url: str
    background_image: str


class ShowcaseSectionContent(TypedDict):
    image_url: str
    title: str
    subtitle: str
    button_text: str
    button_url: str


class Feature(TypedDict):
    icon: str
    title: str
    text: str


class BrandStorySectionContent(TypedDict):
    title: str
    features: list[Feature]


class HomePageContent(TypedDict):
    hero: HeroSectionContent
    showcase: ShowcaseSectionContent
    brand_story: BrandStorySectionContent


class State(rx.State):
    """The app state."""

    is_mobile_menu_open: bool = False
    show_help_menu: bool = False
    products: list[Product] = [
        {
            "product_id": "item-001",
            "name": "Simptech Smart Luggage",
            "description": "Travel with confidence and convenience. Simptech Smart Luggage is equipped with a built-in power bank (USB/USB-C), global GPS tracker, anti-loss alarm, and a smart scale to prevent overweight surprises. Designed for modern travelers who value both technology and simplicity.",
            "price": 2999.99,
            "img_url": "/black_suitcase_features.png"
        },
        {
            "product_id": "item-002",
            "name": "Simptech Smart Backpacks & Commuter Bags",
            "description": "Engineered for professionals and tech enthusiasts on the go. These backpacks feature integrated charging systems, cable management, anti-theft locks, and RFID-blocking pockets to protect sensitive information. Crafted with water-resistant, scratch-resistant Codura fabric, they are built for durability and security.",
            "price": 1499.5,
            "img_url": "/smartbackpag.png"
        },
        {
            "product_id": "item-003",
            "name": "Simptech Modular Multi-Functional Bags",
            "description": "One bag, endless possibilities. With magnetic quick-release buckles, detachable inner compartments, and customizable dividers, you can easily adapt your bag for business, leisure, or short trips. Simptech Modular Bags are designed to fit seamlessly into every lifestyle.",
            "price": 7500.0,
            "img_url": "/partition_tech_organizer.png"
        },
        # {
        #     "product_id": "item-004",
        #     "name": "Simptech High-Tech Accessories & Organizers",
        #     "description": "Stay organized, stay ready. From anti-bacterial electronic organizers and cable storage cases to smart compression bags for clothing, Simptech accessories bring technology and functionality together for a simplified travel experience.",
        #     "price": 7500.0,
        #     "img_url": "/partition_tech_organizer.png"
        # },
    ]
    index_products: list[IndexProduct] = [
        {
            "name": "Smart Suitcase",
            "image_url": "/black_suitcase_features.png",
        },
        {
            "name": "Smart Backpack",
            "image_url": "/smartbackpag.png",
        },
        {
            "name": "Multifunctional bag",
            "image_url": "/partition_tech_organizer.png",
        },
        # {
        #     "name": "Smart storage box",
        #     "image_url": "/partition_tech_organizer.png",
        # },
    ]
    testimonials: list[Testimonial] = [
        {
            "author": "Alex R.",
            "role": "Tech Enthusiast",
            "quote": "The smart carry-on is a game-changer! The built-in charger and GPS tracker give me so much peace of mind when traveling. Absolutely brilliant.",
            "avatar_seed": "Alex",
        },
        {
            "author": "Samantha B.",
            "role": "Frequent Flyer",
            "quote": "I'm in love with my Tech Backpack. It's sleek, durable, and keeps all my gadgets organized and charged. The anti-theft features are a huge plus.",
            "avatar_seed": "Samantha",
        },
        {
            "author": "Michael T.",
            "role": "Digital Nomad",
            "quote": "Simptech's modular duffel is incredibly versatile. I can customize it for a weekend trip or a long-haul journey. The quality is top-notch.",
            "avatar_seed": "Michael",
        },
        {
            "author": "Jessica L.",
            "role": "Corporate Professional",
            "quote": "Finally, a bag that understands my needs. The minimalist design is so professional, and the smart features make my daily commute so much easier.",
            "avatar_seed": "Jessica",
        },
    ]
    current_testimonial_index: int = 0
    homepage_content: HomePageContent = {
        "hero": {
            "title": "Destination: Future",
            "subtitle": "Celebrate the journey with Simptech's smart luggage, where technology and simplicity meet.",
            "button_text": "EXPLORE THE DESTINATIONS",
            "button_url": "/products",
            "background_image": "/suitcase_travel_person.png",
        },
        "showcase": {
            "image_url": "/white_suitcase_features.png",
            "title": "EXPLORE THE OUTDOORS LIKE NEVER BEFORE WITH OUR SIGNATURE SMART LUGGAGE!",
            "subtitle": "Finally, stylish, durable smart luggage with the comfort and features you need for tough trails, easy walks - and every adventure in between!",
            "button_text": "VIEW ALL SMART LUGGAGE",
            "button_url": "/products",
        },
        "brand_story": {
            "title": "Our Brand Story",
            "features": [
                {
                    "icon": "cpu",
                    "title": "Simple Technology",
                    "text": "We integrate innovative tech and smart functions to solve real travel pain points.",
                },
                {
                    "icon": "shield-check",
                    "title": "Practical & Durable",
                    "text": "Our focus is on making products more practical, durable, and convenient for your journey.",
                },
                {
                    "icon": "gem",
                    "title": "Minimalist Aesthetics",
                    "text": "For modern individuals who value efficiency, quality, and minimalist design.",
                },
            ],
        },
    }

    @rx.var
    def current_product(self) -> Product | None:
        """Get the product for the current page."""
        product_id = self.router.page.params.get(
            "product_id"
        )
        if not product_id:
            return None
        for product in self.products:
            if product["product_id"] == product_id:
                return product
        return None

    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = (
            not self.is_mobile_menu_open
        )

    def toggle_help_menu(self):
        self.show_help_menu = not self.show_help_menu

    def next_testimonial(self):
        self.current_testimonial_index = (
            self.current_testimonial_index + 1
        ) % len(self.testimonials)

    def prev_testimonial(self):
        self.current_testimonial_index = (
            self.current_testimonial_index
            - 1
            + len(self.testimonials)
        ) % len(self.testimonials)

    def set_testimonial(self, index: int):
        self.current_testimonial_index = index

    @rx.var
    def current_testimonial(self) -> Testimonial:
        return self.testimonials[
            self.current_testimonial_index
        ]