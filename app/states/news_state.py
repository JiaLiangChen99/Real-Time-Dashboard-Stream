import reflex as rx
from typing import TypedDict


class NewsArticle(TypedDict):
    id: str
    title: str
    date: str
    description: str
    image_url: str


class NewsState(rx.State):
    """State for the News page."""

    articles: list[NewsArticle] = [
        {
            "id": "brand-story",
            "title": "The Simptech Story: Simplifying Modern Travel",
            "date": "November 1, 2023",
            "description": "Discover the mission and innovation behind Simptech, a brand dedicated to making every journey seamless and stress-free.",
            "image_url": "/simptech_brand_story.png",
        },
        {
            "id": "smart-carry-on-pro-launch",
            "title": "Simptech Launches the new Smart Carry-On Pro",
            "date": "October 26, 2023",
            "description": "Experience the future of travel with our latest innovation, featuring a removable battery, GPS tracking, and a sleek, durable design.",
            "image_url": "/placeholder.svg",
        },
        {
            "id": "sustainability-commitment",
            "title": "Our Commitment to Sustainable Materials",
            "date": "October 15, 2023",
            "description": "We're proud to announce that our new line of products is made from 100% recycled polycarbonate and eco-friendly leather.",
            "image_url": "/placeholder.svg",
        },
        {
            "id": "design-excellence-award",
            "title": "Simptech Recognized for Design Excellence",
            "date": "September 28, 2023",
            "description": "The Simptech Tech Backpack has won the prestigious Red Dot Design Award for its blend of minimalist aesthetics and smart functionality.",
            "image_url": "/placeholder.svg",
        },
        {
            "id": "mobile-app-guide",
            "title": "Travel Smart: A Guide to Our New Mobile App",
            "date": "September 10, 2023",
            "description": "Unlock the full potential of your Simptech gear. Learn about remote locking, location tracking, and trip planning features.",
            "image_url": "/placeholder.svg",
        },
        {
            "id": "clean-travel-partnership",
            "title": "Partnership with 'Clean Travel' Initiative",
            "date": "August 22, 2023",
            "description": "We are joining forces with environmental non-profits to promote responsible tourism and reduce our carbon footprint.",
            "image_url": "/placeholder.svg",
        },
    ]