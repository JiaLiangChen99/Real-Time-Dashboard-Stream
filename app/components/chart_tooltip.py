import reflex as rx

TOOLTIP_PROPS = {
    "is_animation_active": False,
    "separator": ": ",
    "cursor": {
        "stroke": "#A1A1AA",
        "strokeWidth": 1,
        "strokeDasharray": "3 3",
    },
    "item_style": {"color": "#4B5563"},
    "label_style": {
        "fontWeight": "600",
        "color": "#1F2937",
    },
    "content_style": {
        "backgroundColor": "rgba(255, 255, 255, 0.8)",
        "borderColor": "#E5E7EB",
        "borderRadius": "0.75rem",
        "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
        "backdropFilter": "blur(4px)",
    },
}